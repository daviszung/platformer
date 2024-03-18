import os
import pygame

BASE_IMG_PATH = "assets/images/"


def load_image(path: str):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img


def load_images(dir_name: str):
    images: list[pygame.Surface] = []
    for img in sorted(os.listdir(BASE_IMG_PATH + dir_name)):
        images.append(load_image(f"{dir_name}/{img}"))
    return images


def draw_text(
    surf: pygame.Surface,
    text: str,
    loc: list[int],
    font: pygame.Font,
    color: pygame.Color = pygame.Color("white"),
):
    img = font.render(text, False, color)
    surf.blit(img, loc)
