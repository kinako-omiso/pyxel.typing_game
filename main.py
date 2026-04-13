import pyxel #type:ignore
import Key
import function
import Word

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 128

EASY = "easy"
NORMAL = "normal"
HARD = "hard"
HELL = "hell"

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="typing_game")
        pyxel.load("my_resource.pyxres")
        pyxel.mouse(True)
        self.START_SCENE= "START"
        self.PLAY_SCENE = "PLAY"
        self.MENU_SCENE = "MENU"
        self.HELL_SCENE = "HELL"
        self.current_scene = self.MENU_SCENE
        self.game_level = EASY
        self.EASY = EASY
        self.NORMAL = NORMAL
        self.HARD = HARD
        self.HELL = HELL
        self.score = 0
        self.GAME_DISPLAY_TIME = 1800
        self.game_timer = self.GAME_DISPLAY_TIME
        self.game_finish = False
        self.keyboard = Key.Key_input()
        self.word_manager = Word.Key_word(self.game_level)

        pyxel.run(self.update, self.draw)

    
    def update(self):
        if self.current_scene == self.MENU_SCENE:
            function.update_menu_scene(self)
        elif self.current_scene == self.START_SCENE:
            function.update_start_scene(self)
        else:
            function.update_play_scene(self)

        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        if self.current_scene == self.MENU_SCENE:
            function.draw_menu_scene(self)
        elif self.current_scene == self.START_SCENE:
            function.draw_start_scene(self)
        elif self.current_scene == self.PLAY_SCENE:
            function.draw_play_scene(self)

App()