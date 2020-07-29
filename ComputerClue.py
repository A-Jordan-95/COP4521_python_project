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
            self.clue_sprite_list.draw()
            arcade.draw_text(self.clues[self.clue_pos], self.clue_sprite_list[0].center_x - 300, self.clue_sprite_list[0].center_y,
            arcade.csscolor.WHITE, 16)
            arcade.draw_text("Press Enter to close the clue.", self.clue_sprite_list[0].center_x - 275, self.clue_sprite_list[0].center_y - 200,
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

