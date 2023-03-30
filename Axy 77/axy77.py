import time 
from chatbotb import ChatbotBrain
import pyttsx3
import speech_recognition as sr

listener = sr.Recognizer()

engine = pyttsx3.init()

engine.say("Hola, yo soy axi, tu auxiliar emocional personal")
engine.runAndWait()


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
    except:
        pass
    return flag

class VoiceRecognitionModule:
    def __init__(self, key=None):
        self.key = key
        self.r = sr.Recognizer()

    def recognize(self):
        with sr.Microphone() as source:
            print("Speak Anything : ")
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio, key=self.key, language="es")
                return text
            except:
                return None


class SpeechModule:
    def __init__(self, voice=0, volume=1, rate=125):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)

        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[voice].id)

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

context = """who are you?
My name is Pequenin, I'm a robot from the future, I'm trapped \
in a teddy bear, I hate people and I love to wet people, Hector \
Pulido is my master, I am very grumpy, and I'm in the Hector twitch chat"""

translation_artifacts_english = {"Disagreement": "Discord"}

translation_artifacts_spanish = {
    "pequenina": "Pequeñin",
    "osito de peluche": "Oso Teddy",
    "profesor": "Maestro",
}
chatbot = ChatbotBrain(
    context,
    translation_artifacts_english,
    translation_artifacts_spanish,
    "microsoft/DialoGPT-large",
    "microsoft/DialoGPT-large",
    True,
    True,
)

speech = SpeechModule()
recognition = VoiceRecognitionModule()

while True:
    text = recognition.recognize()

    if text:
        chatbot_text = chatbot.talk(text)
        speech.talk(chatbot_text)
    else:
        speech.talk("No te he entendido")
    time.sleep(1)

    
