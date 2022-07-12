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
        self.pokemon_level = 50

        team1,team2 = self.setup_teams()
        self.current_pokemon = team1[0]
        self.current_opp_pokemon = team2[0]
        print(self.current_pokemon)
        print(self.current_pokemon['moves'][0])
        print(self.current_pokemon['moves'][0][0])
        print(self.current_pokemon['moves'][0][0][0])
        print(self.update_health(self.current_pokemon, self.current_opp_pokemon, self.pokemon_level, self.current_pokemon['moves'][0][1][0]))
        print(self.current_opp_pokemon)
        self.change_current_pokemon(self.current_pokemon)
        self.change_current_pokemon_opp(self.current_opp_pokemon)
        self.change_switch_pokemon_labels(team1)
    
    def add_moves_to_team(self,team):
        for pokemon in team:
            pokemon['moves'].append(make_moves(pokemon['type'],"moves.csv"))
        return team

    def change_current_pokemon(self,pokemon):
        self.window.options_ask_start['text'] = f"What will\n{pokemon['name']} do?"
        self.change_move_labels(self.current_pokemon['moves'][0])

        self.window.player_hp_name['text'] = f"{pokemon['name']}"
        self.change_pokemon_img("pokemon_pngs",pokemon['name'])
    
    def change_current_pokemon_opp(self,pokemon):
        self.window.opp_hp_name['text'] = f"{pokemon['name']}"
        self.change_pokemon_img_opp("pokemon_pngs",self.current_opp_pokemon['name'])

    
    def change_pokemon_img(self,folder,pokemon):
        ''' Detect the pokemon, then adds it with the appropiate image sprite '''
        filename = f"{pokemon}_back.png"
        pokemon_image = os.path.join(folder, filename)
        image = Image.open(pokemon_image)
        image = image.resize((300,300), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        self.window.pokemon_player_img['image'] = image
        self.window.pokemon_player_img['bg'] = None
        self.window.pokemon_player_img.image = image
        pokemon_player_waist_up = image.height() / 1.5
        self.window.pokemon_player_img.place(x=MENU_CENTERX/4, y=BOTTOM_BARY_TOP-pokemon_player_waist_up)
        


    def change_pokemon_img_opp(self,folder,pokemon):
        ''' Detect the pokemon, then adds it with the appropiate image sprite '''
        filename = f"{pokemon}.png"
        pokemon_image = os.path.join(folder, filename)
        image = Image.open(pokemon_image)
        image = image.resize((200,200), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        self.window.pokemon_opp_img['image'] = image
        self.window.pokemon_opp_img['bg'] = None
        self.window.pokemon_opp_img.image = image
        self.window.pokemon_opp_img.place(x=MENU_CENTERX*1.30, y=MENU_CENTERY*0.1)

    def change_move_labels(self,moves):
        self.window.move1['text'] = moves[0][0]['name']
        self.window.move2['text'] = moves[1][0]['name']
        self.window.move3['text'] = moves[2][0]['name']
        self.window.move4['text'] = moves[3][0]['name']

    def change_switch_pokemon_labels(self,team):
        self.window.Pokemon1['text'] = team[0]['name']
        self.window.Pokemon2['text'] = team[1]['name']
        self.window.Pokemon3['text'] = team[2]['name']
        self.window.Pokemon4['text'] = team[3]['name']
        self.window.Pokemon5['text'] = ""
        self.window.Pokemon6['text'] = ""

    def setup_teams(self):
        team_1,team_2 = create_teams("pokemon.csv")
        team_1 = self.add_moves_to_team(team_1)
        team_2 = self.add_moves_to_team(team_2)
        return team_1,team_2

    def update_health(self, attacker, defender, attacker_level, chosen_move):
        multiplier = get_multiplier('multipler.csv',attacker['type'],defender['type'])
        new_damage = determine_damage(multiplier, attacker_level, attacker['moves'][0][0], attacker['attack'], attacker['defence'])
        return new_damage
        


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



    

    def setting_up_buttons(self):
        self.window.fight_button['command'] = self.test
        self.window.bag_button['command'] = self.test
        self.window.switch_button['command'] = self.test
        self.window.run_button['command'] = self.test

        self.window.fight_button['command'] = self.window.place_moves_GUI
        self.window.switch_button['command'] = self.window.place_switch_gui


        # self.window.move1_button['command'] =
        # self.window.move2_button['command'] =
        # self.window.move3_button['command'] =
        # self.window.move4_button['command'] =

        self.window.run_button['command'] = self.window.root.destroy


if __name__ == "__main__":
    menu = ""#menu we havent created
    game = Main()
    game.window.root.mainloop()