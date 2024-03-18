import sys, time
import pygame

from scripts.utils import load_image, draw_text


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
        self.selected_tile = None
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
        }

        for img in self.tile_images:
            self.tile_images[img] = pygame.transform.scale_by(
                self.tile_images[img], self.SCALING_FACTOR
            )

        self.img_list = list(self.tile_images)
        self.prop_images: dict[str, pygame.Surface] = {}

    def run_main_loop(self):
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

            # RENDERING
            self.screen.fill("black")

            pygame.draw.rect(self.screen, pygame.Color(45, 43, 85), (0, 0, 288, self.SCREEN_SIZE[1]))
            pygame.draw.rect(self.screen, pygame.Color(45, 43, 85), (0, 0, self.SCREEN_SIZE[0], 48))

            # render sidebar
            for i in range(len(self.img_list)):
                img_x = 48
                img_y = i * 72 + 96
                if img_y > self.SCREEN_SIZE[1] - 72:
                    img_x += 72
                    img_y = len(self.img_list) % i + 96
                self.screen.blit(self.tile_images[self.img_list[i]], (img_x, img_y))
                
            # self.screen.blit(self.tile_images["grass_left"], (100, 30))
            # self.screen.blit(self.tile_images["grass_middle"], (100, 50))
            # self.screen.blit(self.tile_images["grass_right"], (100, 70))
            # self.screen.blit(self.tile_images["stone_left"], (100, 90))
            # self.screen.blit(self.tile_images["stone_middle"], (100, 110))
            # self.screen.blit(self.tile_images["stone_right"], (100, 130))
            # self.screen.blit(self.tile_images["dirt_left"], (100, 150))
            # self.screen.blit(self.tile_images["dirt_middle"], (100, 170))
            # self.screen.blit(self.tile_images["dirt_right"], (100, 190))
            # self.screen.blit(self.tile_images["dirt_left_low"], (100, 210))
            # self.screen.blit(self.tile_images["dirt_middle_low"], (100, 230))
            # self.screen.blit(self.tile_images["dirt_right_low"], (100, 250))

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
                pygame.draw.rect(
                    self.screen,
                    "lightblue",
                    (
                        (mx // self.SCALED_TILE_SIZE) * self.SCALED_TILE_SIZE,
                        (my // self.SCALED_TILE_SIZE) * self.SCALED_TILE_SIZE,
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
