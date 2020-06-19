import arcade
#import random
import os
import ComputerClue

#user defined classes:
import Levels

SCREEN_TITLE = "Escape The Hacker's Lair"
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

CHARACTER_SCALING = 0.75
TILE_SCALING = 0.5
COIN_SCALING = 0.25
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)

PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 0.75
PLAYER_JUMP_SPEED = 20

LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 100
TOP_VIEWPORT_MARGIN = 100

TEXTURE_FACING_LEFT = 1
TEXTURE_FACING_RIGHT = 0

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        #Player Textures
        self.textures = []
        texture = arcade.load_texture("Images/platformChar_idle.png")
        self.textures.append(texture)
        texture = arcade.load_texture("Images/platformChar_idle.png", mirrored=True)
        self.textures.append(texture)

        self.scale = CHARACTER_SCALING

        #Default texture - set right
        self.set_texture(TEXTURE_FACING_RIGHT)

    def update_animation(self, delta_time: float = 1/60):

        #Player image based on movement
        if (self.change_x < 0):
            self.texture = self.textures[TEXTURE_FACING_LEFT]
        elif self.change_x > 0:
            self.texture = self.textures[TEXTURE_FACING_RIGHT]


#Start of new code TextButtons and StartView
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


class Lev5Button(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Level 5", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


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
        lev2_button = Lev2Button(350, 200, self.go_to_lev2)
        self.button_list.append(lev2_button)
        lev3_button = Lev3Button(500, 200, self.go_to_lev3)
        self.button_list.append(lev3_button)
        lev4_button = Lev4Button(650, 200, self.go_to_lev4)
        self.button_list.append(lev4_button)
        lev5_button = Lev5Button(800, 200, self.go_to_lev5)
        self.button_list.append(lev5_button)

    #Draws this window
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.texture1.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.3, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        self.texture2.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.7, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 8)

        for button in self.button_list:
            button.draw()
        
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

    def go_to_lev5(self):
        game_view = MyGame()
        game_view.setup(4)
        self.window.show_view(game_view)


