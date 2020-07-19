# Pause Menu

import arcade
import start
import EscapeGame

WIDTH = 1000
HEIGHT = 650

class PauseMenu(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.pause_box = arcade.Sprite("images/pause_back.png", 1, center_x=WIDTH/2, center_y=HEIGHT/2)
        
        # pause menu title ---------- +
        self.title = arcade.draw_text("|-- P A U S E   M E N U --|", 
        WIDTH/2, HEIGHT/2, 
        arcade.color.WHITE, font_size = 55, 
        anchor_x = "center")
        # --------------------------- +

        # menu options -------------- +
        self.resume = arcade.draw_text("(P) RESUME",
        WIDTH / 2, HEIGHT / 2,
        arcade.color.WHITE, font_size = 20, 
        anchor_x = "left")

        self.quit = arcade.draw_text("(Q) QUIT GAME",
        WIDTH / 2, HEIGHT / 2,
        arcade.color.WHITE, font_size = 20,
        anchor_x = "left")

        self.controls = arcade.draw_text("CONTROLS",
        WIDTH / 2, HEIGHT / 2,
        arcade.color.WHITE, font_size = 32,
        anchor_x = "right")
        # --------------------------- +

    def set_menu_position(self, left, bottom):
        self.pause_box.center_x = left + WIDTH/2
        self.pause_box.center_y = bottom + HEIGHT/2

        # -----
        self.title.center_x = left + WIDTH/2
        self.title.center_y = bottom + HEIGHT/2 + 175

        # -----
        self.controls.center_x = left + WIDTH/2 + 275
        self.controls.center_y = bottom + HEIGHT/2 + 60

        # -----
        self.resume.center_x = left + WIDTH/2 - 310
        self.resume.center_y = bottom + HEIGHT/2 + 60

        self.quit.center_x = left + WIDTH/2 - 295
        self.quit.center_y = bottom + HEIGHT/2 - 15

    def on_draw(self):

        # draw background
        self.pause_box.draw()

        # draw menu title
        self.title.draw()

        # draw menu options
        self.controls.draw()
        self.resume.draw()
        self.quit.draw()
        # --------------------------- +

    def on_key_press(self, key, _modifiers):

        # resume game
        if key == arcade.key.P:   
            self.window.show_view(self.game_view)

        # quit to the title screen
        elif key == arcade.key.Q:
            start_view = start.StartView()
        self.window.show_view(start_view)
        start_view.setup()
        arcade.run()
