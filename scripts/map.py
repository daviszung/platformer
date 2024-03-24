import os, json
import pygame

class Map:
    def __init__(self, tile_size: int, tiles: dict[str, dict[str, pygame.Surface]], props: dict[str, dict[str, pygame.Surface]]):
        self.tile_size = tile_size
        self.tiles = tiles
        self.props = props
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
        print(self.current_map)
        for data in self.current_map["tilemap"]:
            t = self.current_map["tilemap"][data]
            surf.blit(self.tiles[f"r{t['rotation']}"][t["type"]], (t["pos"][0] * self.tile_size - scroll[0], t["pos"][1] * self.tile_size - scroll[1]))  # type: ignore

        for data in self.current_map["propmap"]:
            p = self.current_map["propmap"][data]
            surf.blit(self.props[f"r{p['rotation']}"][p["type"]], (p["pos"][0] * self.tile_size - scroll[0], p["pos"][1] * self.tile_size - scroll[1]))  # type: ignore
