from vosk import Model, KaldiRecognizer, SetLogLevel # vosk 
import sys # for fetching arg from CLI
import os # os operations
import wave # handle audio wav files
import pyaudio

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16, channels=1, rate = 16000, input = True, frames_per_buffer = 4000)
stream.start_stream()

SetLogLevel(0) # debug level 0 for output on terminal

kherem = "хэрэм";
print("хэрэм байна")

#Modeliinho zamiig zaaj ogoh heregtei ba 
if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

#Audiogoo wav esehiig shalgaj baina
wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)

while True:
    data = wf.readframes(4000, exception_on_overflow = False)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
                if rec.Result("гэрэл ас"):
                    print("sonsloo " + rec.Result())
                    print("Pi: " + "аслаа" )
                    led.on();
                    print(rec.Result())

                if rec.Result("гэрэл унтар"):
                    print("sonsloo " + rec.Result())
                    print("Pi: " + "унтарлаа" )
                    led.off();
    else:
        print(rec.PartialResult())

print(rec.FinalResult())
