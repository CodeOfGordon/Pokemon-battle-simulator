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

    def open_moves_gui(self):
        self.window.moves_GUI

    def setting_up_buttons(self):
        fight_button = self.window.fight_button()
        fight_button['command'] = lambda self = self : self.open_moves_gui()

    def activate_buttons(self):
        fight_button = self.window.fight_button()
        fight_button['state'] = NORMAL

if __name__ == "__main__":
    menu = ""#menu we havent created
    game = Main()
    game.window.root.mainloop()