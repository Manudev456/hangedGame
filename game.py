from random import *

class game:
    id    = int
    hp    = int
    score = int
    level = int
    state = bool
    word = str
    
    def __init__(self, id, level):
        self.id = id
        self.level = level
        if self.level == 1:
            self.hp = 8
        elif self.level == 2:
            self.hp = 6
        elif self.level == 3:
            self.hp = 4
        self.score = 0
        self.state = False
        self.word =  with open("./data_base.txt", "r", encoding= "utf-8") as data:
                        data_base = [line.strip("\n") for line in data]
                        self.word = data_base[randint(0, len(data_base))]

    def star(self):
        self.state = True
    def end(self):
        self.state = False
    # def get_word(self):
    #     with open("./data_base.txt", "r", encoding= "utf-8") as data:
    #         data_base = [line.strip("\n") for line in data]
    #         word = data_base[randint(0, len(data_base))]
    #     return word