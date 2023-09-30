from typing import Any
import arcade
from arcade import Sprite
from arcade.types import PathOrTexture
from const import *

class Tool(Sprite):
    def __init__(self, path_or_texture: PathOrTexture = None, scale: float = 1, center_x: float = 0, center_y: float = 0, angle: float = 0, **kwargs: Any):
        super().__init__(path_or_texture, scale, center_x, center_y, angle, **kwargs)

class Toolbelt:
    def __init__(self) -> None:
        self.tiled_map = arcade.tilemap.TileMap(
            "assets/toolset.tmj",
            scaling = SPRITE_SCALING,
            layer_options = {
                "tools": {
                    "use_spatial_hash": True,
                    "custom_class": Tool
                }
            },
            use_spatial_hash = True,
        )
        self.map = arcade.Scene.from_tilemap(self.tiled_map)

        self.tools = self.map.get_sprite_list("tools")

    def update(self):
        self.map.update()

    def draw(self):
        self.map.draw()
