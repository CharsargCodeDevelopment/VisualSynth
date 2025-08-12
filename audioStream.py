import sounddevice as sd
import numpy as np


import queue

# Create a queue for our audio data
q = queue.Queue(maxsize=2)

blockSize = 640



def callback(outdata, frames, time, status):
    """This is our callback function. It gets called by the output stream."""
    if status:
        print("status:",status)
    while frames > 0:
        try:
            # Try to get data from the queue
            data = (q.get_nowait())
            #data = data[:1136]
            data = data[:blockSize]
            size = len(data)
            #size = min(1136,size)
            size = min(blockSize,size)
            #print(data.shape)
            #reshaped_data = data.reshape(-1, 1) 
            outdata[:size] = data
            frames -= size
        except queue.Empty:
            # If the queue is empty, fill the rest with zeros
            outdata.fill(0)
            #outdata[:] = 0
            frames = 0

def QueueFull():
    return q.full()

def GenerateAudio():
    return not QueueFull()


def QueueClear():
    q.queue.clear()

def QueuePut(samples):
    i = 0
    if QueueFull():
        print("Full")
    while len(samples) > 0:
        i+=1
        #data = samples[:1136]
        data = samples[:blockSize]
        q.put(data)
        #samples = samples[1136:]
        samples = samples[blockSize:]
    #print(i)



def pad_list(lst, padding):
    """Pads out a list by repeating each element a specified number of times.

    Args:
        lst: The input list.
        padding: The number of times to repeat each element.

    Returns:
        A new list with each element repeated 'padding' times.
    """
    if padding <= 0:
        return lst
    """
    
    padded_list = []
    for item in lst:
        padded_list.extend([item] * padding)
        
    return padded_list
    """
    return np.repeat(lst, padding)
    #return [item for item in lst for _ in range(padding)]

def PlaySample(samplesL,samplesR):
    #sr = len(samples)/time
    #sr = int(sr)
    #print(sr)
    #pad = int((time*44100) / len(samples))
    #samples = pad_list(samples,pad)
    #sr = int(len(samples)/time)
    #print(sr)
    #sd.play(samples,min(sr,44100))
    #q.put(np.array(samples))
    #print(np.array(samples))
    stereo_samples = np.column_stack([samplesL, samplesR])
    QueuePut(np.array(stereo_samples))
    #sd.wait()
    #sd.play(samples,44100)


stream = sd.OutputStream(callback=callback, samplerate=44100, channels=2,latency = 0.1)

stream.start()
print(stream.blocksize)
#QueuePut(np.sin(2 * np.pi * 440 * np.linspace(0, 2, 44100 * 2)))  # 2 seconds of a sine wave


print(pad_list([0,1,2,3],2))
