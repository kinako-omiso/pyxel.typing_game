import pyxel #type:ignore
class Key_input:
    Alphabet={pyxel.KEY_A:"A", pyxel.KEY_B:"B", pyxel.KEY_C:"C", pyxel.KEY_D:"D", pyxel.KEY_E:"E", pyxel.KEY_F:"F", pyxel.KEY_G:"G", 
              pyxel.KEY_H:"H", pyxel.KEY_I:"I", pyxel.KEY_J:"J", pyxel.KEY_K:"K", pyxel.KEY_L:"L", pyxel.KEY_M:"M", pyxel.KEY_N:"N",
              pyxel.KEY_O:"O", pyxel.KEY_P:"P", pyxel.KEY_Q:"Q", pyxel.KEY_R:"R", pyxel.KEY_S:"S", pyxel.KEY_T:"T", pyxel.KEY_U:"U",
              pyxel.KEY_V:"V", pyxel.KEY_W:"W", pyxel.KEY_X:"X", pyxel.KEY_Y:"Y", pyxel.KEY_Z:"Z",pyxel.KEY_0:"0", pyxel.KEY_1:"1", pyxel.KEY_2:"2", pyxel.KEY_3:"3", pyxel.KEY_4:"4", pyxel.KEY_5:"5", pyxel.KEY_6:"6", 
              pyxel.KEY_7:"7", pyxel.KEY_8:"8", pyxel.KEY_9:"9",pyxel.KEY_UNDERSCORE:"_",pyxel.KEY_EQUALS:"=",pyxel.KEY_SPACE:" "}

    def __init__(self):
        self.keyword = ""

    def update(self):
        for key in self.Alphabet :  # キーコードの範囲
            if pyxel.btnp(key):
                self.keyword += self.Alphabet[key]
        if pyxel.btnp(pyxel.KEY_BACKSPACE):
            self.keyword = self.keyword[:-1]
