from math import hypot
from typing import Any
import arcade
from arcade import AnimatedTimeBasedSprite
from arcade import Text
from arcade.hitbox import HitBox
from arcade.types import PathOrTexture
from const import *

DIR_TO_OUT = {
    "bottom": (0, -1),
    "top": (0, 1),
    "left": (-1, 0),
    "right": (1, 0)
}

class Tool(AnimatedTimeBasedSprite):
    def __init__(self, path_or_texture: PathOrTexture = None, center_x: float = 0, center_y: float = 0, scale: float = 1, **kwargs):
        super().__init__(path_or_texture, center_x, center_y, scale, **kwargs)

    def setup(self):
        points = [
            (-SPRITE_DISPLAY_SIZE / 2, -SPRITE_DISPLAY_SIZE / 2),
            (SPRITE_DISPLAY_SIZE / 2, -SPRITE_DISPLAY_SIZE / 2),
            (SPRITE_DISPLAY_SIZE / 2, SPRITE_DISPLAY_SIZE / 2),
            (-SPRITE_DISPLAY_SIZE / 2, SPRITE_DISPLAY_SIZE / 2),
        ]
        self.hit_box = HitBox(points, position=(self.center_x, self.center_y))
        
        self.set_input_output((self.center_x, self.top), "top")
        self.set_input_output((self.center_x, self.bottom), "bottom")
        self.set_input_output((self.left, self.center_y), "left")
        self.set_input_output((self.right, self.center_y), "right")

    def set_input_output(self, top, dir):
        if self.properties[dir] == "in":
            self.input = top
        elif self.properties[dir] == "out":
            self.output = top
            self.out_dir = DIR_TO_OUT[dir]

    def update(self) -> None:
        self.update_animation()
        return super().update()
    
    def clone(self):
        copy = Tool(self.texture, self.center_x, self.center_y, self.scale)
        copy.textures = self.textures
        copy.properties = self.properties
        copy.frames = self.frames
        copy.angle = self.angle
        copy.setup()

        return copy
    
    def direction(self, x, y):
        to_out = arcade.math.get_distance(x, y, self.output[0], self.output[1])
        to_in = arcade.math.get_distance(x, y, self.input[0], self.input[1])
        if to_in < to_out * 0.9:
            dist = arcade.math.get_distance(x, y, self.center_x, self.center_y)
            dx = (self.center_x - x) / dist
            dy = (self.center_y - y) / dist
            return (dx, dy)
        else:
            dist = arcade.math.get_distance(x, y, self.output[0], self.output[1])
            if dist > 1:
                dx = (self.output[0] - x) / dist
                dy = (self.output[1] - y) / dist
                return (dx, dy)
            else:
                return self.out_dir


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

        def _place_text(obj, txt):
            start_x, start_y = obj.coordinates
            start_y = self.tiled_map.height * SPRITE_SIZE - start_y #TODO: fix arcade, not here!
            return Text(txt, start_x * SPRITE_SCALING, start_y * SPRITE_SCALING, align="center", width=obj.size.width, font_size=40)
            
        for obj in self.tiled_map.get_tilemap_layer("osd").tiled_objects:
            if obj.name == "remaining":
               self.remain =  _place_text(obj, "... crate left")
            elif obj.name == "goal":
                self.goal =  _place_text(obj, "... to deliver")

        self.tools = self.map.get_sprite_list("tools")



    def update(self, nb, goal):
        self.map.update()
        self.remain.text = f"{nb:3} crate left"
        self.goal.text = f"{goal:3} to deliver"

    def draw(self):
        self.map.draw()
        self.remain.draw()
        self.goal.draw()

    def setup(self):
        for tool in self.map.get_sprite_list("tools"):
            tool.setup()


