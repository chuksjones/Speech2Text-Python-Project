import pyttsx3
import speech_recognition as sr

def get():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("Recognizing...")
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except Exception as e:
            print(e)
        
get()