import arcade
import start

SCREEN_TITLE = "Escape The Hacker's Lair"
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650


class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        # self.game_window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.texture = arcade.load_texture("Images/game_over.png")
        self.background = arcade.load_texture("Images/backgroundNoise.png")

    def setup(self):
        arcade.set_background_color(arcade.csscolor.BLACK)
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.5, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100,
                         arcade.color.RED, font_size=30, bold=True, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        start_view = start.StartView()
        self.window.show_view(start_view)
        start_view.setup()
