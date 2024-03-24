import pygame
from scripts.editor_btn import Editor_Tile_Btn

class Asset_Manager():
    def __init__(self):
        self.tileset = pygame.image.load("./assets/images/star_tileset.png").convert_alpha()
        self.base_tiles: dict[str, pygame.Surface] = {
            "t1": self.tileset.subsurface((0, 144, 16, 16)),
            "t2": self.tileset.subsurface((16, 144, 16, 16)),
            "t3": self.tileset.subsurface((32, 144, 16, 16)),
            "t4": self.tileset.subsurface((48, 144, 16, 16)),
            "t5": self.tileset.subsurface((64, 144, 16, 16)),
            "t6": self.tileset.subsurface((80, 144, 16, 16)),
            "t7": self.tileset.subsurface((96, 144, 16, 16)),
            "t8": self.tileset.subsurface((112, 144, 16, 16)),
            "t10": self.tileset.subsurface((128, 144, 16, 16)),
            "t11": self.tileset.subsurface((144, 144, 16, 16)),
            "t12": self.tileset.subsurface((160, 144, 16, 16)),
            "t13": self.tileset.subsurface((176, 144, 16, 16)),
            "t14": self.tileset.subsurface((192, 144, 16, 16)),
            "t15": self.tileset.subsurface((208, 144, 16, 16)),
            "t16": self.tileset.subsurface((224, 144, 16, 16)),
            "t17": self.tileset.subsurface((240, 144, 16, 16)),
            "t18": self.tileset.subsurface((256, 144, 16, 16)),
            "t19": self.tileset.subsurface((272, 144, 16, 16)),
            "t20": self.tileset.subsurface((0, 160, 16, 16)),
            "t21": self.tileset.subsurface((16, 160, 16, 16)),
            "t22": self.tileset.subsurface((32, 160, 16, 16)),
            "t23": self.tileset.subsurface((48, 160, 16, 16)),
            "t24": self.tileset.subsurface((64, 160, 16, 16)),
            "t25": self.tileset.subsurface((80, 160, 16, 16)),
            "t26": self.tileset.subsurface((96, 160, 16, 16)),
            "t27": self.tileset.subsurface((112, 160, 16, 16)),
            "t28": self.tileset.subsurface((128, 160, 16, 16)),
            "t29": self.tileset.subsurface((144, 160, 16, 16)),
        }

        self.prop_images: dict[str, pygame.Surface] = {
            "small_tree": self.tileset.subsurface((0, 80, 64, 64)),
            "big_tree": self.tileset.subsurface((160, 0, 128, 144)),
            "hanging_star1": self.tileset.subsurface((16, 32, 16, 16)),
            "hanging_star2": self.tileset.subsurface((0, 32, 16, 32)),
            "hanging_star3": self.tileset.subsurface((32, 32, 16, 48)),
            "hanging_grass": self.tileset.subsurface((16, 48, 16, 16)),
            "flower1": self.tileset.subsurface((16, 64, 16, 16)),
            "flower2": self.tileset.subsurface((0, 64, 16, 16)),
            "flower3": self.tileset.subsurface((144, 112, 16, 16)),
            "flower4": self.tileset.subsurface((144, 128, 16, 16)),
            "flower5": self.tileset.subsurface((64, 80, 16, 16)),
            "bush_long": self.tileset.subsurface((64, 112, 80, 32)),
            "bush_short": self.tileset.subsurface((112, 80, 48, 32)),
            "grass1": self.tileset.subsurface((64, 96, 16, 16)),
            "grass2": self.tileset.subsurface((80, 96, 16, 16)),
            "grass3": self.tileset.subsurface((96, 96, 16, 16)),
            "rock": self.tileset.subsurface((48, 48, 32, 32)),
            "side_vine1": self.tileset.subsurface((80, 80, 16, 16)),
            "side_vine2": self.tileset.subsurface((96, 80, 16, 16)),
        }

        self.prop_image_icons: dict[str, pygame.Surface] = {
            "small_tree": self.prop_images["small_tree"].subsurface((16, 32, 16, 16)),
            "big_tree": self.prop_images["big_tree"].subsurface((80, 32, 16, 16)),
            "hanging_star1": self.prop_images["hanging_star1"].subsurface((0, 0, 16, 16)),
            "hanging_star2": self.prop_images["hanging_star2"].subsurface((0, 0, 16, 16)),
            "hanging_star3": self.prop_images["hanging_star3"].subsurface((0, 0, 16, 16)),
            "hanging_grass": self.prop_images["hanging_grass"].subsurface((0, 0, 16, 16)),
            "flower1": self.prop_images["flower1"].subsurface((0, 0, 16, 16)),
            "flower2": self.prop_images["flower2"].subsurface((0, 0, 16, 16)),
            "flower3": self.prop_images["flower3"].subsurface((0, 0, 16, 16)),
            "flower4": self.prop_images["flower4"].subsurface((0, 0, 16, 16)),
            "flower5": self.prop_images["flower5"].subsurface((0, 0, 16, 16)),
            "bush_long": self.prop_images["bush_long"].subsurface((32, 16, 16, 16)),
            "bush_short": self.prop_images["bush_short"].subsurface((16, 16, 16, 16)),
            "grass1": self.prop_images["grass1"].subsurface((0, 0, 16, 16)),
            "grass2": self.prop_images["grass2"].subsurface((0, 0, 16, 16)),
            "grass3": self.prop_images["grass3"].subsurface((0, 0, 16, 16)),
            "rock": self.prop_images["rock"].subsurface((0, 16, 16, 16)),
            "side_vine1": self.prop_images["side_vine1"].subsurface((0, 0, 16, 16)),
            "side_vine2": self.prop_images["side_vine2"].subsurface((0, 0, 16, 16)),
        }

        # scale up tiles
        for img in self.base_tiles:
            self.base_tiles[img] = pygame.transform.scale_by(
                self.base_tiles[img], 3
            )

        # scale up props
        for img in self.prop_images:
            self.prop_images[img] = pygame.transform.scale_by(self.prop_images[img], 3)

        # scale up prop image icons
        for img in self.prop_image_icons:
            self.prop_image_icons[img] = pygame.transform.scale_by(
                self.prop_image_icons[img], 3
            )
        
        self.tiles = self.produce_rotated_image_sets(self.base_tiles)
        self.props = self.produce_rotated_image_sets(self.prop_images)
        self.prop_icons = self.produce_rotated_image_sets(self.prop_image_icons)
        self.editor_btns: dict[str, list[Editor_Tile_Btn]] = {
            "tiles_r0": self.produce_editor_btns(self.tiles, 0),
            "tiles_r1": self.produce_editor_btns(self.tiles, 1),
            "tiles_r2": self.produce_editor_btns(self.tiles, 2),
            "tiles_r3": self.produce_editor_btns(self.tiles, 3),
            "prop_icons_r0": self.produce_editor_btns(self.prop_icons, 0),
            "prop_icons_r1": self.produce_editor_btns(self.prop_icons, 1),
            "prop_icons_r2": self.produce_editor_btns(self.prop_icons, 2),
            "prop_icons_r3": self.produce_editor_btns(self.prop_icons, 3),
        }

    def produce_rotated_image_sets(self, original: dict[str, pygame.Surface]) -> dict[str, dict[str, pygame.Surface]]:
        output: dict[str, dict[str, pygame.Surface]] = {}
        copy1 = original.copy()
        copy2 = original.copy()
        copy3 = original.copy()

        for img in copy1:
            # copy1[img] = pygame.transform.flip(copy1[img], False, True)
            copy1[img] = pygame.transform.rotate(copy1[img], 90)
        for img in copy2:
            # copy2[img] = pygame.transform.flip(copy2[img], True, True)
            copy2[img] = pygame.transform.rotate(copy2[img], 180)
        for img in copy3:
            # copy3[img] = pygame.transform.flip(copy3[img], True, False)
            copy3[img] = pygame.transform.rotate(copy3[img], 270)
        
        output["r0"] = original
        output["r1"] = copy1
        output["r2"] = copy2
        output["r3"] = copy3
        
        return output

    def produce_editor_btns(self, original: dict[str, dict[str, pygame.Surface]], rotation: int):
        img_list = list(original[f"r{rotation}"])
        output: list[Editor_Tile_Btn] = []

        for i in range(len(img_list)):
            img_x = 48 + (72 * (i // 12))
            img_y = i % 12 * 72 + 96
            output.append(
                Editor_Tile_Btn([img_x, img_y], original[f"r{rotation}"][img_list[i]], img_list[i])
            )

        return output
