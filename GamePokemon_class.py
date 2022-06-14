from tkinter import *
from tkinter.font import BOLD, Font
from Move_class import *
from Pokemon_class import *
from Fight_class import *
from Player_class import *
from Window_class import *
import random
from PIL import Image, ImageTk

class Main:

    def __init__(self):
        self.window = Window()

    def setting_up_buttons(self):
        fight_button = self.window.fight_button()
        fight_button['command'] = self.window.moves_GUI

if __name__ == "__main__":
    menu = ""#menu we havent created
    game = Main()
    game.window.root.mainloop()