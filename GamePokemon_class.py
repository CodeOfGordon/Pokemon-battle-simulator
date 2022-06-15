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
        self.setting_up_buttons()
    
    def test(self):
        COLORS = ["red", "green", "blue", "yellow"]
        example = Label(self.window.root, text="test", background=random.choice(COLORS))
        example.place(x=0, y=0, width=50, height=50)

    def setting_up_buttons(self):
        self.window.fight_button['command'] = self.test
        self.window.bag_button['command'] = self.test
        self.window.switch_button['command'] = self.test
        self.window.run_button['command'] = self.test

        self.window.fight_button['command'] = self.window.moves_GUI
        # self.window.move1_button['command'] =
        # self.window.move2_button['command'] =
        # self.window.move3_button['command'] =
        # self.window.move4_button['command'] =

if __name__ == "__main__":
    menu = ""#menu we havent created
    game = Main()
    game.window.root.mainloop()