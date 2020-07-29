import arcade

class ComputerClue():
    def __init__(self):
        self.show_clue = False
        self.first_clue = True
        self.clue_sprite = None
        self.clue_sprite_list = None
        self.clues = None #list of strings(each string being a clue) passed to setup function
        self.clue_pos = 0

    def setup(self, level):
        self.clue_sprite_list = arcade.SpriteList()
        
        self.clues = self.parse_clues(level)

        self.clue_sprite = arcade.Sprite("Images/clue_window.png", 1.0)
        self.clue_sprite_list.append(self.clue_sprite)

    def parse_clues(self, level):
        print("parsing clues...")
        print(f"level = {level}")
        f = open("questions/questions.txt", "r")
        clues = []
        if level == 0:
            for line in f:
                if "Q1" not in line:
                    continue 
                else:
                    while "Cl1" not in line:
                        line = f.readline()
                    clues = [f.readline() for x in range(3)]
                    clues.insert(0, line)
                    print(clues)

        elif level == 1:
            for line in f:
                if "Q2" not in line:
                    continue 
                else:
                    while "Cl1" not in line:
                        line = f.readline()
                    clues = [f.readline() for x in range(3)]
                    clues.insert(0, line)
                    print(clues)

        elif level == 2:
            for line in f:
                if "Q3" not in line:
                    continue 
                else:
                    while "Cl1" not in line:
                        line = f.readline()
                    clues = [f.readline() for x in range(3)]
                    clues.insert(0, line)
                    print(clues)

        elif level == 3:
            for line in f:
                if "Q4" not in line:
                    continue 
                else:
                    while "Cl1" not in line:
                        line = f.readline()
                    clues = [f.readline() for x in range(3)]
                    clues.insert(0, line)
                    print(clues)

        elif level == 4:
            for line in f:
                if "Q5" not in line:
                    continue 
                else:
                    while "Cl1" not in line:
                        line = f.readline()
                    clues = [f.readline() for x in range(3)]
                    clues.insert(0, line)
                    print(clues)
        return clues

    def update_clue_pos(self, view_bottom, view_left):
        self.clue_sprite_list[0].center_x = view_left + 500
        self.clue_sprite_list[0].center_y = view_bottom + 325


    def draw_clue(self):
        if self.show_clue:
            self.clue_sprite_list.draw()
            arcade.draw_text(self.clues[self.clue_pos], self.clue_sprite_list[0].center_x - 40, self.clue_sprite_list[0].center_y,
            arcade.csscolor.WHITE, 18)
            arcade.draw_text("Press Enter to close the clue.", self.clue_sprite_list[0].center_x - 200, self.clue_sprite_list[0].center_y - 100,
            arcade.csscolor.WHITE, 18)

    def exit_clue(self):
        if self.show_clue:
            self.show_clue = False
            if self.clue_pos < 3:
                self.clue_pos += 1
            else:
                self.clue_pos = 0

    def get_clue(self):
        return self.clues[self.clue_pos]
