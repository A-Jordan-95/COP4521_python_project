class QuestionCreation(object):
    def __init__(self):
        super().__init__()
        self.masterList = []
        self.questions = []
        self.clues = []
        self.answers = []

    def replacedelim(self, text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text

    def createlist(self):
        lines = []
        with open("questions/questions.txt") as file:
            lines = [line.rstrip()
                         .split("Q1:, Q2:, Q3:, Q4:, Q5:, Cl1:, Cl2:, Cl3:, Cl4:, A:, W1:, W2:, W3:, W4:")
                     for line in file]

        remove_empty = []

        for string in lines:
            for x in string:
                if(len(x) != 0):
                    remove_empty.append(string)
        d = {"Q1: ": "", "Q2: ": "", "Q3: ": "", "Q4: ": "", "Q5: ": "", "Cl1: ": "",
             "Cl2: ": "", "Cl3: ": "", "Cl4: ": "", "A: ": "", "W1: ": "", "W2: ": "", "W3: ": "", "W4: ": ""}

        RemoveText = []
        for string in remove_empty:
            for x in string:
                RemoveText.append(self.replacedelim(x, d))

        question1 = []
        question2 = []
        question3 = []
        question4 = []
        question5 = []
        counter = 1

        for x in RemoveText:
            if counter < 15:
                question1.append(x)
            elif counter < 29:
                question2.append(x)
            elif counter < 48:
                question3.append(x)
            elif counter < 62:
                question4.append(x)
            else:
                question5.append(x)
            counter += 1
        self.masterList = [question1, question2, question3, question4, question5]

    def splitQuestions(self, level):
        if level == 0:
            return [6, 10, 14]
        if level == 1:
            return [6, 10, 14]
        if level == 2:
            return [11, 15, 19]
        if level == 3:
            return [6, 10, 14]
        return [13, 17, 21]


    def createQuestions(self):
        for level in range (0, 5):
            counter = 0
            q = []
            c = []
            a = []
            lineParse = self.splitQuestions(level)
            for x in self.masterList[level]:
                if counter < lineParse[0]:
                    q.append(x)
                elif counter < lineParse[1]:
                    c.append(x)
                elif counter < lineParse[2]:
                    a.append(x)
                counter += 1
            self.questions.append(q)
            self.clues.append(c)
            self.answers.append(a)


