import arcade

class ComputerClue():
    def __init__(self):
        self.show_clue = False
        self.show_question = False
        self.first_clue = True
        self.clue_sprite = None
        self.clue_sprite_list = None
        self.questions = None
        self.clues = None #list of strings(each string being a clue) passed to setup function
        self.answers = None
        self.clue_pos = 0

    def setup(self, questions, clues, answers):
        self.clue_sprite_list = arcade.SpriteList()
        self.questions = questions
        self.clues = clues
        self.answers = answers
        self.clue_sprite = arcade.Sprite("Images/clue_window.png", 1.5)
        self.clue_sprite_list.append(self.clue_sprite)

<<<<<<< HEAD
    def parse_clues(self, level):
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

        elif level == 1:
            for line in f:
                if "Q2" not in line:
                    continue 
                else:
                    while "Cl1" not in line:
                        line = f.readline()
                    clues = [f.readline() for x in range(3)]
                    clues.insert(0, line)
            

        elif level == 2:
            for line in f:
                if "Q3" not in line:
                    continue 
                else:
                    while "Cl1" not in line:
                        line = f.readline()
                    clues = [f.readline() for x in range(3)]
                    clues.insert(0, line)
                   

        elif level == 3:
            for line in f:
                if "Q4" not in line:
                    continue 
                else:
                    while "Cl1" not in line:
                        line = f.readline()
                    clues = [f.readline() for x in range(3)]
                    clues.insert(0, line)
                 

        elif level == 4:
            for line in f:
                if "Q5" not in line:
                    continue 
                else:
                    while "Cl1" not in line:
                        line = f.readline()
                    clues = [f.readline() for x in range(3)]
                    clues.insert(0, line)
                
        return clues

=======
>>>>>>> 94d3992ee0b72e08e99f4675fd0be013f487eff9
    def update_clue_pos(self, view_bottom, view_left):
        self.clue_sprite_list[0].center_x = view_left + 500
        self.clue_sprite_list[0].center_y = view_bottom + 350


    def draw_clue(self):
        if self.show_question:
            self.clue_sprite_list.draw()
            newline = 20
            for x in self.questions:
                arcade.draw_text(x, self.clue_sprite_list[0].center_x - 200,
                                 self.clue_sprite_list[0].center_y + 100 - newline,
                                 arcade.csscolor.WHITE, 15)
                newline += 20
            arcade.draw_text("Press Enter to close the clue.", self.clue_sprite_list[0].center_x - 300,
                             self.clue_sprite_list[0].center_y - 200,
                             arcade.csscolor.WHITE, 18)
        if self.show_clue:
            words_in_clue = [wrd for wrd in self.clues[self.clue_pos].split()]
            line1 = ''
            line2 = ''
            line3 = ''
            line4 = ''
            for x in range (0, len(words_in_clue)):
                if x <= 3:
                    line1 += words_in_clue[x]
                    line1 += ' '
                elif x <= 7:
                    line2 += words_in_clue[x]
                    line2 += ' '
                elif x <= 11:
                    line3 += words_in_clue[x]
                    line3 += ' '
                elif x <= 15:
                    line4 += words_in_clue[x]
                    line4 += ' '
            self.clue_sprite_list.draw()

            #arcade.draw_text(self.clues[self.clue_pos], self.clue_sprite_list[0].center_x - 300, self.clue_sprite_list[0].center_y,
            #arcade.csscolor.WHITE, 16)
            #arcade.draw_text("Press Enter to close the clue.", self.clue_sprite_list[0].center_x - 275, self.clue_sprite_list[0].center_y - 200,

            arcade.draw_text(line1, self.clue_sprite_list[0].center_x - 220, self.clue_sprite_list[0].center_y + 70,
            arcade.csscolor.WHITE, 18)
            arcade.draw_text(line2, self.clue_sprite_list[0].center_x - 220, self.clue_sprite_list[0].center_y + 40,
            arcade.csscolor.WHITE, 18)
            arcade.draw_text(line3, self.clue_sprite_list[0].center_x - 220, self.clue_sprite_list[0].center_y + 10,
            arcade.csscolor.WHITE, 18)
            arcade.draw_text(line4, self.clue_sprite_list[0].center_x - 220, self.clue_sprite_list[0].center_y - 20,
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

    def exit_question(self):
        if self.show_question:
            self.show_question = False

    def get_clue(self):
        return self.clues[self.clue_pos]

