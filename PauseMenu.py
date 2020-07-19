# Pause Menu

import arcade
import start
import EscapeGame

WIDTH = 1000
HEIGHT = 650

class PauseMenu(arcade.View):
    def __init__(self, game_view): #{
        super().__init__()
        self.game_view = game_view
        self.pause_box = arcade.Sprite("images/pause_background.png", 1.2, 
            center_x=WIDTH/2, center_y=HEIGHT/2)
        self.control_image = arcade.Sprite("images/Controls_Display.png", 1.1, 
            center_x=WIDTH/2, center_y=HEIGHT/2)
        
        # pause menu title ---------- +
        self.title = arcade.draw_text("P A U S E   M E N U", 
            WIDTH/2, HEIGHT/2, 
            arcade.color.WHITE, font_size = 57, 
            anchor_x = "center")
        # --------------------------- +

        # menu options -------------- +
        self.quit = arcade.draw_text("(Q) : Quit to Main Menu",
            WIDTH / 2, HEIGHT / 2,
            arcade.color.WHITE, font_size = 20,
            anchor_x = "left")

        self.controls = arcade.draw_text("CONTROLS",
            WIDTH / 2, HEIGHT / 2,
            arcade.color.WHITE, font_size = 30,
            anchor_x = "right")

        self.jump_text = arcade.draw_text("jump",
            WIDTH / 2, HEIGHT / 2,
            arcade.color.WHITE, font_size = 16,
            anchor_x = "right")

        self.pause_text = arcade.draw_text("pause / resume",
            WIDTH / 2, HEIGHT / 2,
            arcade.color.WHITE, font_size = 16,
            anchor_x = "right")

        self.move_text = arcade.draw_text("move right",
            WIDTH / 2, HEIGHT / 2,
            arcade.color.WHITE, font_size = 16,
            anchor_x = "right")

        self.move_text2 = arcade.draw_text("move left",
            WIDTH / 2, HEIGHT / 2,
            arcade.color.WHITE, font_size = 16,
            anchor_x = "right")
        # --------------------------- +
    #}

    def set_menu_position(self, left, bottom): #{
        self.pause_box.center_x = left + WIDTH/2
        self.pause_box.center_y = bottom + HEIGHT/2
        self.pause_box.alpha = 25

        self.control_image.center_x = left + WIDTH/2 + 230
        self.control_image.center_y = bottom + HEIGHT/2 - 70

        # -----
        self.title.center_x = left + WIDTH/2 - 20
        self.title.center_y = bottom + HEIGHT/2 + 168

        # -----
        self.controls.center_x = left + WIDTH/2 + 230
        self.controls.center_y = bottom + HEIGHT/2 + 75

        # -----
        self.quit.center_x = left + WIDTH/2 - 310
        self.quit.center_y = bottom + HEIGHT/2 - 185

        self.jump_text.center_x = left + WIDTH/2 + 232
        self.jump_text.center_y = bottom + HEIGHT/2 + 26

        self.move_text.center_x = left + WIDTH/2 + 357
        self.move_text.center_y = bottom + HEIGHT/2 - 72

        self.move_text2.center_x = left + WIDTH/2 + 105
        self.move_text2.center_y = bottom + HEIGHT/2 - 72

        self.pause_text.center_x = left + WIDTH/2 + 235
        self.pause_text.center_y = bottom + HEIGHT/2 - 170
    #}

    def on_draw(self): #{
        # draw background
        self.pause_box.draw()
        self.control_image.draw()

        # draw menu title
        self.title.draw()

        # draw menu options
        self.quit.draw()
        self.controls.draw()
        self.jump_text.draw()
        self.pause_text.draw()
        self.move_text.draw()
        self.move_text2.draw()
    #}

    def on_key_press(self, key, _modifiers): #{
        # resume game
        if key == arcade.key.P:
            self.window.show_view(self.game_view)

        # quit to the title screen
        elif key == arcade.key.Q:
            start_view = start.StartView()
            self.window.show_view(start_view)
            start_view.setup()
            arcade.run()
    #}
