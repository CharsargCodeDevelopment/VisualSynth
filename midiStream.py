import mido
import time


port_name = "loopMIDI Port 1"

print(mido.get_output_names())
print(mido.get_input_names())

inport = mido.open_input(port_name)


notes = []

def noteToFreq(note):
    a = 440 #frequency of A (coomon value is 440Hz)
    return (a / 32) * (2 ** ((note - 9) / 12))

def GetInputs(channel = -1):

    for msg in inport.iter_pending():
        if msg.type not in ["clock"]:
            if msg.channel == channel or channel == -1:
                if msg.type == "note_on" and msg.velocity != 0:
                    if msg.velocity != 0:
                        notes.append(msg.note)
                elif msg.type  == "note_off" or (msg.type == "note_on" and msg.velocity == 0) :
                    if msg.note in notes:
                        notes.remove(msg.note)
        #print(msg)
    #print(notes)


