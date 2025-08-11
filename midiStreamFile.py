import mido
import time

midi_files = []
midi_file = 'Murder Drones Ost.mid'
midi_files.append(midi_file)
midi_file = "Murder Drones - Forever Extended.mid"
midi_files.append(midi_file)
midi_file = "Eternal_Dream_MD_Piano.mid"
midi_files.append(midi_file)

port = mido.open_output('loopMIDI Port 1')


midiFile =mido.MidiFile(midi_files[0])
print(midiFile.ticks_per_beat)
print(dir(midiFile))
tpb =midiFile.ticks_per_beat
tempo = 0

t = 0

data = {}
notes = {}
length = 0
for msg in mido.MidiFile(midi_files[0]):
    if msg.type in ["note_on","note_off"]:
        
        if not msg.is_meta:
            #tick2second
            t+= msg.time
            length += msg.time
            if t not in data:
                data[t] = {"notes":[]}

            if msg.type == "note_on":
                
                notes[msg.note] = msg.velocity
            if msg.type == "note_off":
                notes[msg.note] = msg.velocity
                del notes[msg.note]
            for note in list(notes):
                if notes[note] == 0:
                    del notes[note]
            data[t]["notes"] = notes.copy()
            print(notes)
            delay = (mido.tick2second(msg.time,tpb,tempo))
            #time.sleep(msg.time)

            #port.send(msg)
            #print(msg)
    else:
        if msg.type == "set_tempo":
            tempo = msg.tempo
for item in data:
    print(f"{item}:{data[item]}")



progress = [0]

def Snap(x,v=1):
    return round(x/v)*v


def GetInputs(T):
    startTime = time.time()
    if T in data:
        #print(time.time()-startTime)
        return data[T]
    values = {"notes":[]}
    #print(T)
    if Snap(T,0.2) != Snap(progress[0],0.2):
        progress[0] = T
        print(f"{progress[0]}/{int(length)}")
    index = list(data)[0]
    for item in list(data):
        
        if item < T:
            index = item
        if item > T:
            #print(time.time()-startTime)
            values = data[index]
            return values
            
    
    values = data[index]
    #print(time.time()-startTime)
        
    return None


