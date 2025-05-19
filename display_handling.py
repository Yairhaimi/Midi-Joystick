import board, busio, displayio, adafruit_displayio_ssd1306, terminalio

from adafruit_display_text import label
from i2cdisplaybus import I2CDisplayBus

class Display:
    def __init__(self, scl_pin, sda_pin, width, height, device_address=0x3C):
        self.scl_pin = scl_pin
        self.sda_pin = sda_pin
        self.device_address = device_address
        self.width = width
        self.height = height
        
        displayio.release_displays()
        self.i2c = busio.I2C(board.GP15, board.GP14)
        self.display_bus = I2CDisplayBus(self.i2c, device_address=self.device_address)
        self.display = adafruit_displayio_ssd1306.SSD1306(self.display_bus, width=width, height=height)
        
        self.bitmap = displayio.Bitmap(width, height, 2)
        self.color_palette = displayio.Palette(2)
        self.color_palette[0] = 0x000000 # black
        self.color_palette[1] = 0xFFFFFF # white
        
        self.display.root_group = displayio.Group()
        
        self.overview_page()
    
    def draw_sprite(self, sprite_path, x, y):
        sprite = displayio.TileGrid(
            displayio.OnDiskBitmap(sprite_path), 
            pixel_shader=self.color_palette, 
            x=x, 
            y=y
        )
        
        self.display.root_group.append(sprite)
    
    def draw_title(self, text):
        title = label.Label(
            terminalio.FONT, 
            text=text, 
            color=0xFFFFFF, 
            x=0, 
            y=0, 
            anchor_point=(0,0)
        )
        
        self.display.root_group.append(title)
    
    def overview_page(self):
        self.draw_title("title bababooie")

        for (sprite_path, (x, y)) in [
            ('./sprites/dpad_up.bmp', (50, 25)),
            ('./sprites/A_button.bmp', (0, 15)),
            ('./sprites/B_button.bmp', (0, 35)),
        ]:
            self.draw_sprite(sprite_path, x, y)
        
        
        
        
        
        


        
        

# displayio.release_displays()
# i2c = busio.I2C(board.GP15, board.GP14)
# display_bus = I2CDisplayBus(i2c, device_address=0x3C)
# display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Make the display context
# splash = displayio.Group()
# display.root_group = splash

# color_bitmap = displayio.Bitmap(128, 64, 1)
# color_palette = displayio.Palette(1)
# color_palette[0] = 0xFFFFFF  # White

# bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
# splash.append(bg_sprite)

# # Draw a smaller inner rectangle
# inner_bitmap = displayio.Bitmap(118, 54, 1)
# inner_palette = displayio.Palette(1)
# inner_palette[0] = 0x000000  # Black
# inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=5)
# splash.append(inner_sprite)

# # Draw a label
# text = "Hello World!"
# text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=28)
# splash.append(text_area)

# while True:
#     pass
