#from gpiozero import led
import struct
from vosk import Model, KaldiRecognizer, SetLogLevel # Vosk 
import sys # CLI-аас arg татахад зориулагдсан
import os # os үйл ажиллагаа
import wave # wav ugugdluudiig udirdahad zoriulagdsan
import pyaudio # Audio orolt garalttai ajilladag san
import webrtcvad #
import gpiozero

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16, channels=1, rate = 16000, input = True, frames_per_buffer = 8192)
stream.start_stream()


"""
handle = pvporcupine.create(keywords=['herem', ''])
porcupine = None
pa = None
audio_stream = None
def get_next_audio_frame():
    pass

while True:
    keyword_index = handle.process(get_next_audio_frame())
    if keyword_index >= 0:
        # Insert detection event callback here
        print('Yes sir?')
        pass

            try:
                porcupine = pvporcupine.create(keywords=["computer", "jarvis"])

                pa = pyaudio.PyAudio()

                audio_stream = pa.open(
                    rate=porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=porcupine.frame_length)

        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                print("Hotword Detected")
                speak("Computer online")
                break
"""
SetLogLevel(0) # debug level 0 for output on terminal

#led = LED(17)
kherem = "хэрэм";
print("хэрэм байна")

#Modeliinho zamiig zaaj ogoh heregtei ba 
if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)
    
model = Model("model")
rec = KaldiRecognizer(model, 16000)
rec.SetWords(True)


while True:
    data = stream.read(4096, exception_on_overflow = False)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
                if  rec.Result() == "гэрэл ас":
                    print("Pi: " + "аслаа" )
                    #led.on();

                elif rec.Result() == "гэрэл унтар":
                    print("Pi: " + "унтарлаа" )
                    #led.off();

    
