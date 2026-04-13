import pyxel #type:ignore

# update

def update_menu_scene(self):
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        mx = pyxel.mouse_x
        my = pyxel.mouse_y
        
        # x座標が文字の範囲内か（ざっくり width//3 から +40 ピクセルくらいまで）
        if pyxel.width//3 <= mx <= pyxel.width//3 + 40:
            
            # y座標でどの難易度をクリックしたか判定
            if pyxel.height//10 + 40 <= my <= pyxel.height//10 + 50:
                self.game_level = self.EASY
                self.current_scene = self.START_SCENE
                
            elif pyxel.height//10 + 60 <= my <= pyxel.height//10 + 70:
                self.game_level = self.NORMAL
                self.current_scene = self.START_SCENE
                
            elif pyxel.height//10 + 80 <= my <= pyxel.height//10 + 90:
                self.game_level = self.HARD
                self.current_scene = self.START_SCENE

        if pyxel.width//10 <= pyxel.mouse_x <= pyxel.width//2 and pyxel.height//10  <= pyxel.mouse_y <= pyxel.height//10 + 5:
                self.game_level = self.HELL
                self.current_scene = self.START_SCENE

        if 4 <= pyxel.mouse_x <= 13 and 13 <= pyxel.mouse_y <= 21:
                self.current_scene = self.MENU_SCENE
            # ESCAPEボタンのクリック判定（elifをここに入れる）
        elif pyxel.width-6 <= pyxel.mouse_x <= pyxel.width and 2 <= pyxel.mouse_y <= 10:
                pyxel.quit()


def update_start_scene(self):
    if self.current_scene == self.START_SCENE:
        
        # クリック判定をひとまとめにする
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            # MENUボタンのクリック判定
            if 4 <= pyxel.mouse_x <= 13 and 4 <= pyxel.mouse_y <= 13: 
                self.current_scene = self.MENU_SCENE
            # ESCAPEボタンのクリック判定（elifをここに入れる）
            elif pyxel.width-6 <= pyxel.mouse_x <= pyxel.width and 2 <= pyxel.mouse_y <= 10:
                pyxel.quit()

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.word_manager.generate_new_word(self.game_level)
            self.score = 0
            self.keyboard.keyword = ""
            self.game_finish = False 
            self.game_timer = self.GAME_DISPLAY_TIME # もし前回1800に直していたらそっちに合わせてね
            self.current_scene = self.PLAY_SCENE

def update_play_scene(self):
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        # MENUボタンがクリックされた場合
        if 4 <= pyxel.mouse_x <= 13 and 4 <= pyxel.mouse_y <= 13: 
            self.current_scene = self.MENU_SCENE
        # ESCAPEボタンがクリックされた場合
        elif pyxel.width-6 <= pyxel.mouse_x <= pyxel.width and 2 <= pyxel.mouse_y <= 10:
            pyxel.quit()
            
    if self.game_finish:
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.current_scene = self.MENU_SCENE
        return 


    # まだゲーム中ならタイマーを減らす
    self.game_timer -= 1
    # タイマーが0になったら終了フラグを立てて、そのフレームの処理を終わる
    if self.game_timer <= 0:
        self.game_finish = True
        return

    self.keyboard.update()
    if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_KP_ENTER):
        if self.keyboard.keyword == self.word_manager.keyword:
            self.score += 1                                      # 1. スコアを加算
            self.word_manager.generate_new_word(self.game_level) # 2. 次のお題を生成
            self.keyboard.keyword = ""                           # 3. 入力した文字を空っぽに戻す
        # 違っていたら何もしない（そのまま打たせ続ける）
    

# draw
def draw_menu_scene(self):
    pyxel.cls(pyxel.COLOR_DARK_BLUE)
    pyxel.blt(1,2,0,56,2,8,7,pyxel.COLOR_BLACK) #MENUのアイコン
    pyxel.blt(pyxel.width-6,2,0,48,0,5,8,pyxel.COLOR_BLACK) #ESCAPEのアイコン
    pyxel.text(pyxel.width//10, pyxel.height//10, "CLICK TO START", pyxel.COLOR_WHITE)
    pyxel.text(pyxel.width//3+10, pyxel.height//10 + 40, "EASY", pyxel.COLOR_YELLOW)
    pyxel.text(pyxel.width//3+10, pyxel.height//10 + 60, "NORMAL", pyxel.COLOR_WHITE)
    pyxel.text(pyxel.width//3+10, pyxel.height//10 + 80, "HARD", pyxel.COLOR_RED)

def draw_start_scene(self):
    pyxel.cls(pyxel.COLOR_BLACK) 
    mode_text = f"MODE: {self.game_level.upper()}"
    pyxel.text(pyxel.width//10, pyxel.height//10, mode_text, pyxel.COLOR_YELLOW)
    pyxel.blt(1,2,0,56,2,8,7,pyxel.COLOR_BLACK) #MENUのアイコン
    pyxel.blt(pyxel.width-6,2,0,48,0,5,8,pyxel.COLOR_BLACK) #ESCAPEのアイコン
    pyxel.text(pyxel.width//10, pyxel.height//10 + 20, "SPACE TO START", pyxel.COLOR_WHITE)


def draw_play_scene(self):
    pyxel.cls(pyxel.COLOR_BLACK)
    pyxel.blt(1,2,0,56,2,8,7,pyxel.COLOR_WHITE) #MENUのアイコン
    pyxel.blt(pyxel.width-6,2,0,48,0,5,8,pyxel.COLOR_BLACK) #ESCAPEのアイコン
    if self.game_finish:
        # FINISH画面の描画
        pyxel.text(pyxel.width//2 - 15, pyxel.height//2 - 20, "FINISH!", pyxel.COLOR_RED)
        pyxel.text(pyxel.width//2 - 18, pyxel.height//2 , f"SCORE: {self.score}", pyxel.COLOR_YELLOW)
        pyxel.text(pyxel.width//2 - 40, pyxel.height//2 + 10, "PRESS SPACE TO MENU", pyxel.COLOR_WHITE)

    else:
        pyxel.text(5, 5, f"TIME: {self.game_timer // 30}", pyxel.COLOR_WHITE)
        pyxel.text(pyxel.width//10, pyxel.height//10, "PLAYING...", pyxel.COLOR_WHITE)
        pyxel.text(pyxel.width - 50, pyxel.height//10, f"SCORE: {self.score}", pyxel.COLOR_GREEN)
        self.word_manager.draw()
        input_text = f"INPUT: {self.keyboard.keyword}"
        pyxel.text(4, pyxel.height//2, input_text, pyxel.COLOR_YELLOW)
