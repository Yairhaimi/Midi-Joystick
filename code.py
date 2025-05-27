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

from display_handling import Display
from rotary_encoder import Encoder
from menu import Menu
from sprite import Sprite

sprites = [
    Sprite("\sprites\A_button.bmp", variations_paths="\sprites\A_button_inverted"),
    Sprite("\sprites\B_button.bmp", variations_paths="\sprites\B_button_inverted"),
    Sprite("\sprites\dpad.bmp", variations_paths=["\sprites\dpad_left.bmp", "\sprites\dpad_right.bmp", "\sprites\dpad_up.bmp", "\sprites\dpad_down.bmp", ])
]

oled_display = Display(board.GP15, board.GP14, 128, 64, device_address=0x3C)
encoder = Encoder([board.GP2, board.GP3], board.GP29)
menu = Menu(oled_display, sprites)

menu.overview_page()

while(True):
    # encoder.update()
    # print(f"encoder value: {encoder.position}, encoder button: {not encoder.button.value}")
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
