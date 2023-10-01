from itertools import chain
from typing import TYPE_CHECKING, Any, Optional, Self
import arcade
from arcade import Sprite
from arcade.types import PathOrTexture

from const import *
from crate import Crate
from toolbelt import Tool
import sound

if TYPE_CHECKING:
    from app import MyGame

class Wall(Sprite):
    def setup(self):
        pass

    def direction(self, *args):
        return None

int_to_direction = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0)
}

class Dest(Sprite):
    def setup(self):
        self._direction = int_to_direction[self.properties["direction"]]

    def direction(self, *args):
        return "win"

class Source(Sprite):
    map: "Map"
    def __init__(self, path_or_texture: PathOrTexture = None, scale: float = 1, center_x: float = 0, center_y: float = 0, angle: float = 0, **kwargs: Any):
        self.generator = 0
        self.map = kwargs["map"]
        super().__init__(path_or_texture, scale, center_x, center_y, angle, **kwargs)

    def setup(self):
        self._direction = int_to_direction[self.properties["direction"]]

    def direction(self, *args):
        return self._direction

    def update(self):
        self.generator += 1
        if self.generator == 80:
            sound.launch.play()

        if self.generator > 100:
            self.generator -= 100
            self.map.add_crate(self.center_x, self.center_y)


OFFSET = SPRITE_DISPLAY_SIZE * (TOOLS_WIDTH + 1)


class Map():
    selected: None | Tool = None
    tiled_map: arcade.tilemap.TileMap
    grid: list[list[None | Source | Wall | Dest | Tool]]
    nb_crate: int
    goal: int
    
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
                    "custom_class": Source,
                    "custom_class_args" : {
                        "map": self
                    }
                },
                "destination": {
                    "use_spatial_hash": True,
                    "custom_class": Dest
                }
            },
            use_spatial_hash = True,
            offset = (OFFSET, 0) # type: ignore
        )
        assert self.tiled_map.properties
        goal = self.tiled_map.properties["goal"]
        assert isinstance(goal, int)
        self.goal = goal
        nb_crate = self.tiled_map.properties["crate"]
        assert isinstance(nb_crate, int)
        self.nb_crate = nb_crate

        self.map = arcade.Scene.from_tilemap(self.tiled_map)

        self.map.add_sprite_list("conveyer")
        self.conveyers = self.map.get_sprite_list("conveyer")

        self.map.add_sprite_list("crate")
        self.crates = self.map.get_sprite_list("crate")

        self.walls = self.map.get_sprite_list("wall")
        self.source = self.map.get_sprite_list("source")
        self.dest = self.map.get_sprite_list("destination")

        self.grid = [[None for _ in range(int(self.tiled_map.height))]
                     for _ in range(int(self.tiled_map.width))]

        item:Source | Wall | Dest | Tool
        for item in chain(self.walls, self.source, self.dest):
            item.setup()
            self[item.center_x, item.center_y] = item

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
    
    def __setitem__(self, pos, value):
        x, y = pos
        x, y = self._get_grid_pos(x, y)
        self.grid[x][y] = value

    
    def set_tool(self):
        assert self.selected is not None, "cannot set unselected tools!"

        pos = (self.selected.center_x, self.selected.center_y)
        at_pos = self[pos]
        if at_pos:
            if isinstance(at_pos, Tool):
                at_pos.kill()
            else:
                return

        clone = self.selected.clone()
        self[clone.center_x, clone.center_y] = clone
        self.conveyers.append(clone)

    def add_crate(self, x:float, y:float):
        #sound.launch.play()
        #sound.play_sound(sound.launch)

        self.nb_crate -= 1

        new_crate = Crate(self, x, y)
        if arcade.check_for_collision_with_list(new_crate, self.crates):
            sound.lost.play()
        else:
            self.crates.append(new_crate)




    
