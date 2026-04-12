import pyxel #type:ignore
class Key_input:
    Alphabet={pyxel.KEY_A:"a", pyxel.KEY_B:"b", pyxel.KEY_C:"c", pyxel.KEY_D:"d", pyxel.KEY_E:"e", pyxel.KEY_F:"f", pyxel.KEY_G:"g", 
              pyxel.KEY_H:"h", pyxel.KEY_I:"i", pyxel.KEY_J:"j", pyxel.KEY_K:"k", pyxel.KEY_L:"l", pyxel.KEY_M:"m", pyxel.KEY_N:"n",
              pyxel.KEY_O:"o", pyxel.KEY_P:"p", pyxel.KEY_Q:"q", pyxel.KEY_R:"r", pyxel.KEY_S:"s", pyxel.KEY_T:"t", pyxel.KEY_U:"u",
              pyxel.KEY_V:"v", pyxel.KEY_W:"w", pyxel.KEY_X:"x", pyxel.KEY_Y:"y", pyxel.KEY_Z:"z",pyxel.KEY_0:"0", pyxel.KEY_1:"1", pyxel.KEY_2:"2", pyxel.KEY_3:"3", pyxel.KEY_4:"4", pyxel.KEY_5:"5", pyxel.KEY_6:"6", 
              pyxel.KEY_7:"7", pyxel.KEY_8:"8", pyxel.KEY_9:"9",pyxel.KEY_UNDERSCORE:"_",pyxel.KEY_EQUALS:"=",pyxel.KEY_SPACE:" ",pyxel.KEY_COMMA:",",pyxel.KEY_PERIOD:"."}

    def __init__(self):
        self.keyword = ""

    def update(self):
        for key in self.Alphabet :  # キーコードの範囲
            if pyxel.btnp(key):
                self.keyword += self.Alphabet[key]
        if pyxel.btnp(pyxel.KEY_BACKSPACE):
            self.keyword = self.keyword[:-1]
