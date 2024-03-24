import sys, time
import pygame

from scripts.utils import load_images, draw_text, save_map
from scripts.editor_btn import Editor_Tile_Btn
from scripts.map import Map
from scripts.background import Bg
from scripts.asset_manager import Asset_Manager


class Editor:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("level editor")
        self.SCALING_FACTOR = 3
        self.BASE_TILE_SIZE = 16
        self.SCALED_TILE_SIZE = self.BASE_TILE_SIZE * self.SCALING_FACTOR
        self.SCREEN_SIZE = (1600, 960)
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.last_time = time.time()
        self.font = pygame.Font("assets/fonts/monogram.ttf")
        self.scroll: list[float] = [0, 0]
        self.selected_tile: None | Editor_Tile_Btn = None
        self.sidebar_mode: str = "tiles"
        self.sidebar_mode_toggle_btn = pygame.Rect(120, 56, 48, 20)
        self.rotation = 0

        self.am = Asset_Manager()

        self.bg = Bg(self.SCREEN_SIZE, load_images("background", True))

        self.map = Map(self.SCALED_TILE_SIZE, self.am.tiles, self.am.props)

        self.did_scroll: bool = True

        # first paint of bg
        self.bg.cache_bg(self.scroll)
        self.map.render_to_surf(self.bg.current_bg, self.scroll)

    def run_main_loop(self):

        clicked_prev = pygame.mouse.get_pressed()
        keys_prev = pygame.key.get_pressed()

        while 1:

            self.did_scroll = False

            t = time.time()
            dt = t - self.last_time
            dt *= 60
            self.last_time = t

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    return
                if e.type == pygame.KEYDOWN and pygame.key.get_mods() == 4097:
                    if e.dict["key"] == pygame.K_s:
                        save_map(self.map.current_map)
                        print("saved map")
                    if e.dict["key"] == pygame.K_l:
                        self.map.load_level("map1")
                        self.bg.cache_bg(self.scroll)
                        self.map.render_to_surf(self.bg.current_bg, self.scroll)
                        print("loaded map")

            keys = pygame.key.get_pressed()
            if keys[pygame.K_s] and self.scroll[0] > 0:
                self.scroll[0] -= 5 * dt
                self.did_scroll = True
            if keys[pygame.K_f]:
                self.scroll[0] += 5 * dt
                self.did_scroll = True
            if keys[pygame.K_e]:
                self.scroll[1] -= 5 * dt
                self.did_scroll = True
            if keys[pygame.K_d] and self.scroll[1] < 0:
                self.scroll[1] += 5 * dt
                self.did_scroll = True
            if keys[pygame.K_r] and not keys_prev[pygame.K_r]:
                if self.rotation >= 3:
                    self.rotation = 0
                else:
                    self.rotation += 1
            
            keys_prev = keys

            mx, my = pygame.mouse.get_pos()

            clicked_curr = pygame.mouse.get_pressed()
            left_click = clicked_curr[0]
            left_click_once = left_click and not clicked_prev[0]
            right_click = clicked_curr[2]
            clicked_prev = clicked_curr

            # selecting tiles/props
            if mx <= 288 and left_click:
                if self.sidebar_mode == "tiles":
                    for btn in self.am.editor_btns[f"tiles_r{self.rotation}"]:
                        rect = pygame.Rect(
                            btn.loc[0],
                            btn.loc[1],
                            btn.img.get_width(),
                            btn.img.get_height(),
                        )
                        if rect.collidepoint(mx, my):
                            self.selected_tile = btn

                elif self.sidebar_mode == "props":
                    for btn in self.am.editor_btns[f"prop_icons_r{self.rotation}"]:
                        rect = pygame.Rect(
                            btn.loc[0],
                            btn.loc[1],
                            btn.img.get_width(),
                            btn.img.get_height(),
                        )
                        if rect.collidepoint(mx, my):
                            self.selected_tile = btn

                if (
                    self.sidebar_mode_toggle_btn.collidepoint(mx, my)
                    and left_click_once
                ):
                    if self.sidebar_mode == "tiles":
                        self.sidebar_mode = "props"
                    elif self.sidebar_mode == "props":
                        self.sidebar_mode = "tiles"

            if mx > 288 and left_click and self.selected_tile:
                tile_x, tile_y = int(
                    (mx + self.scroll[0]) // self.SCALED_TILE_SIZE
                ), int((my + self.scroll[1]) // self.SCALED_TILE_SIZE)

                if self.sidebar_mode == "tiles":
                    self.map.current_map["tilemap"][f"{tile_x};{tile_y}"] = {
                        "type": self.selected_tile.name,
                        "pos": [tile_x, tile_y],
                        "rotation": self.rotation
                    }

                elif self.sidebar_mode == "props":
                    self.map.current_map["propmap"][f"{tile_x};{tile_y}"] = {
                        "type": self.selected_tile.name,
                        "pos": [tile_x, tile_y],
                        "rotation": self.rotation
                    }

                self.map.render_to_surf(self.bg.current_bg, self.scroll)

            if mx > 288 and right_click:
                should_refresh = False
                tile_x, tile_y = int(
                    (mx + self.scroll[0]) // self.SCALED_TILE_SIZE
                ), int((my + self.scroll[1]) // self.SCALED_TILE_SIZE)
                if self.sidebar_mode == "tiles":
                    if f"{tile_x};{tile_y}" in self.map.current_map["tilemap"]:
                        del self.map.current_map["tilemap"][f"{tile_x};{tile_y}"]
                    should_refresh = True
                elif self.sidebar_mode == "props":
                    if f"{tile_x};{tile_y}" in self.map.current_map["propmap"]:
                        del self.map.current_map["propmap"][f"{tile_x};{tile_y}"]
                    should_refresh = True
                if should_refresh:
                    self.bg.cache_bg(self.scroll)
                    self.map.render_to_surf(self.bg.current_bg, self.scroll)


            # RENDERING

            # rendering bg and map
            if self.did_scroll:
                self.bg.cache_bg(self.scroll)
                self.map.render_to_surf(self.bg.current_bg, self.scroll)
            self.screen.blit(self.bg.current_bg, (0, 0))

            # render sidebar
            pygame.draw.rect(
                self.screen, pygame.Color(45, 43, 85), (0, 0, 288, self.SCREEN_SIZE[1])
            )
            pygame.draw.rect(
                self.screen, pygame.Color(45, 43, 85), (0, 0, self.SCREEN_SIZE[0], 48)
            )

            pygame.draw.rect(
                self.screen, pygame.Color(80, 43, 85), self.sidebar_mode_toggle_btn
            )

            if self.sidebar_mode == "tiles":
                for btn in self.am.editor_btns[f"{self.sidebar_mode}_r{self.rotation}"]:
                    btn.render(self.screen)
            elif self.sidebar_mode == "props":
                for btn in self.am.editor_btns[f"prop_icons_r{self.rotation}"]:
                    btn.render(self.screen)

            draw_text(
                self.screen, f"{round(self.clock.get_fps())} FPS", [20, 20], self.font
            )

            draw_text(
                self.screen, f"mouse ({round(mx)}, {round(my)})", [120, 20], self.font
            )

            draw_text(self.screen, f"{self.sidebar_mode}", [124, 56], self.font)

            draw_text(
                self.screen,
                f"tile ({(mx + self.scroll[0]) // self.SCALED_TILE_SIZE}, {(my + self.scroll[1]) // self.SCALED_TILE_SIZE})",
                [280, 20],
                self.font,
            )

            draw_text(
                self.screen,
                f"scroll: {round(self.scroll[0]), round(self.scroll[1])}",
                [460, 20],
                self.font,
            )

            if mx > 288 and my > 48:
                t = self.selected_tile
                tile_x = int((mx // self.SCALED_TILE_SIZE) * self.SCALED_TILE_SIZE)
                tile_y = int((my // self.SCALED_TILE_SIZE) * self.SCALED_TILE_SIZE)
                if t:
                    if self.sidebar_mode == "tiles":
                        self.screen.blit(self.am.tiles[f"r{self.rotation}"][t.name], (tile_x, tile_y))
                    elif self.sidebar_mode == "props":
                        self.screen.blit(self.am.props[f"r{self.rotation}"][t.name], (tile_x, tile_y))
                else:
                    pygame.draw.rect(
                        self.screen,
                        "lightblue",
                        (
                            tile_x,
                            tile_y,
                            self.SCALED_TILE_SIZE,
                            self.SCALED_TILE_SIZE,
                        ),
                    )

            pygame.display.update()
            self.clock.tick()


editor = Editor()
editor.run_main_loop()
sys.exit()
