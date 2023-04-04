import pyttsx3

def generate_audio(text):
    engine = pyttsx3.init() 
    engine.say(text) 
    engine.runAndWait()