from tkinter import *
from tkinter.font import BOLD, Font
from Move_class import *
from Pokemon_class import *
from Fight_class import *
from Player_class import *
from Window_class import *
import random
import os
from PIL import Image, ImageTk

class Main:

    def __init__(self):
        self.window = Window()
        self.setting_up_buttons()
        self.setting_up_mouse_hover()

        team1,team2 = self.setup_teams()
        current_pokemon = team1[0]
        current_opp_pokemon = team2[0]
        self.change_current_pokemon_label(current_pokemon)
        self.change_pokemon_img("pokemon_pngs",current_pokemon['name'])

    
    def add_moves_to_team(self,team):
        for pokemon in team:
            pokemon['moves'].append(make_moves(pokemon['type'],"moves.csv"))
        return team

    def change_current_pokemon_label(self,pokemon):
        self.window.options_ask_start['text'] = f"What will\n{pokemon['name']} do?"
    
    def change_pokemon_img(self,folder,pokemon):
        ''' Detect the pokemon, then adds it with the appropiate image sprite '''
        filename = f"{pokemon}_back.png"
        pokemon_image = os.path.join(folder, filename)
        image = Image.open(pokemon_image)
        image.resize((20,20), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        self.window.pokemon_player_img['image'] = image
        self.window.pokemon_player_img['bg'] = None


    def setup_teams(self):
        team_1,team_2 = create_teams("pokemon.csv")
        team_1 = self.add_moves_to_team(team_1)
        team_2 = self.add_moves_to_team(team_2)
        return team_1,team_2

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
        self.window.run_button['command'] = self.window.root.destroy

if __name__ == "__main__":
    menu = ""#menu we havent created
    game = Main()
    game.window.root.mainloop()