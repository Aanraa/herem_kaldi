from email.mime import audio
from sklearn.metrics import auc
import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak :")
    audio = r.listen(source)

try :
    print("you said :" + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Unknown val")


