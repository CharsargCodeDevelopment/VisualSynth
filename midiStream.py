import mido
import time
import threading


port_name = "loopMIDI Port 0"

print(mido.get_output_names())
print(mido.get_input_names())

inport = mido.open_input(port_name)

lock = threading.Lock() # A lock to ensure thread-safe access to the 'notes' list


notes = []

def Activate(channel = -1):
    midi_thread = threading.Thread(target=midi_input_thread, args=(inport, notes,channel))
    midi_thread.daemon = True # Set as daemon
    midi_thread.start()


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

def midi_input_thread(inport, notes, channel=-1):
    while True:
        for msg in inport.iter_pending():
            if msg.type not in ["clock"]:
                if msg.channel == channel or channel == -1:
                    if msg.type == "note_on" and msg.velocity != 0:
                        notes.append(msg.note)
                    elif msg.type == "note_off" or (msg.type == "note_on" and msg.velocity == 0):
                        if msg.note in notes:
                            notes.remove(msg.note)
        if len(notes) != 0:
            pass
            #print(notes)
        time.sleep(0.0005)  # Small sleep to prevent busy-waiting
