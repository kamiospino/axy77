import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia
import webbrowser
import pyjokes

# name of the virtual assistant
name = 'axi'

# the flag help us to turn off the program
flag = 1

listener = sr.Recognizer()

engine = pyttsx3.init()

engine.say("Hola, yo soy axi, tu auxiliar emocional personal")
engine.runAndWait()

# get voices and set the first of them
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# editing default configuration
engine. setProperty('rate', 178)
engine.setProperty('volume', 0.7)


def talk(text):
    '''
        here, virtual assistant can talk
    '''
    engine.say(text)
    engine.runAndWait()
    

def listen():
    '''
        The program recover our voice and it sends to another function
    '''
    flag = 1
    try:
        with sr.Microphone() as source:
            talk("Te escucho")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            
            if name in rec:
                rec = rec.replace(name, '')
                flag = run(rec)
            else:
                talk("¿Puedes volver a intentarlo?, no pude entenderte bien: " + rec)
    except:
        pass
    return flag


def run(rec):
    '''
        All the actions that virtual assistant can do
    '''
    if 'mal' in rec:
        talk("que pasa")
    else:
        talk("¿Puedes volver a intentarlo?, no pude entenderte bien")
    return flag
 

while flag:
    flag = listen()