import math
import arcade

from const import *
from maps import Map
from toolbelt import Toolbelt
import sound

levels = [
    "assets/first map.tmj",
    "assets/second map.tmj",
]


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Set the background color
        self.background_color = arcade.color.AIR_FORCE_BLUE

        self.level = 0
        self.map = Map(levels[0], self)
        self.toolbelt = Toolbelt()

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.toolbelt.setup()

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw all the sprites.
        self.map.draw()
        self.toolbelt.draw()

    def draw_grid(self):
        for x in range(SPRITE_DISPLAY_SIZE // 2, SCREEN_WIDTH, SPRITE_DISPLAY_SIZE):
            for y in range(SPRITE_DISPLAY_SIZE // 2, SCREEN_HEIGHT, SPRITE_DISPLAY_SIZE):
                arcade.draw_rectangle_outline(x , y, SPRITE_DISPLAY_SIZE, SPRITE_DISPLAY_SIZE, arcade.color.ALMOND)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player
        self.map.update(delta_time)
        if self.map.goal == 0:
            self.level += 1
            if self.level >= len(levels):
                self.level = 0
            self.map = Map(levels[self.level], self)
            sound.yeah.play()
        elif self.map.nb_crate + len(self.map.crates) == 0:
            self.level = 0
            self.map = Map(levels[self.level], self)
        self.toolbelt.update(self.map.nb_crate, self.map.goal)


    def on_mouse_press(self, x, y, button, key_modifiers):
        """mouse press"""

        if self.map.selected and (x, y) in self.map:
            if button == 4:
                self.map.selected = None
            elif button == 1:
                self.map.set_tool()
        else:
            tools = arcade.get_sprites_at_point((x, y), self.toolbelt.tools)
            if tools:
                self.map.selected = tools[0].clone()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.map.selected:
            if (x, y) in self.map:
                x = (math.floor(x / SPRITE_DISPLAY_SIZE)) * SPRITE_DISPLAY_SIZE
                y = (math.floor(y / SPRITE_DISPLAY_SIZE)) * SPRITE_DISPLAY_SIZE
                self.map.selected.left = x
                self.map.selected.bottom = y
            else:
                self.map.selected.center_x = x
                self.map.selected.center_y = y



def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
