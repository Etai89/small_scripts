import wave
import pyaudio
import sys
import os
from threading import Thread
from datetime import datetime
import time

time_to_record = 60 # in seconds

recording = False  # global variable to control recording loop
frames = []  # global variable to store audio frames

def record():
    global frames
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    base_dir = "C:\\Users\\senio\\OneDrive\\Desktop\\recordings"
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".wav"
    WAVE_OUTPUT_FILENAME = os.path.join(base_dir, filename)

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    while recording:
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))  # write the frames to the WAV file
    wf.close()

def start_recording():
    global recording
    recording = True
    t = Thread(target=record)
    t.start()
    
    print("Start")

def stop_recording():
    global recording
    recording = False

    print("End")

# Example usage:

# Allow recording for 10 seconds (adjust as needed)
#time.sleep(600)

start_recording()
time.sleep(time_to_record)
stop_recording()
