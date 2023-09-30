from typing import Any, Self
import arcade
from arcade import Sprite
from arcade.types import PathOrTexture

from const import *

class Wall(Sprite):
    pass

class Dest(Sprite):
    pass

class Source(Sprite):
    pass

class Map():
    def __init__(self, path:str) -> None:
        load_map = arcade.tilemap.TileMap(
            path,
            scaling = SPRITE_SCALING,
            layer_options = {
                "wall": {
                    "use_spatial_hash": True,
                    "custom_class": Wall
                },
                "source": {
                    "use_spatial_hash": True,
                    "custom_class": Source
                },
                "destination": {
                    "use_spatial_hash": True,
                    "custom_class": Dest
                }
            },
            use_spatial_hash = True,
            offset = (SPRITE_DISPLAY_SIZE * (TOOLS_WIDTH + 1), 0) # type: ignore
        )
        self.map = arcade.Scene.from_tilemap(load_map)

    def update(self):
        self.map.update()

    def draw(self):
        self.map.draw()

    
