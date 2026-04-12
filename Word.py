
import pyxel #type:ignore
from faker import Faker #type:ignore

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
        self.fake = Faker('en_US')

    # 英語の単語を出したいので 'en_US' を指定
    

    def get_target_word(self,game_level):
        # 条件に合う単語が出るまで繰り返す
        while True:            
            # 難易度に合わせて文字数をチェックして、条件に合えば返す
            if game_level == "easy":
                word = self.fake.word().lower()
                if len(word) <= self.word_len_max:
                    return word
            elif game_level == "normal":
                word = self.fake.text.lower()
                if len(word) <= self.word_len_max:
                    return word
            elif game_level == "hard":
                word = self.fake.text(max_nb_chars=20).lower()
                return word
            else:
                word = self.fake.text(max_nb_chars=30).lower()
                return word

    def generate_new_word(self, game_level):
        self.keyword = self.get_target_word(game_level)

    
    def draw(self):
        pyxel.text(pyxel.width//5, pyxel.height//2-20,self.keyword,pyxel.COLOR_WHITE)
