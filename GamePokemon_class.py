from tkinter import *
from tkinter.font import Font
from Move_class import *
from Pokemon_class import *
from Fight_class import *
from Player_class import *
import random

MENU_WIDTH = 1024
MENU_HEIGHT = 576

class GamePokemon:

    def __init__(self):
        self.root = Tk()
        self.root.geometry(f"{MENU_WIDTH}x{MENU_HEIGHT}")
        self.root.title("The Randomized Shiny Pokemon Showdown!")
        self.root.resizable(False,False)

        self.setup()

    def get_root(self):
        return self.root

    def get_pokemon(self):
        return self.pokemon

    def get_run_button(self):
        return self.run_button

    def get_fight_button(self):
        return self.fight_button
    
    def get_switch_button(self):
        return self.switch_button

    def get_pokemon_name(self):
        return self.pokemon_name

    def get_pokemon_hp(self):
        return self.pokemon_hp

    def get_bag_button(self):
        return self.bag_button

    def get_pokemon_remaining(self):
        return self.pokemon_remaining
    
    def test(self):
        COLORS = ["red", "green", "blue", "yellow"]
        example = Label(self.root, text="test", background=random.choice(COLORS))
        example.place(x=MENU_WIDTH-50, y=MENU_HEIGHT-50, width=50, height=50)
        

    
    def setup(self): # Change to use place() instead of grid()
        '''Create all of the widgets for the menu.'''
        self.font = Font(family="Helvetica", size=20)

        self.pokemon = Label(self.root)
        self.pokemon.grid(row=0, column=0, columnspan=2)

        self.run_button = Button(self.root, text="Run", font=self.font, command=self.test)
        self.run_button.grid(row=1, column=0)

        self.fight_button = Button(self.root, text="Fight", font=self.font, command=self.test)
        self.fight_button.grid(row=1, column=1)

        self.switch_button = Button(self.root, text="Switch", font=self.font, command=self.test)
        self.switch_button.grid(row=2, column=0)

        self.pokemon_name = Label(self.root, text="dog",font=self.font) # Insert pokemon name variable
        self.pokemon_name.grid(row=2, column=1)

        self.pokemon_hp = Frame(self.root)
        self.pokemon_hp.grid(row=3, column=0)

        self.bag_button = Button(self.root, text="Bag", font=self.font, command=self.test)
        self.bag_button.grid(row=3, column=1)

        self.pokemon_remaining = Frame(self.root)
        self.pokemon_remaining.grid(row=4, column=0)


if __name__ == '__main__':
    window = GamePokemon()
    window.root.mainloop()
