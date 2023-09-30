from typing import Any
import arcade
from arcade import AnimatedTimeBasedSprite
from arcade.hitbox import HitBox
from arcade.types import PathOrTexture
from const import *

class Tool(AnimatedTimeBasedSprite):
    def setup(self):
        points = [
            (-SPRITE_DISPLAY_SIZE / 2, -SPRITE_DISPLAY_SIZE / 2),
            (SPRITE_DISPLAY_SIZE / 2, -SPRITE_DISPLAY_SIZE / 2),
            (SPRITE_DISPLAY_SIZE / 2, SPRITE_DISPLAY_SIZE / 2),
            (-SPRITE_DISPLAY_SIZE / 2, SPRITE_DISPLAY_SIZE / 2),
        ]
        self.hit_box = HitBox(points, position=(self.center_x, self.center_y))

    def update(self) -> None:
        self.update_animation()
        return super().update()
    
    def clone(self):
        copy = Tool(self.texture, self.center_x, self.center_y, self.scale)
        copy.properties = self.properties
        copy.setup()

        return copy

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

    def setup(self):
        for tool in self.map.get_sprite_list("tools"):
            tool.setup()


