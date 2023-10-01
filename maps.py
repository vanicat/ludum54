from itertools import chain
from typing import TYPE_CHECKING, Any, Optional, Self
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


OFFSET = SPRITE_DISPLAY_SIZE * (TOOLS_WIDTH + 1)


class Map():
    selected: None | Tool = None
    tiled_map: arcade.tilemap.TileMap
    grid: list[list[None | Source | Wall | Dest | Tool]]
    
    def __init__(self, path:str, game:"MyGame") -> None:
        self.game = game

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
            offset = (OFFSET, 0) # type: ignore
        )
        self.map = arcade.Scene.from_tilemap(self.tiled_map)
        self.map.add_sprite_list("conveyer")
        self.conveyers = self.map.get_sprite_list("conveyer")
        self.walls = self.map.get_sprite_list("wall")
        self.source = self.map.get_sprite_list("source")
        self.dest = self.map.get_sprite_list("destination")

        self.grid = [[None for _ in range(int(self.tiled_map.height))]
                     for _ in range(int(self.tiled_map.width))]

        item:Source | Wall | Dest | Tool
        for item in chain(self.walls, self.source, self.dest):
            x, y = self._get_grid_pos(item.center_x, item.center_y)
            self.grid[x][y] = item

    def _get_grid_pos(self, x, y):
        x = int((x - OFFSET) // SPRITE_DISPLAY_SIZE)
        y = int(y // SPRITE_DISPLAY_SIZE)
        return x,y
            

    def update(self, deltatime):
        self.map.update()

    def draw(self):
        self.map.draw()
        if self.selected:
            self.selected.draw()

    def __contains__(self, pos):
        start_x = SPRITE_DISPLAY_SIZE * (TOOLS_WIDTH + 1)
        width = self.tiled_map.width * SPRITE_DISPLAY_SIZE
        height = self.tiled_map.height * SPRITE_DISPLAY_SIZE
        x, y = pos
        return start_x <= x < start_x + width and 0 <= y < height
    
    def __getitem__(self, pos):
        x, y = pos
        x, y = self._get_grid_pos(x, y)
        return self.grid[x][y]
    
    def set_tool(self):
        assert self.selected is not None, "cannot set unselected tools!"

        pos = (self.selected.center_x, self.selected.center_y)
        if arcade.get_sprites_at_point(pos, self.walls): return
        if arcade.get_sprites_at_point(pos, self.dest): return
        if arcade.get_sprites_at_point(pos, self.source): return

        self.conveyers.append(self.selected.clone())






    
