import sys, time
import pygame

from scripts.utils import load_image, load_images, draw_text, save_map
from scripts.editor_btn import Editor_Tile_Btn
from scripts.map import Map

class Editor:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("level editor")
        self.SCALING_FACTOR = 3
        self.BASE_TILE_SIZE = 16
        self.SCALED_TILE_SIZE = self.BASE_TILE_SIZE * self.SCALING_FACTOR
        self.SCREEN_SIZE = (1600, 960)
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.bg_size = (round(self.SCREEN_SIZE[0] / 6), round(self.SCREEN_SIZE[1] / 6))
        self.bg = pygame.Surface(self.bg_size)
        self.current_bg = pygame.Surface(self.SCREEN_SIZE)
        self.tileset = load_image("tileset.png")
        self.star_tileset = load_image("star_tileset.png")
        self.clock = pygame.time.Clock()
        self.last_time = time.time()
        self.font = pygame.Font("assets/fonts/monogram.ttf")
        self.fps_display = self.font.render("FPS", False, pygame.Color("white"))
        self.last_scroll_pos = [0, 0]
        self.scroll: list[float] = [0, 0]
        self.selected_tile: None | Editor_Tile_Btn = None
        self.bg_images = load_images("background", True)

        for i, img in enumerate(self.bg_images):
            self.bg_images[i] = pygame.transform.scale(img, self.bg_size)

        self.star_tile_images: dict[str, pygame.Surface] = {
            "t1": self.star_tileset.subsurface((0, 144, 16, 16)),
            "t2": self.star_tileset.subsurface((16, 144, 16, 16)),
            "t3": self.star_tileset.subsurface((32, 144, 16, 16)),
            "t4": self.star_tileset.subsurface((48, 144, 16, 16)),
            "t5": self.star_tileset.subsurface((64, 144, 16, 16)),
            "t6": self.star_tileset.subsurface((80, 144, 16, 16)),
            "t7": self.star_tileset.subsurface((96, 144, 16, 16)),
            "t8": self.star_tileset.subsurface((112, 144, 16, 16)),
            "t10": self.star_tileset.subsurface((128, 144, 16, 16)),
            "t11": self.star_tileset.subsurface((144, 144, 16, 16)),
            "t12": self.star_tileset.subsurface((160, 144, 16, 16)),
            "t13": self.star_tileset.subsurface((176, 144, 16, 16)),
            "t14": self.star_tileset.subsurface((192, 144, 16, 16)),
            "t15": self.star_tileset.subsurface((208, 144, 16, 16)),
            "t16": self.star_tileset.subsurface((224, 144, 16, 16)),
            "t17": self.star_tileset.subsurface((240, 144, 16, 16)),
            "t18": self.star_tileset.subsurface((256, 144, 16, 16)),
            "t19": self.star_tileset.subsurface((272, 144, 16, 16)),
            "t20": self.star_tileset.subsurface((0, 160, 16, 16)),
            "t21": self.star_tileset.subsurface((16, 160, 16, 16)),
            "t22": self.star_tileset.subsurface((32, 160, 16, 16)),
            "t23": self.star_tileset.subsurface((48, 160, 16, 16)),
            "t24": self.star_tileset.subsurface((64, 160, 16, 16)),
            "t25": self.star_tileset.subsurface((80, 160, 16, 16)),
            "t26": self.star_tileset.subsurface((96, 160, 16, 16)),
            "t27": self.star_tileset.subsurface((112, 160, 16, 16)),
            "t28": self.star_tileset.subsurface((128, 160, 16, 16)),
            "t29": self.star_tileset.subsurface((144, 160, 16, 16)),
        }

        self.prop_images: dict[str, pygame.Surface] = {}

        # scale up tiles
        for img in self.star_tile_images:
            self.star_tile_images[img] = pygame.transform.scale_by(
                self.star_tile_images[img], 3
            )

        self.map = Map(self.SCALED_TILE_SIZE, self.star_tile_images)

        self.img_list = list(self.star_tile_images)
        self.editor_tile_btns: list[Editor_Tile_Btn] = []

        for i in range(len(self.img_list)):
            img_x = 48 + (72 * (i // 12))
            img_y = i % 12 * 72 + 96
            self.editor_tile_btns.append(
                Editor_Tile_Btn(
                    [img_x, img_y],
                    self.star_tile_images[self.img_list[i]],
                    self.img_list[i],
                )
            )

        self.did_scroll: bool = True

        # first paint of bg
        self.current_bg = self.update_bg()
        self.map.render_to_surf(self.current_bg, self.scroll)

    def update_bg(self):
        tile1 = self.scroll[0] // (self.SCREEN_SIZE[0] * 4)
        tile2 = self.scroll[0] // (self.SCREEN_SIZE[0] * 2)
        tile3 = self.scroll[0] // self.SCREEN_SIZE[0]
        delta_scroll = (self.scroll[0] / 6) * 0.25 - (tile1 * self.bg_size[0])
        delta_scroll2 = (self.scroll[0] / 6) * 0.5 - (tile2 * self.bg_size[0])
        delta_scroll3 = (self.scroll[0] / 6) - (tile3 * self.bg_size[0])
        self.bg.blit(self.bg_images[0], (0 - (delta_scroll), 0 - self.scroll[1] * 0.15))
        self.bg.blit(
            self.bg_images[0],
            (self.bg_size[0] - (delta_scroll), 0 - self.scroll[1] * 0.15),
        )
        self.bg.blit(self.bg_images[1], (0 - (delta_scroll2), 0 - self.scroll[1] * 0.15))
        self.bg.blit(
            self.bg_images[1],
            (self.bg_size[0] - (delta_scroll2), 0 - self.scroll[1] * 0.15),
        )
        self.bg.blit(
            self.bg_images[2], (0 - (delta_scroll3), 0 - self.scroll[1] * 0.15)
        )
        self.bg.blit(
            self.bg_images[2],
            (self.bg_size[0] - (delta_scroll3), 0 - self.scroll[1] * 0.15),
        )
        return pygame.transform.scale_by(self.bg, 6)

    def run_main_loop(self):
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
                        self.current_bg = self.update_bg()
                        self.map.render_to_surf(self.current_bg, self.scroll)
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

            mx, my = pygame.mouse.get_pos()

            clicked_curr = pygame.mouse.get_pressed()
            left_click = clicked_curr[0]
            right_click = clicked_curr[2]

            # selecting tiles
            if mx <= 288 and left_click:
                for btn in self.editor_tile_btns:
                    rect = pygame.Rect(
                        btn.loc[0],
                        btn.loc[1],
                        btn.img.get_width(),
                        btn.img.get_height(),
                    )
                    if rect.collidepoint(mx, my):
                        self.selected_tile = btn

            if mx > 288 and left_click and self.selected_tile:
                tile_x, tile_y = int(
                    (mx + self.scroll[0]) // self.SCALED_TILE_SIZE
                ), int((my + self.scroll[1]) // self.SCALED_TILE_SIZE)
                self.map.current_map["tilemap"][f"{tile_x};{tile_y}"] = {
                    "type": self.selected_tile.name,
                    "pos": [tile_x, tile_y],
                }
                self.map.render_to_surf(self.current_bg, self.scroll)

            if mx > 288 and right_click:
                tile_x, tile_y = int(
                    (mx + self.scroll[0]) // self.SCALED_TILE_SIZE
                ), int((my + self.scroll[1]) // self.SCALED_TILE_SIZE)
                if f"{tile_x};{tile_y}" in self.map.current_map["tilemap"]:
                    del self.map.current_map["tilemap"][f"{tile_x};{tile_y}"]

            # RENDERING

            # rendering bg and map
            if self.did_scroll:
                self.current_bg = self.update_bg()
                self.map.render_to_surf(self.current_bg, self.scroll)
            self.screen.blit(self.current_bg, (0, 0))

            # render sidebar
            pygame.draw.rect(
                self.screen, pygame.Color(45, 43, 85), (0, 0, 288, self.SCREEN_SIZE[1])
            )
            pygame.draw.rect(
                self.screen, pygame.Color(45, 43, 85), (0, 0, self.SCREEN_SIZE[0], 48)
            )

            for btn in self.editor_tile_btns:
                btn.render(self.screen)

            draw_text(
                self.screen, f"{round(self.clock.get_fps())} FPS", [20, 20], self.font
            )

            draw_text(
                self.screen, f"mouse ({round(mx)}, {round(my)})", [120, 20], self.font
            )

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
                    self.screen.blit(t.img, (tile_x, tile_y))
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
