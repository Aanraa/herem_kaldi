from vosk import Model, KaldiRecognizer, SetLogLevel # Vosk 
import pyaudio # Audio orolt garalttai ajilladag san
import os
import json
import sys
import datetime as dt
from playsound import playsound
# from gpiozero import LED

mic = pyaudio.PyAudio()

if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

def print_w_date_time(alert, event_time = None):
    if event_time is None : event_time = dt.datetime.now()
    str_event_time = event_time.strftime("%Y-%m-%d %H-%M-%S")
    print("{} {}".format(str_event_time, alert))

SetLogLevel(1)

keywords = '["хэрэм", "[unk]"]' 
model = Model("model")
rec = KaldiRecognizer(model, 16000, keywords)

cap = pyaudio.PyAudio()
stream = cap.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8192)
stream.start_stream()

print("Sonsoj baina")
def wake():
    while True:
        try:
            data = stream.read(4096, exception_on_overflow = False)
            if rec.AcceptWaveform(data):
                result = rec.Result()
                json1 = json.loads(result)
                resp = json1["text"]
                print("kkk>>", resp)

                if(resp == "хэрэм"):
                    playsound('squirrel1.wav')
                    print("That's right")
                    print_w_date_time("Wake word detected")
                    stream.close()
                    return resp
                else :
                    pass
        except KeyboardInterrupt:
            break
   