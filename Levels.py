import arcade
from numpy import random
import os

TILE_SCALING = 0.5
CHARACTER_SCALING = 0.75

class Level():#create inherited classes for each level in game and overload
              #the setup function to place your enemies where you want/Determine
              #their behavior
    def __init__(self):
        self.map_path = None #holds string which is path to map
        self.map_object #holds arcade tilemap object
        self.enemy_sprite_list = None
        self.wall_list = None
        self.coin_list = None
        self.background_list = None

    def setup(self, map_path):
        #setup level information here:
        self.map_path = map_path
        self.map_object= arcade.tilemap.read_tmx(self.map_path)
        self.enemy_sprite_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        #!-- Platform section --!
        #set up platforms:
        self.wall_list = arcade.tilemap.process_layer(map_object = self.map_object,
                                                      layer_name = "Platforms",
                                                      scaling = TILE_SCALING)
        #!-- Coin section --!
        #setup coins and total:
        self.coin_list = arcade.tilemap.process_layer(self.map_object,"Coins", TILE_SCALING)


        #!--Background section --!
        #setup background objects:
        self.background_list = arcade.tilemap.process_layer(self.map_object,"Background", TILE_SCALING)

        #set up enemies:
        self.enemy_sprite_list = arcade.tilemap.process_layer(self.map_object,"Enemies", TILE_SCALING)

    def get_walls(self):
        return self.wall_list

    def get_enemies(self):
        return self.enemy_sprite_list

    def get_coins(self):
        return self.coin_list

    def get_background(self):
        return self.background_list


class Level1(Level):
    def __init__(self):
        self.map_object = None
        super().__init__()


    def setup(self):
        x = "Images/"
        super().setup("maps/cave_1.tmx")
        for enemy in self.enemy_sprite_list:
            enemy.change_x = 2 #set speed of enemies
"""
class Level2(Level):
    def __init__(self):
        super().__init__()

    def setup(self):
        x = "Images/"
        super().setup("your map path here")
        for enemy in self.enemy_sprite_list:
            enemy.change_x = 'your enemy speed here'

class Level3(Level):
    def __init__(self):
        super().__init__()

    def setup(self):
        x = "Images/"
        super().setup("your map path here")
        for enemy in self.enemy_sprite_list:
            enemy.change_x = 'your enemy speed here'

class Level4(Level):
    def __init__(self):
        super().__init__()

    def setup(self):
        x = "Images/"
        super().setup("your map path here")
        for enemy in self.enemy_sprite_list:
            enemy.change_x = 'your enemy speed here'

class Level5(Level):
    def __init__(self):
        super().__init__()

    def setup(self):
        x = "Images/"
        super().setup("your map path here")
        for enemy in self.enemy_sprite_list:
            enemy.change_x = 'your enemy speed here'
"""

lev1 = Level1()
#lev2 = Level2()
#lev3 = Level3()
#lev4 = Level4()
#lev5 = Level5()
level_list = [lev1]
