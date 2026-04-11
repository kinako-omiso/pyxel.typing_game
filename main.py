import pyxel #type:ignore
import function

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256
START_SCENE= "START"
PLAY_SCENE = "PLAY"
MENU_SCENE = "MENU"

class App:
    def __input__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="typing_game")
        pyxel.mouse(True)
        self.current_scene = START_SCENE
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if self.current_scene == MENU_SCENE:
            function.update_menu_scene(self)
        elif self.current_scene == START_SCENE:
            function.update_start_scene(self)
        else:
            function.update_game_scene(self)

        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        if self.current_scene == MENU_SCENE:
            function.draw_menu_scene(self)
        elif self.current_scene == START_SCENE:
            function.draw_start_scene(self)
        elif self.current_scene == PLAY_SCENE:
            function.draw_play_scene(self)

#class keyword: