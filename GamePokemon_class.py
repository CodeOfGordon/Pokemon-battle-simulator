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
        self.setting_up_mouse_hover()
        self.setup_teams()
    
    def add_moves_to_team(self,team):
        for pokemon in team:
            pokemon[0]['moves'].append(make_moves(pokemon[0]['type'],"moves.csv"))

    def setup_teams(self):
        team_1,team_2 = create_teams("pokemon.csv")
        team_1 = self.add_moves_to_team(team_1)
        team_2 = self.add_moves_to_team(team_2)
    
    #def get_current_pokemon(self):

    def test(self):
        COLORS = ["red", "green", "blue", "yellow"]
        example = Label(self.window.root, text="test", background=random.choice(COLORS))
        example.place(x=0, y=0, width=50, height=50)

    def mouse_hover_change(self, button, oldtext):
        '''Change the text of the button when the mouse is over it.'''
        button.bind("<Enter>", lambda e: button.config(text="➤ " + oldtext))
        button.bind("<Leave>", lambda e: button.config(text=oldtext))

    def setting_up_mouse_hover(self):
        self.mouse_hover_change(self.window.fight_button, "Fight")
        self.mouse_hover_change(self.window.bag_button, "Bag")
        self.window.bag_button["state"] = DISABLED
        self.mouse_hover_change(self.window.switch_button, "Switch")
        self.mouse_hover_change(self.window.run_button, "Run")


    def exit_current_GUI(self):
        
        self.window.root.destroy()
    

    def open_moves_gui(self):
        self.window.moves_GUI

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

        self.window.switch_button['command'] = self.window.switch_GUI

if __name__ == "__main__":
    menu = ""#menu we havent created
    game = Main()
    game.window.root.mainloop()