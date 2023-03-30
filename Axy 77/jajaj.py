import time
import speech_recognition
from chatbotb import ChatbotBrain
import speech_recognition as sr

import pyttsx3


class SpeechModule:

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


