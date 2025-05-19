import rotaryio
import digitalio

class Encoder:
    def __init__(self, enc_pins, button_pin):
        self.enc_pins = enc_pins
        self.button_pin = button_pin
        self.has_button = self.button_pin != None
        self.encoder = rotaryio.IncrementalEncoder(*enc_pins)
        self.last_position = None
        self.position = None
        
        button = digitalio.DigitalInOut(button_pin)
        button.direction = digitalio.Direction.INPUT
        button.pull = digitalio.Pull.UP
        self.button = button

        self.update()

    def update(self):
        position = self.encoder.position
        
        if self.last_position is None or position != self.last_position:
            self.last_position = position
            self.position = self.encoder.position