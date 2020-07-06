# Pause Menu

import arcade

WIDTH = 1000
HEIGHT = 650

class PauseMenu(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.pause_box = arcade.Sprite("images/pause_back.png", 1, center_x=WIDTH/2, center_y=HEIGHT/2)

    def on_draw(self):
        arcade.start_render()

        # draw background
        self.pause_box.draw()

        # pause menu title ---------- +
        arcade.draw_text("PAUSE MENU", 
        WIDTH/2, HEIGHT/2 + 50, 
        arcade.color.WHITE, 
        font_size = 50, 
        anchor_x = "center")
        # --------------------------- +

        # menu options -------------- +
        arcade.draw_text("RESUME: P",
        WIDTH / 2,
        HEIGHT / 2,
        arcade.color.WHITE,
        font_size = 20,
        anchor_x = "center")
        # --------------------------- +

    def on_key_press(self, key, _modifiers):

        # resume game
        if key == arcade.key.P:   
            self.window.show_view(self.game_view)
