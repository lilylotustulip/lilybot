import subprocess
import sys
import numpy as np

piper_bin = "/home/lilybot/lilybot/code/piper/piper"
model_path = "/home/lilybot/lilybot/code/piper/en_US-amy-low.onnx"

def speak(text):
    piper_proc = subprocess.Popen(
        [piper_bin, "--model", model_path, "--output-raw"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    raw_audio, _ = piper_proc.communicate(input=text.encode())

    samples_16bit = np.frombuffer(raw_audio, dtype=np.int16)

    upsampled = np.repeat(samples_16bit, 3)

    samples_32bit = upsampled.astype(np.int32) * 65536

    stereo = np.empty(samples_32bit.size * 2, dtype=np.int32)
    stereo[0::2] = samples_32bit
    stereo[1::2] = samples_32bit

    aplay_proc = subprocess.Popen(
        ["aplay", "-r", "48000", "-f", "S32_LE", "-t", "raw", "-c", "2", "-D", "hw:0,0"],
        stdin=subprocess.PIPE
    )
    aplay_proc.communicate(input=stereo.tobytes())


if __name__ == "__main__":
    full_text = " ".join(sys.argv[1:])
    if full_text:
        speak(full_text)
