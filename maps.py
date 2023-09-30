from typing import Any, Self
import arcade
from arcade import Sprite
from arcade.types import PathOrTexture

from const import *
from toolbelt import Tool

class Wall(Sprite):
    pass

class Dest(Sprite):
    pass

class Source(Sprite):
    pass

class Map():
    selected: None | Tool = None
    
    def __init__(self, path:str) -> None:
        self.tiled_map = arcade.tilemap.TileMap(
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
        self.map = arcade.Scene.from_tilemap(self.tiled_map)

    def update(self):
        self.map.update()

    def draw(self):
        self.map.draw()

    def __contains__(self, pos):
        start_x = SPRITE_DISPLAY_SIZE * (TOOLS_WIDTH + 1)
        x, y = pos
        return start_x <= x < start_x + self.tiled_map.width and 0 <= y < self.tiled_map.height

    
