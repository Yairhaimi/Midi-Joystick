class Sprite:
    def __init__(self, path: str, variations: list | None, parent_sprite=None):
        self.path = path
        self.variations = variations
        self.parent_sprite = parent_sprite