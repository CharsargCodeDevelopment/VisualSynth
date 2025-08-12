import ModularInterface
import ModularInterface.UI


import ModularLuaInterface
import ModularLuaInterface.LoadCore


import time


import audioStream
import midiStream

ModularInterface.UI.ActivateCore(core = "pygame")
ModularLuaInterface.LoadCore.ActivateCore()


GenerationRuntime = ModularLuaInterface.Core.Lua()



LuaCode = ""

with open("default.lua") as file:
    LuaCode = file.read()


GenerationFunction = GenerationRuntime.eval(LuaCode)


"""
#ModularInterface.UI.Window


Preview = ModularInterface.Core.Window()

ModularInterface.Core.AddImage(Preview,128,128)

Preview.ImageManager.set_pixel(5, 5, (0,0,0))
#Preview.root.update()
#ModularInterface.UI.FillImage(IM = Preview.ImageManager)
Preview.ImageManager.fill_image((0,0,0))
Preview.ImageManager.update_image()
Preview.root.update()
"""


targetSampleRate = 44100
drawBufferSize = 2048
soundBufferSize = int(targetSampleRate*1)
soundBufferSize = 1136
soundBufferSize = audioStream.blockSize
#soundBufferSize = 2048
#soundBufferSize = 640
#soundBufferSize = 1024
positions = []
LeftChannel = []
RightChannel = []



VisualAudioPreview = ModularInterface.Core.Window(width = 1024,height = 1024)
ModularInterface.Core.AddImage(VisualAudioPreview,1024,1024)


running = True

import math
t = 0


deltaTime = 0



frameStart = time.time()
scale = 64

writeTime = 0
volume = 0.05

minGap = 1/targetSampleRate


frameTimer = time.time()

i = 0
inputTimer = 0

activeFrequencies = [440]

enable_midi = True

VisualAudioPreview.update()

#channel = int(input("Enter Channel: "))
channel = -1
midiStream.Activate()


while running:
    inputTimer+=1
    if inputTimer > 1 and enable_midi:
        inputTimer=0
        #midiStream.GetInputs(channel = channel)
        activeFrequencies = []
        #print(set(midiStream.notes))
        for note in set(midiStream.notes):
            activeFrequencies.append(midiStream.noteToFreq(note))
        #print(activeFrequencies)
        if len(activeFrequencies) == 0:
            audioStream.QueueClear()
    #print("Test")
    #time.sleep(minGap*4)
    
    
    deltaTime = time.time()-frameStart
    #deltaTime = minGap
    #while deltaTime < minGap*0.5:
    #    deltaTime = time.time()-frameStart
    frameStart = time.time()
    
    #print(deltaTime,len(positions))
    #t+=deltaTime
    if audioStream.GenerateAudio():
        t+= minGap


        l,r = math.sin(math.radians(t*440*360)),math.cos(math.radians(t*440*360))
        #l,r = 0,0
        l,r = (GenerationFunction(t,activeFrequencies))
        x,y = l,r
        l = l*volume
        r = r*volume
        l = max(-1,min(1,l))
        r = max(-1,min(1,r))

    

        LeftChannel.append((l))
        RightChannel.append((r))
    
        #x,y = x+1,y+1
        x,y = (int(scale*x)+512,int(scale*y)+512)
        positions.append((x,y))
    while len(positions) > drawBufferSize:
        positions.pop(0)
    #if len(positions)-1 > drawBufferSize:
     #   positions = []
    writeTime += deltaTime
    if len(LeftChannel) >= soundBufferSize or len(RightChannel) >=  soundBufferSize:
        playStart = time.time()
        
        #audioStream.PlaySample(LeftChannel,writeTime)
        
        audioStream.PlaySample(LeftChannel,RightChannel)
        #print(time.time()-playStart)
        #print(writeTime,len(LeftChannel)/44100)
        LeftChannel = []
        RightChannel = []
        writeTime = 0

    
    #i+=1
    #if time.time()-frameTimer > 0.05:
    #if i > 500:
        #i=0
        #print(time.time()-frameTimer)
        frameTimer = time.time()

    i+=1
    if i > 1000 and True:
        i=0
        VisualAudioPreview.ImageManager.fill_image((0,0,0))

        renderPoses = (set(positions))

        #print(len(renderPoses))

        ModularInterface.Core.DrawImage(IM = VisualAudioPreview.ImageManager,positions=renderPoses,color=(0,255,0))
        VisualAudioPreview.ImageManager.update_image()
        

        #print("test")
        
        VisualAudioPreview.update()
    

