import sys, time
import pygame

from scripts.utils import load_image, draw_text
from scripts.editor_btn import Editor_Tile_Btn


class Editor:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("level editor")
        self.SCALING_FACTOR = 3
        self.BASE_TILE_SIZE = 16
        self.SCALED_TILE_SIZE = self.BASE_TILE_SIZE * self.SCALING_FACTOR
        self.SCREEN_SIZE = (1600, 900)
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.tileset = load_image("tileset.png")
        self.clock = pygame.time.Clock()
        self.game_state: str = "game"
        self.last_time = time.time()
        self.font = pygame.Font("assets/fonts/monogram.ttf")
        self.fps_display = self.font.render(
            "FPS", antialias=False, color=pygame.Color("white")
        )
        self.scroll = [0, 0]
        self.selected_tile: None | Editor_Tile_Btn = None
        self.tile_images: dict[str, pygame.Surface] = {
            "grass_left": self.tileset.subsurface((16, 16, 16, 16)),
            "grass_middle": self.tileset.subsurface((48, 16, 16, 16)),
            "grass_right": self.tileset.subsurface((80, 16, 16, 16)),
            "dirt_left": self.tileset.subsurface((16, 48, 16, 16)),
            "dirt_middle": self.tileset.subsurface((48, 48, 16, 16)),
            "dirt_right": self.tileset.subsurface((80, 48, 16, 16)),
            "dirt_left_low": self.tileset.subsurface((16, 80, 16, 16)),
            "dirt_middle_low": self.tileset.subsurface((48, 80, 16, 16)),
            "dirt_right_low": self.tileset.subsurface((80, 80, 16, 16)),
            "stone_left": self.tileset.subsurface((240, 112, 16, 16)),
            "stone_middle": self.tileset.subsurface((272, 112, 16, 16)),
            "stone_right": self.tileset.subsurface((304, 112, 16, 16)),
            "glyph": self.tileset.subsurface((16, 320, 16, 16)),
        }

        for img in self.tile_images:
            self.tile_images[img] = pygame.transform.scale_by(
                self.tile_images[img], self.SCALING_FACTOR
            )

        self.img_list = list(self.tile_images)

        self.editor_tile_btns: list[Editor_Tile_Btn] = []

        for i in range(len(self.img_list)):
            img_x = 48
            img_y = i * 72 + 96
            if img_y > self.SCREEN_SIZE[1] - 72:
                img_x += 72
                img_y = len(self.img_list) % i * 72 + 24
            self.editor_tile_btns.append(Editor_Tile_Btn([img_x, img_y], self.tile_images[self.img_list[i]], self.img_list[i]))

        self.prop_images: dict[str, pygame.Surface] = {}

    def run_main_loop(self):

        clicked_prev = pygame.mouse.get_pressed()

        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    return

            t = time.time()
            dt = t - self.last_time
            dt *= 60
            self.last_time = t

            mx, my = pygame.mouse.get_pos()

            clicked_curr = pygame.mouse.get_pressed()
            left_click = clicked_curr[0] and not clicked_prev[0]
            clicked_prev = clicked_curr

            # RENDERING
            self.screen.fill("black")

            pygame.draw.rect(
                self.screen, pygame.Color(45, 43, 85), (0, 0, 288, self.SCREEN_SIZE[1])
            )
            pygame.draw.rect(
                self.screen, pygame.Color(45, 43, 85), (0, 0, self.SCREEN_SIZE[0], 48)
            )

            # render sidebar
            for btn in self.editor_tile_btns:
                btn.render(self.screen)
            

            if mx <= 288 and left_click:
                for btn in self.editor_tile_btns:
                    rect = pygame.Rect(btn.loc[0], btn.loc[1], btn.img.get_width(), btn.img.get_height())
                    if rect.collidepoint(mx, my):
                        self.selected_tile = btn

            self.screen.blit(self.tileset, (500, 500))

            draw_text(
                self.screen, f"{round(self.clock.get_fps())} FPS", [20, 20], self.font
            )

            draw_text(self.screen, f"mouse ({mx}, {my})", [120, 20], self.font)

            draw_text(
                self.screen,
                f"tile ({mx // self.SCALED_TILE_SIZE}, {my // self.SCALED_TILE_SIZE})",
                [280, 20],
                self.font,
            )

            if mx > 288 and my > 48:
                t = self.selected_tile
                tile_x = (mx // self.SCALED_TILE_SIZE) * self.SCALED_TILE_SIZE
                tile_y = (my // self.SCALED_TILE_SIZE) * self.SCALED_TILE_SIZE
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

            self.screen.blit(self.screen, (0, 0))

            pygame.display.update()
            self.clock.tick()


editor = Editor()
editor.run_main_loop()
sys.exit()
