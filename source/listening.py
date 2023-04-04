from ansi.colour import fg
import speech_recognition as sr

def listen_petition():
    # Obtain audio for microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(fg.boldblue("\nDi algo\n"),"----"*10,end="\n")
        # r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)

    try:
        output = r.recognize_google(audio, language="es-Es")
        return output
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

