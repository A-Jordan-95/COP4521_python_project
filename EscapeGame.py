import arcade
#import random
import os

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


    def setup(self):
        #setup sprite lists
        self.view_bottom = 0
        self.view_left = 0
        self.score = 0
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()

        #setup player sprite:
        image_source = "Images/platformChar_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        #setup enemy sprites
        enemy = arcade.Sprite("Images/robot.png", CHARACTER_SCALING)
        enemy.center_x = 800
        enemy.center_y = 110
        enemy.change_x = 2
        self.enemy_list.append(enemy)
        #setup map:
        map_name = "maps/map.tmx"
        platforms_layer_name = 'Platforms'
        coins_layer_name = 'Coins'
        my_map = arcade.tilemap.read_tmx(map_name)
        #set up platforms:
        self.wall_list = arcade.tilemap.process_layer(map_object = my_map,
                                                      layer_name = platforms_layer_name,
                                                      scaling = TILE_SCALING)

        #setup coins:
        self.coin_list = arcade.tilemap.process_layer(my_map, coins_layer_name, TILE_SCALING)

        #setup background objects:
        self.background_list = arcade.tilemap.process_layer(my_map, "Background", TILE_SCALING)

        #setup background:
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

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


        score_text = f"Computer pieces found: {self.score}"
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

        #!--Movement section --!
        self.player_sprite.change_x = 0

         #Left - Right
        if self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        #-Movement section end--

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
            #check for player hitting enemy:
            if len(arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)) > 0:
                self.game_over = True

        #!--Game Over --!
        else:
            self.setup()
            self.game_over = False


def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
