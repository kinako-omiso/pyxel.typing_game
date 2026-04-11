import pyxel #type:ignore
import funtion

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256
START_SCENE= "START"
PLAY_SCENE = "PLAY"

class App:
    def __input__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="typing_game")
        pyxel.mouse(True)
        self.current_scene = START_SCENE
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if self.current_scene == START_SCENE:
            function.update_start_scene()
        else:
            function.update_game_scene()

        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

