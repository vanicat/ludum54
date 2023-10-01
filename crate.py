from typing import Any
import arcade
from arcade import Sprite
from arcade import check_for_collision_with_list
from arcade.types import PathOrTexture

from const import *
import maps

import sound

class Crate(Sprite):
    def __init__(self, map:"maps.Map", center_x: float = 0, center_y: float = 0):
        self.map = map

        texture = arcade.load_texture("assets/tiles.png", 
                                      x = 0, y = 4 * SPRITE_SIZE, 
                                      width=SPRITE_SIZE, height=SPRITE_SIZE)
        
        super().__init__(texture, SPRITE_SCALING, center_x, center_y, 0)

    def update(self):
        under = self.map[(self.center_x, self.center_y)]
        if under and (dir := under.direction(self.center_x, self.center_y)):
            if dir == "win":
                self.kill()
                sound.yeah.play()
                self.map.goal -= 1
            else:
                dx, dy = dir
                
                self.center_x += dx
                self.center_y += dy

                colision = check_for_collision_with_list(self, self.map.crates)
                colision = colision or check_for_collision_with_list(self, self.map.walls)
                if colision:
                    if abs(dx) < abs(dy):
                        self.center_x -= dx
                    else:
                        self.center_y -= dy
                    colision = check_for_collision_with_list(self, self.map.crates)
                    colision = colision or check_for_collision_with_list(self, self.map.walls)
                    if colision:
                        if abs(dx) < abs(dy):
                            self.center_y -= dy
                        else:
                            self.center_x -= dx

                pass
        else:
            self.kill()
            sound.lost.play()
