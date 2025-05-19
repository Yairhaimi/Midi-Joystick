class Sprite:
    def __init__(self, path: str, variations_paths: list[str] | None):
        self.path = path
        self.variations_paths = variations_paths