class MyGame(arcade.View):        #Changed '.Window' to .View
    def __init__(self):
        super().__init__()    #Got rid of parameters (not needed for view)

        self.coin_list = None
        self.wall_list = None
        self.background_list = None
        self.player_list = None
        self.enemy_list = None
        self.player_sprite = None
        self.physics_engine = None
        self.view_bottom = 0
        self.view_left = 0
        self.score = 0
        self.game_over = False
        arcade.set_background_color(arcade.csscolor.BLACK)

        #Check if movement key is being pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        #Determines map
        self.level = 0
        self.levels = None

        #computer clue info:
        self.comp_clue = None

    def setup(self, level):
        #setup sprite lists
        self.view_bottom = 0
        self.view_left = 0
        self.score = 0
        self.coinTotal = 0
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()

        #setup player sprite:
        self.player_sprite = Player()
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        #setup level info:
        self.levels = Levels.level_list
        self.levels[self.level].setup()
        for wall in self.levels[self.level].get_walls(): self.wall_list.append(wall)
        for coin in self.levels[self.level].get_coins(): self.coin_list.append(coin)
        for enemy in self.levels[self.level].get_enemies(): self.enemy_list.append(enemy)
        for background in self.levels[self.level].get_background(): self.background_list.append(background)
        self.coinTotal = len(self.coin_list)

        """
        this is the old code commented out so you can see what I changed:
        #setup enemy sprites
        enemy = arcade.Sprite("Images/robot.png", CHARACTER_SCALING)
        enemy.center_x = 800
        enemy.center_y = 110
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        #setup map:
        #Map is loaded based on the level
        map_name = f"maps/cave_{level}.tmx"
        platforms_layer_name = 'Platforms'
        coins_layer_name = 'Coins'
        my_map = arcade.tilemap.read_tmx(map_name)

        #!-- Platform section --!
        #set up platforms:
        self.wall_list = arcade.tilemap.process_layer(map_object = my_map,
                                                      layer_name = platforms_layer_name,
                                                      scaling = TILE_SCALING)
        #!-- Coin section --!
        #setup coins and total:
        self.coin_list = arcade.tilemap.process_layer(my_map, coins_layer_name, TILE_SCALING)
        self.coinTotal = len(self.coin_list)

        #!--Background section --!
        #setup background objects:
        self.background_list = arcade.tilemap.process_layer(my_map, "Background", TILE_SCALING)
        """
        #setup background:
        if level == 1:
            arcade.set_background_color((109,205,247))

        #setup Computer Clue system:
        self.comp_clue = ComputerClue.ComputerClue()
        self.comp_clue.setup()

        ##setup physics engine:
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)
    def on_draw(self):
        arcade.start_render()
        self.background_list.draw()
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()
        self.enemy_list.draw()
        self.comp_clue.draw_clue()

        #Display Objective
        score_text = f"Computer pieces found: {self.score} / {self.coinTotal}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom,
                         arcade.csscolor.WHITE, 18)

    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        if key == arcade.key.RIGHT:
            self.right_pressed = True
        if key == arcade.key.LEFT:
            self.left_pressed = True
        if key == arcade.key.ENTER:
            if self.comp_clue.show_clue:
                self.comp_clue.exit_clue()

    def on_key_release(self, key, modifiers: int):
        if key == arcade.key.UP:
            self.up_pressed = False
        if key == arcade.key.DOWN:
            self.down_pressed = False
        if key == arcade.key.RIGHT:
            self.right_pressed = False
        if key == arcade.key.LEFT:
            self.left_pressed = False


    def on_update(self, delta_time):
        #Update Player Image
        self.player_list.update_animation()

        #!--Movement section --!
        self.player_sprite.change_x = 0

         #Left - Right
        if self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED

        #check if game over:
        if not self.game_over:


            #check state of enemy and adjust:
            for enemy in self.enemy_list:
                if len(arcade.check_for_collision_with_list(enemy, self.wall_list)) > 0:
                    #reverse if hit wall
                    enemy.change_x *= -1


            #check for coins collected
            coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                 self.coin_list)
            if coin_hit_list:
                self.comp_clue.show_clue = True
                self.comp_clue.update_clue_pos(self.view_bottom, self.view_left)
            if self.comp_clue.show_clue == False:
                #update physics engine
                self.physics_engine.update()
                #move enemies
                self.enemy_list.update()

            #remove found coins and update score:
            for coin in coin_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1

            #adjust viewport:
            changed = False
            #left:
            left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
            if self.player_sprite.left < left_boundary:
                self.view_left -= left_boundary - self.player_sprite.left
                changed = True
            #right:
            right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
            if self.player_sprite.right > right_boundary:
                self.view_left += self.player_sprite.right - right_boundary
                changed = True
            #up:
            top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
            if self.player_sprite.top > top_boundary:
                self.view_bottom += self.player_sprite.top - top_boundary
                changed = True
            #down:
            bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
            if self.player_sprite.bottom < bottom_boundary:
                self.view_bottom -= bottom_boundary - self.player_sprite.bottom
                changed = True

            if changed:
                self.view_bottom = int(self.view_bottom)
                self.view_left = int(self.view_left)
                arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left,
                                    self.view_bottom, SCREEN_HEIGHT + self.view_bottom)

            #Check to advance level
            #if(self.score == self.coinTotal):
                #self.level += 1

                #Setup next level
                #self.setup(self.level)

            #check for player hitting enemy:
            if len(arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)) > 0:
                self.game_over = True

        #!--Game Over --!
        else:
            self.setup(self.level)
            self.game_over = False


def main():
    game_window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = StartView()
    game_window.show_view(start_view)
    start_view.setup()
    arcade.run()
                      

#Old 'main()' for Window
'''
def main():
    window = MyGame()
    window.setup(window.level)
    arcade.run()'''

if __name__ == "__main__":
    main()
