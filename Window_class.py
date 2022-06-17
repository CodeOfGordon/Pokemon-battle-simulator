from tkinter import *
from tkinter.font import BOLD, Font
from Move_class import *
from Pokemon_class import *
from Fight_class import *
from Player_class import *
import random
from PIL import Image, ImageTk


MENU_WIDTH = 953
MENU_HEIGHT = 528+175
MENU_CENTERX = MENU_WIDTH / 2
MENU_CENTERY = MENU_HEIGHT / 2
BOTTOM_BARY = MENU_CENTERY * 0.75
TOP_BOTTOM_FRAME = SIDE_FRAME = BOTTOM_BARY * 0.05
BOTTOM_BARY_TOP = MENU_HEIGHT-BOTTOM_BARY

class Window:

    def __init__(self):
        self.root = Tk()
        self.root.geometry(f"{MENU_WIDTH}x{MENU_HEIGHT}")
        self.root.title("The Randomized Shiny Pokemon Showdown!")
        self.root.resizable(False,False)

        self.setup()

    def get_root(self):
        return self.root

    def get_pokemon_op(self):
        return self.pokemon_op
    
    def get_pokemon_pl(self):
        return self.pokemon_pl

    def get_pokemon_name_op(self):
        return self.pokemon_name_op

    def get_pokemon_name_pl(self):
        return self.pokemon_name_pl

    def get_pokemon_hp_op(self):
        return self.pokemon_hp_op

    def get_pokemon_hp_pl(self):
        return self.pokemon_hp_pl

    def get_pokemon_remaining_op(self):
        return self.pokemon_remaining_op

    def get_pokemon_remaining_pl(self):
        return self.pokemon_remaining_pl
    

    def moves_GUI(self):
        '''Create the GUI for the moves.'''
        OPTIONS_MOVES_FRAME_WIDTH = MENU_WIDTH-(2*SIDE_FRAME)
        OPTIONS_MOVES_FRAME_HEIGHT = (BOTTOM_BARY)-(2*TOP_BOTTOM_FRAME*0.75)

        self.moves_frame = Frame(self.root, bg="white")
        self.moves_frame.place(x=SIDE_FRAME, y=BOTTOM_BARY_TOP+TOP_BOTTOM_FRAME, width=OPTIONS_MOVES_FRAME_WIDTH, height=OPTIONS_MOVES_FRAME_HEIGHT)

        self.move1 = Button(self.moves_frame, text="move1", font=self.font, justify=LEFT)
        self.move1.place(x=0,y=0,width=OPTIONS_MOVES_FRAME_WIDTH/2,height=OPTIONS_MOVES_FRAME_HEIGHT/2)

        self.move2 = Button(self.moves_frame, text="move2", font=self.font, justify=LEFT)
        self.move2.place(x=OPTIONS_MOVES_FRAME_WIDTH/2,y=0,width=OPTIONS_MOVES_FRAME_WIDTH/2,height=OPTIONS_MOVES_FRAME_HEIGHT/2) 

        self.move3 = Button(self.moves_frame, text="move3", font=self.font, justify=LEFT)
        self.move3.place(x=0,y=OPTIONS_MOVES_FRAME_HEIGHT/2,width=OPTIONS_MOVES_FRAME_WIDTH/2,height=OPTIONS_MOVES_FRAME_HEIGHT/2)

        self.move4 = Button(self.moves_frame, text="move4", font=self.font, justify=LEFT)
        self.move4.place(x=OPTIONS_MOVES_FRAME_WIDTH/2,y=OPTIONS_MOVES_FRAME_HEIGHT/2,width=OPTIONS_MOVES_FRAME_WIDTH/2,height=OPTIONS_MOVES_FRAME_HEIGHT/2)

    def switch_GUI(self):
        '''Create the GUI for switching the pokemon'''
        # Switch GUI
        OUTTER_SWITCH_FRAME_COLOR = "#d64739"
        self.OUTTER_SWITCH_FRAME = Frame(self.root,bg=OUTTER_SWITCH_FRAME_COLOR)
        self.OUTTER_SWITCH_FRAME.place(x=0,y=0,width=MENU_WIDTH,height=MENU_HEIGHT)

        INNER_SWITCH_FRAME_COLOR = "#f8f8f8"
        self.INNER_SWITCH_FRAME = Frame(self.root,bg=INNER_SWITCH_FRAME_COLOR)
        self.INNER_SWITCH_FRAME.place(x=SIDE_FRAME,y=TOP_BOTTOM_FRAME,width=MENU_WIDTH-2*SIDE_FRAME,height=MENU_HEIGHT-2*TOP_BOTTOM_FRAME)
        
        SWITCH_BUTTONS_FRAME_WIDTH = MENU_WIDTH-(2*(MENU_CENTERX/4))
        SWITCH_BUTTONS_FRAME_HEIGHT = MENU_HEIGHT-(2*(MENU_HEIGHT/10))
        self.PokemonButtons = Frame(self.root, bg="#f8f8f8") 
        self.PokemonButtons.place(x=MENU_CENTERX/4,y=MENU_HEIGHT/10,width=SWITCH_BUTTONS_FRAME_WIDTH,height=SWITCH_BUTTONS_FRAME_HEIGHT)

        self.Pokemon1 = Button(self.PokemonButtons, text="PLACEHOLDER", font=self.font, justify="right")
        self.Pokemon1.place(x=0,y=0,width=SWITCH_BUTTONS_FRAME_WIDTH/2,height=SWITCH_BUTTONS_FRAME_HEIGHT/4)

        self.Pokemon2 = Button(self.PokemonButtons, text="PLACEHOLDER", font=self.font, justify="right")
        self.Pokemon2.place(x=(SWITCH_BUTTONS_FRAME_WIDTH/2),y=(SWITCH_BUTTONS_FRAME_HEIGHT/(4+3)),width=SWITCH_BUTTONS_FRAME_WIDTH/2,height=SWITCH_BUTTONS_FRAME_HEIGHT/4)

        self.Pokemon3 = Button(self.PokemonButtons, text="PLACEHOLDER", font=self.font, justify="right")
        self.Pokemon3.place(x=0,y=2*(SWITCH_BUTTONS_FRAME_HEIGHT/(4+3)),width=SWITCH_BUTTONS_FRAME_WIDTH/2,height=SWITCH_BUTTONS_FRAME_HEIGHT/4)
        
        self.Pokemon4 = Button(self.PokemonButtons, text="PLACEHOLDER", font=self.font, justify="right")
        self.Pokemon4.place(x=(SWITCH_BUTTONS_FRAME_WIDTH/2),y=3*(SWITCH_BUTTONS_FRAME_HEIGHT/(4+3)),width=SWITCH_BUTTONS_FRAME_WIDTH/2,height=SWITCH_BUTTONS_FRAME_HEIGHT/4)

        self.Pokemon5 = Button(self.PokemonButtons, text="PLACEHOLDER", font=self.font, justify="right")
        self.Pokemon5.place(x=0,y=4*(SWITCH_BUTTONS_FRAME_HEIGHT/(4+3)),width=SWITCH_BUTTONS_FRAME_WIDTH/2,height=SWITCH_BUTTONS_FRAME_HEIGHT/4)

        self.Pokemon6 = Button(self.PokemonButtons, text="PLACEHOLDER", font=self.font, justify="right")
        self.Pokemon6.place(x=(SWITCH_BUTTONS_FRAME_WIDTH/2),y=5*(SWITCH_BUTTONS_FRAME_HEIGHT/(4+3)),width=SWITCH_BUTTONS_FRAME_WIDTH/2,height=SWITCH_BUTTONS_FRAME_HEIGHT/4)

    def go_back(self):

        go_back = Button(self.root, )

    def setup(self): # Origin is top left corner
        '''Create all of the widgets for the main game menu.'''
        # Background
        wallpaper = Image.open("pokemon_background.png")
        wallpaper = ImageTk.PhotoImage(wallpaper)
        img_height = wallpaper.height()

        self.background = Label(self.root,image=wallpaper, bg=None)
        self.background.image = wallpaper
        self.background.place(x=0, y=img_height-MENU_HEIGHT, width=MENU_WIDTH, height=MENU_HEIGHT)


        self.font = Font(family="Helvetica", size=20, weight="bold")
        OPTIONS_INNER_FRAME_WIDTH = MENU_CENTERX-(2*SIDE_FRAME)
        OPTIONS_INNER_FRAME_HEIGHT = (BOTTOM_BARY)-(2*TOP_BOTTOM_FRAME*0.75)

        # Pokemon Sprites
        pokemon_player = Image.open("test_jojo.png")
        pokemon_player.resize((20,20), Image.ANTIALIAS)
        # pokemon_player = Image.open(pokemon_player + ".png")
        pokemon_player_resize = ImageTk.PhotoImage(pokemon_player)

        self.pokemon_player_img = Label(self.root, image=pokemon_player_resize, bg=None)
        self.pokemon_player_img.image = pokemon_player_resize
        pokemon_player_waist_up = pokemon_player_resize.height() / 2
        self.pokemon_player_img.place(x=MENU_CENTERX/4, y=BOTTOM_BARY_TOP-pokemon_player_waist_up)




        # Bottom bar
        BOTTOM_OUTTER_FRAME_COLOR = "#d64739"
        self.outer_options_frame = Frame(self.root,background=BOTTOM_OUTTER_FRAME_COLOR)
        self.outer_options_frame.place(x=0,y=BOTTOM_BARY_TOP,width=MENU_WIDTH,height=BOTTOM_BARY)
        
        self.right_options_frame = Frame(self.root,background="#f8f8f8")
        self.right_options_frame.place(x=MENU_CENTERX+SIDE_FRAME,y=BOTTOM_BARY_TOP+TOP_BOTTOM_FRAME,width=OPTIONS_INNER_FRAME_WIDTH, height=OPTIONS_INNER_FRAME_HEIGHT)
    
        self.left_options_frame = Frame(self.root)
        self.left_options_frame.place(x=SIDE_FRAME,y=BOTTOM_BARY_TOP+TOP_BOTTOM_FRAME,width=OPTIONS_INNER_FRAME_WIDTH, height=OPTIONS_INNER_FRAME_HEIGHT)


        # The "What Will You Do" text
        self.options_ask_start = Label(self.left_options_frame, text="PLACEHOLDER", bg="#69a1a2",font=self.font)
        self.options_ask_start.place(x=0, y=0, width=OPTIONS_INNER_FRAME_WIDTH, height=OPTIONS_INNER_FRAME_HEIGHT)


        # top left button
        self.fight_button = Button(self.right_options_frame, text="Fight", font=self.font, justify=LEFT)
        self.fight_button.place(x=0,y=0,width=OPTIONS_INNER_FRAME_WIDTH/2,height=OPTIONS_INNER_FRAME_HEIGHT/2)
        self.fight_button.config(borderwidth=0)
        
        
        # top right button
        self.bag_button = Button(self.right_options_frame, text="Bag", font=self.font, justify=LEFT)
        self.bag_button.place(x=OPTIONS_INNER_FRAME_WIDTH/2,y=0,width=OPTIONS_INNER_FRAME_WIDTH/2,height=OPTIONS_INNER_FRAME_HEIGHT/2)
        self.bag_button.config(borderwidth=0)

        # bottom left button
        self.switch_button = Button(self.right_options_frame, text="Switch", font=self.font, justify=LEFT)
        self.switch_button.place(x=0,y=OPTIONS_INNER_FRAME_HEIGHT/2,width=OPTIONS_INNER_FRAME_WIDTH/2,height=OPTIONS_INNER_FRAME_HEIGHT/2)
        self.switch_button.config(borderwidth=0)

        # bottom right button
        self.run_button = Button(self.right_options_frame, text="Run", font=self.font, justify=LEFT)
        self.run_button.place(x=OPTIONS_INNER_FRAME_WIDTH/2,y=OPTIONS_INNER_FRAME_HEIGHT/2,width=OPTIONS_INNER_FRAME_WIDTH/2,height=OPTIONS_INNER_FRAME_HEIGHT/2)
        self.run_button.config(borderwidth=0)

        # HP boxes
        self.player_hp_box = Label(self.root, text="HP:", bg="#69a1a2",font=self.font)
        self.player_hp_box.place(x=MENU_CENTERX*1.1, y=MENU_CENTERY*0.9, width=MENU_CENTERX*0.85, height=BOTTOM_BARY/2.5)

        self.opp_hp_box = Label(self.root, text="HP:", bg="#69a1a2", font=self.font)
        self.opp_hp_box.place(x=MENU_CENTERX*0.1, y=MENU_CENTERY*0.2, width=MENU_CENTERX*0.85, height=BOTTOM_BARY/2.5)






        '''self.pokemon_hp = Frame(self.root)
        self.pokemon_hp.grid(row=3, column=0)

        self.pokemon_remaining = Frame(self.root)
        self.pokemon_remaining.grid(row=4, column=0)'''


if __name__ == '__main__':
    window = Window()
    window.root.mainloop()
