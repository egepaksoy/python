import speech_recognition as sr
import speak


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='en-Us')
        except sr.UnknownValueError:
            speak('sorry boss i cant understand')

        except sr.RequestError:
            print("Server error")

        return voice