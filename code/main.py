from microphone import listen
from brain import ask
from speaker import speak

WAKE_WORD = "lily"

def strip_wake_word(text):
    lower_text = text.lower()
    if WAKE_WORD in lower_text:
        position = lower_text.find(WAKE_WORD) + len(WAKE_WORD)
        return text[position:].strip()
    return None


if __name__ == "__main__":
    print("Lilybot ready. Say the wake word to talk.")

    while True:
        heard = listen()
        command = strip_wake_word(heard)

        if command is None:
            continue

        if not command:
            speak("Yes?")
            command = listen()

        response = ask(command)
        speak(response)
