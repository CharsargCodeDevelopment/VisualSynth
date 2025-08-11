import wave
import struct
import time
import numpy as np
samplerate = 44100
filename = "output.wav"
#global SaveSample

mode = "numpy"
def Activate():
    global file
    file = wave.open(filename,mode = "wb")
    file.setnchannels(2)
    file.setsampwidth(2)
    file.setframerate(samplerate)
def SaveSample(left_channel, right_channel):
    if mode == "numpy":
        SaveSampleNumpy(left_channel, right_channel)
    if mode == "list":
        SaveSampleList(left_channel,right_channel)

def SaveSampleList(left_channel,right_channel):
    startTime = time.time()
    for samples in zip(left_channel,right_channel):
        for sample in samples:
            #sample = math.sin(math.radians(i))
            sample = int(sample * (2 ** 15 - 1))
            file.writeframes(struct.pack("<h", sample))
    #print(time.time() - startTime)

def SaveSampleNumpy(left_channel, right_channel):
    startTime = time.time()
    # Combine the two channels into a single NumPy array
    interleaved = np.stack((left_channel, right_channel), axis=1).flatten()
    
    # Scale and convert to 16-bit integers
    interleaved_int = (interleaved * (2**15 - 1)).astype(np.int16)
    
    # Write the frames to the WAV file
    file.writeframes(interleaved_int.tobytes())
    #print(time.time() - startTime)

def DeActivate():
    file.close()


"""
samplerate = 44100
filename = "output.wav"
file = wave.open(filename,mode = "wb")


import math

file.setnchannels(2)
file.setsampwidth(2)
file.setframerate(samplerate)


left_channel = [
    0.5 * math.sin(math.radians(360) * 440.0 * i / samplerate) for i in range(samplerate)
]
right_channel  = [0 for _ in range(samplerate)]

for samples in zip(left_channel,right_channel):
    for sample in samples:
        #sample = math.sin(math.radians(i))
        sample = int(sample * (2 ** 15 - 1))
        file.writeframes(struct.pack("<h", sample))
for samples in zip(right_channel,left_channel):
    for sample in samples:
        #sample = math.sin(math.radians(i))
        sample = int(sample * (2 ** 15 - 1))
        file.writeframes(struct.pack("<h", sample))


file.close()


"""
