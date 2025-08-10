import mido
import time


port_name = "loopMIDI Port 2"

print(mido.get_output_names())
print(mido.get_input_names())


port = mido.open_output(port_name)

midi_files = []
midi_file = 'Murder Drones Ost.mid'
midi_files.append(midi_file)
midi_file = "Murder Drones - Forever Extended.mid"
midi_files.append(midi_file)
midi_file = "Eternal_Dream_MD_Piano.mid"
midi_files.append(midi_file)


midi_files.pop(0)
midi_files.pop(-1)
for midi_file in midi_files:
    mid = mido.MidiFile(midi_file)
    for msg in mid.play():
        if msg.channel == 1 or True:
            print(msg)
            port.send(msg)
