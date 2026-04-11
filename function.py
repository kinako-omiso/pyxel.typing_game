import pyxel #type:ignore

# update
def update_reset_play_scene(self):
    pass

def update_menu_scene(self):
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        mx = pyxel.mouse_x
        my = pyxel.mouse_y
        
        # x座標が文字の範囲内か（ざっくり width//3 から +40 ピクセルくらいまで）
        if pyxel.width//3 <= mx <= pyxel.width//3 + 40:
            
            # y座標でどの難易度をクリックしたか判定
            if pyxel.height//10 + 40 <= my <= pyxel.height//10 + 50:
                self.game_mode = self.EASY
                self.current_scene = self.START_SCENE
                
            elif pyxel.height//10 + 60 <= my <= pyxel.height//10 + 70:
                self.game_mode = self.NORMAL
                self.current_scene = self.START_SCENE
                
            elif pyxel.height//10 + 80 <= my <= pyxel.height//10 + 90:
                self.game_mode = self.HARD
                self.current_scene = self.START_SCENE

def update_start_scene(self):
    if self.current_scene == self.START_SCENE:
        if pyxel.btnp(pyxel.KEY_SPACE):
            update_reset_play_scene(self)
            self.current_scene = self.PLAY_SCENE

def update_play_scene(self):
    self.keyboard.update()

# draw
def draw_menu_scene(self):
    pyxel.cls(pyxel.COLOR_DARK_BLUE)
    pyxel.text(pyxel.width//10, pyxel.height//10, "CLICK TO START", pyxel.COLOR_WHITE)
    pyxel.text(pyxel.width//3+10, pyxel.height//10 + 40, "EASY", pyxel.COLOR_YELLOW)
    pyxel.text(pyxel.width//3+10, pyxel.height//10 + 60, "NORMAL", pyxel.COLOR_WHITE)
    pyxel.text(pyxel.width//3+10, pyxel.height//10 + 80, "HARD", pyxel.COLOR_RED)

def draw_start_scene(self):
    pyxel.cls(pyxel.COLOR_BLACK) 
    mode_text = f"MODE: {self.game_mode.upper()}"
    pyxel.text(pyxel.width//10, pyxel.height//10, mode_text, pyxel.COLOR_YELLOW)
    
    pyxel.text(pyxel.width//10, pyxel.height//10 + 20, "SPACE TO START", pyxel.COLOR_WHITE)

def draw_play_scene(self):
    pyxel.cls(pyxel.COLOR_BLACK)
    pyxel.text(pyxel.width//10, pyxel.height//10, "PLAYING...", pyxel.COLOR_WHITE)
    
    input_text = f"INPUT: {self.keyboard.keyword}"
    pyxel.text(pyxel.width//10, pyxel.height//2, input_text, pyxel.COLOR_YELLOW)
