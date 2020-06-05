import arcade
#import random
import os

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


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

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
        if level == 2:
            arcade.set_background_color((109,205,247))


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
            #move enemies
            self.enemy_list.update()

            #check state of enemy and adjust:
            for enemy in self.enemy_list:
                if len(arcade.check_for_collision_with_list(enemy, self.wall_list)) > 0:
                    #reverse if hit wall
                    enemy.change_x *= -1

            #update physics engine
            self.physics_engine.update()
            #check for coins collected
            coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                 self.coin_list)
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
    window = MyGame()
    window.setup(window.level)
    arcade.run()

if __name__ == "__main__":
    main()
