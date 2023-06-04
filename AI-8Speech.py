#pip install pyttsx3=2.6
#pip install Speechrecognition
import pyttsx3
import datetime
import speech_recognition as sr
engine=pyttsx3.init('sapi5')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishUser():
    speak("hello this is python speaking..")

    hour=int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour<12:
        speak("very good morning everyone..")
    elif hour>=12 and hour<18:
        speak("very good afternoon everyone..")
    else:
        speak("very good evening everyone..")


    speak("welcome to speech recognition  sesion in python")
    speak("i am your pilot bhushan Pusadkar and my copilot kalyani")
    speak("We are ready to takeoff")
    speak("Thanks for your support")
    speak("see you in the next program")
    speak("Test to speech  is very interesting ")

    wishUser()