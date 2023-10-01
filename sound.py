import arcade
import pyglet

lost: arcade.Sound = arcade.load_sound("assets/sound/lost.mp3") # type: ignore
launch: arcade.Sound  = arcade.load_sound("assets/sound/launch.mp3") # type: ignore
yeah: arcade.Sound = arcade.load_sound("assets/sound/yeah.mp3") # type: ignore

assert lost
assert launch
assert yeah

player = pyglet.media.Player()
player.queue(lost.source)
player.on_eos
player.pause()

