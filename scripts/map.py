# map should have a function that loads a file as a level
# a render method

class Map:
    def __init__(self, tile_size: int = 16):
        self.tile_size = tile_size
        self.current_map = {}
        self.props = {}


        pass

    def load_level(self, path: str):

        pass

    def render(self, scroll_offset: list[float]):
        pass
