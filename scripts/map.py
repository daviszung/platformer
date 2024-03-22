# map should have a function that loads a file as a level
# a render method
import os, json
import pygame

class Map:
    def __init__(self, tile_size: int, tile_images: dict[str, pygame.Surface]):
        self.tile_size = tile_size
        self.tile_images = tile_images
        self.current_map: dict[str, dict[str, object]] = {
            "tilemap": {},
            "propmap": {},
            "spawnpoint": {},
        }

    def save_map(self):
        x = 1
        while 1:
            path = "maps/map" + str(x) + ".json"
            if os.path.exists(path):
                x += 1
            else:
                with open(path, "w+") as file:
                    json.dump(self.current_map, file)
                    break

    def load_level(self, map_name: str):
        path = "maps/" + map_name + ".json"
        if os.path.exists(path):
            with open(path) as file:
                self.current_map = json.load(file)

    def render_to_surf(self, surf: pygame.Surface, scroll: list[float]):
        for data in self.current_map["tilemap"]:
            d = self.current_map["tilemap"][data]
            surf.blit(self.tile_images[d["type"]], (d["pos"][0] * self.tile_size - scroll[0], d["pos"][1] * self.tile_size - scroll[1]))  # type: ignore