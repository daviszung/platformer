import pygame

class Editor_Tile_Btn():
    def __init__(self, loc: list[float], img: pygame.Surface, name: str):
        self.loc = loc 
        self.img = img
        self.name = name

    def render(self, surf: pygame.Surface):
        surf.blit(self.img, self.loc)

