from vosk import Model, KaldiRecognizer, SetLogLevel # Vosk 
import pyaudio # Audio orolt garalttai ajilladag san
import os
import json
from wake_word import wake
from playsound import playsound
#from gpiozero import LED

#led1 = LED(6)
#led2 = LED(8)

mic = pyaudio.PyAudio()

if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

SetLogLevel(1)
model = Model("model")
rec = KaldiRecognizer(model, 16000)

listening = False
full = False

def get_command():
        listening = True
        stream = mic.open(format = pyaudio.paInt16, channels=1, rate = 16000, input = True, frames_per_buffer = 8192)
        while listening:
            stream.start_stream()
            try:
                data = stream.read(4096, exception_on_overflow = False)
                if rec.AcceptWaveform(data):
                    result = rec.Result()
                    json1 = json.loads(result)
                    response = json1["text"]
                    listening = False
                    stream.close()
                    return response         
            except OSError:
                pass

def analyze_data(command):
    try:
        if command == 'том өрөөний гэрэл ас':
            print("a")
            #led1.on()
        elif command == 'том өрөөний гэрэл унтар':
            print("b")
            #led1.off()
        elif command == 'гал тогооны гэрэл ас':
            print("c")
            #led2.on()
        elif command == 'гал тогооны гэрэл унтар':
            print("d")
            #led2.off()
        else :
            print("Buruu ug baina")
    except Exception:
        pass

    
try:
    resp = wake()
    if resp == "хэрэм":
        full = True
        while full :
            print("Tushaal huleej baina....")
            command = get_command()
            analyze_data(command)
    else :
        pass        
except KeyboardInterrupt:
    print("\n\nExit tovch daragdlaa")    