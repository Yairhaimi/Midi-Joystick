# YD-RP2040: VREF should be connected to 3V3!!!!!!!!!!!
# Potentiometers connected to GP26
#
#

import time, usb_midi, adafruit_midi, board

from adafruit_simplemath import map_range

from analogio import AnalogIn
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.pitch_bend import PitchBend
from adafruit_midi.control_change import ControlChange

from display_handling import display


oled = display(board.GP15, board.GP14, 128, 64, device_address=0x3C)

while(True):
    pass

# pot_1 = AnalogIn(board.GP26)
# pot_2 = AnalogIn(board.GP27)


# midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

# print("Default output MIDI channel:", midi.out_channel + 1)

# PB_VALUE_RANGE = 16384

# def pb_value(pot_value):
#     return min(int(pot_value * (PB_VALUE_RANGE / 65535)), PB_VALUE_RANGE - 1)

# while True:
    # midi.send(PitchBend(pb_value(pot_1.value)))
    # midi.send(ControlChange(control=1, value=int(map_range(pot_2.value, 0, 65536, 0, 127))))
    # time.sleep(0.1)
