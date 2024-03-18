import sys, time
import pygame


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("platformer")
        self.screen = pygame.display.set_mode((1600, 900))
        self.clock = pygame.time.Clock()
        self.game_state: str = "game"
        self.last_time = time.time()
        self.font = pygame.Font()
        self.fps_display = self.font.render(
            "FPS", antialias=False, color=pygame.Color("white")
        )

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

            # RENDERING
            self.screen.fill("black")

            fps_display = self.font.render(f"{round(self.clock.get_fps())} FPS", False, "white")

            self.screen.blit(fps_display, (20, 20))

            pygame.display.update()
            self.clock.tick()

game = Game()
game.run_main_loop()
sys.exit()