import pygame

class Bg:
    def __init__(self, screen_size: tuple[int, int], bg_images: list[pygame.Surface]):
        self.screen_size = screen_size
        self.bg_size = (round(screen_size[0] / 6), round(screen_size[1] / 6))
        self.bg = pygame.Surface(self.bg_size)
        self.bg_images = bg_images
        self.current_bg = pygame.Surface(screen_size)

        for i, img in enumerate(self.bg_images):
            self.bg_images[i] = pygame.transform.scale(img, self.bg_size)

    def cache_bg(self, scroll: list[float]):
        tile1 = scroll[0] // (self.screen_size[0] * 4)
        tile2 = scroll[0] // (self.screen_size[0] * 2)
        tile3 = scroll[0] // self.screen_size[0]
        delta_scroll = (scroll[0] / 6) * 0.25 - (tile1 * self.bg_size[0])
        delta_scroll2 = (scroll[0] / 6) * 0.5 - (tile2 * self.bg_size[0])
        delta_scroll3 = (scroll[0] / 6) - (tile3 * self.bg_size[0])
        self.bg.blit(self.bg_images[0], (0 - (delta_scroll), 0 - scroll[1] * 0.15))
        self.bg.blit(
            self.bg_images[0],
            (self.bg_size[0] - (delta_scroll), 0 - scroll[1] * 0.15),
        )
        self.bg.blit(self.bg_images[1], (0 - (delta_scroll2), 0 - scroll[1] * 0.15))
        self.bg.blit(
            self.bg_images[1],
            (self.bg_size[0] - (delta_scroll2), 0 - scroll[1] * 0.15),
        )
        self.bg.blit(
            self.bg_images[2], (0 - (delta_scroll3), 0 - scroll[1] * 0.15)
        )
        self.bg.blit(
            self.bg_images[2],
            (self.bg_size[0] - (delta_scroll3), 0 - scroll[1] * 0.15),
        )
        self.current_bg = pygame.transform.scale_by(self.bg, 6)
