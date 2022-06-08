from tkinter import *
from tkinter.font import Font
from Move_class import *
from Pokemon_class import *
from Fight_class import *
from Player_class import *
import random


MENU_WIDTH = 1024
MENU_HEIGHT = 576
MENU_CENTERX = MENU_WIDTH / 2
MENU_CENTERY = MENU_HEIGHT / 2
BOTTOM_OPTIONS = MENU_HEIGHT / 4


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
        example.place(x=0, y=0, width=50, height=50)
        

    
    def setup(self): # Change to use place() instead of grid(). Also origin is top left corner
        '''Create all of the widgets for the menu.'''
        self.font = Font(family="Helvetica", size=20)

        self.pokemon = Label(self.root)
        self.pokemon.place(x=MENU_CENTERX/2,y=BOTTOM_OPTIONS)

        self.fight_button = Button(self.root, text="Fight", font=self.font, command=self.test)
        self.fight_button.place(x=MENU_CENTERX,y=BOTTOM_OPTIONS*0.9,width=MENU_CENTERX/4,height=BOTTOM_OPTIONS/4)

        self.bag_button = Button(self.root, text="Bag", font=self.font, command=self.test)
        self.bag_button.place(x=MENU_CENTERX*1.8,y=BOTTOM_OPTIONS*0.9,width=MENU_CENTERX/4,height=BOTTOM_OPTIONS/4)

        self.switch_button = Button(self.root, text="Switch", font=self.font, command=self.test)
        self.switch_button.place(x=MENU_CENTERX,y=BOTTOM_OPTIONS-(BOTTOM_OPTIONS/4),width=MENU_CENTERX/4,height=BOTTOM_OPTIONS/4)

        self.run_button = Button(self.root, text="Run", font=self.font, command=self.test)
        self.run_button.place(x=MENU_CENTERX*1.8,y=BOTTOM_OPTIONS-(BOTTOM_OPTIONS/4),width=MENU_CENTERX/4,height=BOTTOM_OPTIONS/4)

        self.pokemon_name = Label(self.root, text="placeholder",font=self.font) # Insert pokemon name variable
        self.pokemon_name.place(x=MENU_CENTERX*1.2,y=BOTTOM_OPTIONS*1.5,width=MENU_CENTERX/4,height=BOTTOM_OPTIONS/4)


        '''self.pokemon_hp = Frame(self.root)
        self.pokemon_hp.grid(row=3, column=0)

        self.pokemon_remaining = Frame(self.root)
        self.pokemon_remaining.grid(row=4, column=0)'''


if __name__ == '__main__':
    window = GamePokemon()
    window.root.mainloop()
