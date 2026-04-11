
import pyxel #type:ignore

class Key_word:
    def __init__(self,game_level):
        self.keyword = ""
        if game_level == "easy":
            self.word_len_max = 10
        elif game_level == "normal":
            self.word_len_max = 20
        elif game_level == "hard":
            self.word_len_max = 30
        else:
            self.word_len_max = 50

    def update(self):
        pass
    
    def draw(self):
        pass
