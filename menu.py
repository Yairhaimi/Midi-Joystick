from display_handling import Display
from sprite import Sprite

class Menu:
    def __init__(self, display: Display, sprites: list[Sprite]):
        self.display = display
        self.sprites = sprites
    
    def overview_page(self, title_text="bababooie"):
        self.display.draw_title(title_text)

        for (sprite, (x, y)) in zip(self.sprites, [ (0, 15), (0, 35), (50, 25), ]):
            self.display.draw_sprite(sprite.path, x, y)
    
    def select(self, sprite_index: int):
        pass
        