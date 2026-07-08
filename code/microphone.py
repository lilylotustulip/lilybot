import sounddevice as sd
import queue
import json 
import vosk 

MODEL_PATH = "/home/lilybot/lilybot/code/vosk-model-small-en-us-0.15"
SAMPLE_RATE = 16000

model = vosk.Model(MODEL_PATH)
audio_queue = queue.Queue()

def callback(indata, frames, time, status):
    audio_queue.put(bytes(indata))

def listen():
    rec = vosk.KaldiRecognizer(model, SAMPLE_RATE)

    with sd.RawInputStream(samplerate=SAMPLE_RATE, blocksize=8000,
                            dtype='int16', channels=1, callback=callback):
        print("Listening...")
        while True:
            data = audio_queue.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    return text


if __name__ == "__main__":
    while True:
  
        spoken_text = listen()
        print("You said:", spoken_text)
