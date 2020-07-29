from time import sleep
import arcade
print("inside start.py: imported arcade")
from EscapeGame import MyGame 
print("inside start.py: from EscapeGame imported MyGame ")
from Levels import level_list

#Start of new code TextButtons and StartView
SCREEN_TITLE = "Escape The Hacker's Lair"
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
 
class TextButton:
    """ Text-based button """
    def __init__(self,
                 center_x, center_y,
                 width, height,
                 text,
                 font_size=18,
                 font_face="Arial",
                 face_color=arcade.color.WHITE,
                 highlight_color=arcade.color.WHITE,
                 shadow_color=arcade.color.DARK_GRAY,
                 button_height=2):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height

    def draw(self):
        """ Draw the button """
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)

        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # Bottom horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y - self.height / 2,
                         color, self.button_height)

        # Right vertical
        arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # Top horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        # Left vertical
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x - self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y,
                         arcade.color.RED, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False


def check_mouse_press_for_buttons(x, y, button_list):
    """ Given an x, y, see if we need to register any button clicks. """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()


def check_mouse_release_for_buttons(_x, _y, button_list):
    """ If a mouse button has been released, see if we need to process
        any release events. """
    for button in button_list:
        if button.pressed:
            button.on_release()


class Lev1Button(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Level 1", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Lev2Button(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Level 2", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Lev3Button(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Level 3", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Lev4Button(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Level 4", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


'''class Lev5Button(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Level 5", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()'''

class score():
    def __init__(self, center_x, center_y, score):
        self.center_x = center_x
        self.center_y = center_y
        if score:
            self.score = score
        else: 
            self.score = None

    def draw(self):
        if self.score:
            arcade.draw_text("{:.2f} sec".format(self.score), self.center_x, self.center_y,
                        arcade.csscolor.WHITE, 18)



class StartView(arcade.View):
    #Runs when this window is called
    def __init__(self):
        super().__init__()
        self.texture1 = arcade.load_texture("Images/Escape!.png")
        self.texture2 = arcade.load_texture("Images/TheLair.png")
        self.background = None

    def setup(self):
        arcade.set_background_color(arcade.csscolor.BLACK)
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.background = arcade.load_texture("Images/evilLair.png")

        self.button_list = []
        lev1_button = Lev1Button(200, 200, self.go_to_lev1)
        self.button_list.append(lev1_button)
        lev2_button = Lev2Button(400, 200, self.go_to_lev2)
        self.button_list.append(lev2_button)
        lev3_button = Lev3Button(600, 200, self.go_to_lev3)
        self.button_list.append(lev3_button)
        lev4_button = Lev4Button(800, 200, self.go_to_lev4)
        self.button_list.append(lev4_button)
        '''lev5_button = Lev5Button(800, 200, self.go_to_lev5)
        self.button_list.append(lev5_button)'''

        self.score_list = []
        lev1_score = score(100, 100, level_list[0].score)
        self.score_list.append(lev1_score)
        lev2_score = score(200, 100, level_list[1].score)
        self.score_list.append(lev2_score)
        lev3_score = score(200, 100, level_list[2].score)
        self.score_list.append(lev3_score)
        lev4_score = score(200, 100, level_list[3].score)
        self.score_list.append(lev4_score)

    #Draws this window
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.texture1.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.3, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        self.texture2.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.7, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 8)

        for button in self.button_list:
            button.draw()

        for score in self.score_list:
            score.draw()
        
    #Do this on Mouse click
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        check_mouse_release_for_buttons(x, y, self.button_list)

    def go_to_lev1(self):
        game_view = MyGame()
        game_view.setup(0)
        self.window.show_view(game_view)

    def go_to_lev2(self):
        game_view = MyGame()
        game_view.setup(1)
        self.window.show_view(game_view)

    def go_to_lev3(self):
        game_view = MyGame()
        game_view.setup(2)
        self.window.show_view(game_view)

    def go_to_lev4(self):
        game_view = MyGame()
        game_view.setup(3)
        self.window.show_view(game_view)

    '''def go_to_lev5(self):
        game_view = MyGame()
        game_view.setup(4)
        self.window.show_view(game_view)'''
