
SPRITE_SCALING = 8
SPRITE_SIZE = 8
SPRITE_DISPLAY_SIZE = SPRITE_SCALING * SPRITE_SIZE

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Factory connector"

SPRITE_WIDTH = SCREEN_WIDTH // (SPRITE_DISPLAY_SIZE)
SPRITE_HEIGHT = SCREEN_HEIGHT // (SPRITE_DISPLAY_SIZE)

TOOLS_WIDTH = 5


if __name__ == "__main__":
    import sys

    mod = current_module = sys.modules[__name__]
    name = None
    value = None
    for name, value in mod.__dict__.items():
        print(name, ":", value)