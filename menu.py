from display_handling import Display
from sprite import Sprite

class Menu:
    class Page:
        def __init__(self, name: str, sprites: dict[str, (Sprite, int)]):
            self.name = name
            self.sprites = sprites
        
        def total_sprites(self):
            sprites = [ s[0] for s in self.sprites.values() ]
            
            return sum([ len(s.variations_paths) + 1 for s in sprites ])
        
        @staticmethod
        def overview_page():
            return Menu.Page(
                name="overview", 
                sprites={
                    "A_button": ( 
                        Sprite(
                            "\sprites\A_button.bmp", 
                            variations=[
                                Sprite("\sprites\A_button_inverted.bmp", variations=[], parent_sprite="A_button")
                            ],
                        ), 
                        (0,15) 
                    ),
                    "B_button": ( 
                        Sprite(
                            "\sprites\B_button.bmp", 
                            variations=[
                                Sprite("\sprites\B_button_inverted.bmp", variations=[], parent_sprite="B_button")
                            ],
                        ), 
                        (0, 35) 
                    ),
                    "dpad": ( 
                        Sprite(
                            "\sprites\dpad.bmp", 
                            variations=[
                                Sprite("\sprites\dpad_left.bmp", variations=[], parent_sprite="dpad"),
                                Sprite("\sprites\dpad_right.bmp", variations=[], parent_sprite="dpad"),
                                Sprite("\sprites\dpad_up.bmp", variations=[], parent_sprite="dpad"),
                                Sprite("\sprites\dpad_down.bmp", variations=[], parent_sprite="dpad"),
                            ]
                        ), 
                        (50,25)
                    ),
                }
            )
    
    def __init__(self, display: Display, current_page: str):        
        self.display = display
        self.pages = {
            "overview": self.Page.overview_page(),
        }
        self.current_page = current_page
        self.draw_page(current_page)
    
    def draw_page(self, page_name: str, title_text="bababooie"):
        self.display.draw_title(title_text)

        page = self.pages[page_name]
        
        for (sprite, (x, y)) in page.sprites.values():
            self.display.draw_sprite(sprite.path, x, y)
    
    def highlight(self, encoder_value: int):
        children_sprites = [ 
            parent_sprite[0].variations
                for parent_sprite 
                in list(self.pages[self.current_page].sprites.values())
        ]
        
        children_sprites = [ x for xs in children_sprites for x in xs]        
        child_sprite = children_sprites[encoder_value % len(children_sprites)]
        (x, y) = self.pages[self.current_page].sprites[child_sprite.parent_sprite][1]

        self.draw_page(self.current_page)
        self.display.draw_sprite(child_sprite.path, x, y)
        