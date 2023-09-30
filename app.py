import arcade

from const import *
from maps import Map
from toolbelt import Toolbelt

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

        self.map = Map("assets/first map.tmj")
        self.toolbelt = Toolbelt()

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        pass

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
        self.map.update()



def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
