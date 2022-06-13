from tkinter import *
from tkinter.font import BOLD, Font
from Move_class import *
from Pokemon_class import *
from Fight_class import *
from Player_class import *
import random
from PIL import Image, ImageTk


MENU_WIDTH = 1024
MENU_HEIGHT = 576
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

    def test(self):
        COLORS = ["red", "green", "blue", "yellow"]
        example = Label(self.root, text="test", background=random.choice(COLORS))
        example.place(x=0, y=0, width=50, height=50)

    def mouse_hover_change(self, button, oldtext):
        '''Change the text of the button when the mouse is over it.'''
        button.bind("<Enter>", lambda e: button.config(text="➤ " + oldtext))
        button.bind("<Leave>", lambda e: button.config(text=oldtext))
    

    def moves_GUI(self,event):
        '''Create the GUI for the moves.'''
        OPTIONS_MOVES_FRAME_WIDTH = MENU_WIDTH-(2*SIDE_FRAME)
        OPTIONS_MOVES_FRAME_HEIGHT = (BOTTOM_BARY)-(2*TOP_BOTTOM_FRAME*0.75)

        self.moves_frame = Frame(self.root, bg="white")
        self.moves_frame.place(x=SIDE_FRAME, y=BOTTOM_BARY_TOP+TOP_BOTTOM_FRAME, width=OPTIONS_MOVES_FRAME_WIDTH, height=OPTIONS_MOVES_FRAME_HEIGHT)

        self.move1 = Button(self.moves_frame, text="move1", font=self.font, justify=LEFT,command=self.test)
        self.move1.place(x=0,y=0,width=OPTIONS_MOVES_FRAME_WIDTH/2,height=OPTIONS_MOVES_FRAME_HEIGHT/2)

        self.move2 = Button(self.moves_frame, text="move2", font=self.font, justify=LEFT,command=self.test)
        self.move2.place(x=OPTIONS_MOVES_FRAME_WIDTH/2,y=0,width=OPTIONS_MOVES_FRAME_WIDTH/2,height=OPTIONS_MOVES_FRAME_HEIGHT/2) 

        self.move3 = Button(self.moves_frame, text="move3", font=self.font, justify=LEFT,command=self.test)
        self.move3.place(x=0,y=OPTIONS_MOVES_FRAME_HEIGHT/2,width=OPTIONS_MOVES_FRAME_WIDTH/2,height=OPTIONS_MOVES_FRAME_HEIGHT/2)

        self.move4 = Button(self.moves_frame, text="move4", font=self.font, justify=LEFT,command=self.test)
        self.move4.place(x=OPTIONS_MOVES_FRAME_WIDTH/2,y=OPTIONS_MOVES_FRAME_HEIGHT/2,width=OPTIONS_MOVES_FRAME_WIDTH/2,height=OPTIONS_MOVES_FRAME_HEIGHT/2)

        self.move2.bind("<Escape>", lambda e: self.moves_frame.destroy) # Make this button close the frame



    def setup(self): # Change to use place() instead of grid(). Also origin is top left corner
        '''Create all of the widgets for the menu.'''
        background = Image("Sprites/pokemon_background.png")
        background = ImageTk(background)
        background.place(x=0,)


        self.font = Font(family="Helvetica", size=20, weight="bold")
        OPTIONS_INNER_FRAME_WIDTH = MENU_CENTERX-(2*SIDE_FRAME)
        OPTIONS_INNER_FRAME_HEIGHT = (BOTTOM_BARY)-(2*TOP_BOTTOM_FRAME*0.75)


        # Bottom bar
        BOTTOM_OUTTER_FRAME_COLOR = "#d64739"
        self.outer_options_frame = Frame(self.root,background=BOTTOM_OUTTER_FRAME_COLOR)
        self.outer_options_frame.place(x=0,y=BOTTOM_BARY_TOP,width=MENU_WIDTH,height=BOTTOM_BARY)
        
        self.right_options_frame = Frame(self.root,background="#f8f8f8")
        self.right_options_frame.place(x=MENU_CENTERX+SIDE_FRAME,y=BOTTOM_BARY_TOP+TOP_BOTTOM_FRAME,width=OPTIONS_INNER_FRAME_WIDTH, height=OPTIONS_INNER_FRAME_HEIGHT)
    
        self.left_options_frame = Frame(self.root)
        self.left_options_frame.place(x=SIDE_FRAME,y=BOTTOM_BARY_TOP+TOP_BOTTOM_FRAME,width=OPTIONS_INNER_FRAME_WIDTH, height=OPTIONS_INNER_FRAME_HEIGHT)


        # The "What Will You Do" text
        self.options_ask_start = Label(self.left_options_frame, text=(f"What will\nPLACEHOLDER do?"), bg="#69a1a2",font=self.font) # self.get_pokemon_name_pl
        self.options_ask_start.place(x=0, y=0, width=OPTIONS_INNER_FRAME_WIDTH, height=OPTIONS_INNER_FRAME_HEIGHT)


        # top left button
        self.fight_button = Button(self.right_options_frame, text="Fight", font=self.font, justify=LEFT,command=self.test)
        self.fight_button.place(x=0,y=0,width=OPTIONS_INNER_FRAME_WIDTH/2,height=OPTIONS_INNER_FRAME_HEIGHT/2)
        self.fight_button.config(borderwidth=0)
        self.mouse_hover_change(self.fight_button, "Fight")
        
        # top right button
        self.bag_button = Button(self.right_options_frame, text="Bag", font=self.font, justify=LEFT,command=self.test)
        self.bag_button.place(x=OPTIONS_INNER_FRAME_WIDTH/2,y=0,width=OPTIONS_INNER_FRAME_WIDTH/2,height=OPTIONS_INNER_FRAME_HEIGHT/2)
        self.bag_button.config(borderwidth=0)
        self.bag_button["state"] = DISABLED
        self.mouse_hover_change(self.bag_button, "Bag")

        # bottom left button
        self.switch_button = Button(self.right_options_frame, text="Switch", font=self.font, justify=LEFT,command=self.test)
        self.switch_button.place(x=0,y=OPTIONS_INNER_FRAME_HEIGHT/2,width=OPTIONS_INNER_FRAME_WIDTH/2,height=OPTIONS_INNER_FRAME_HEIGHT/2)
        self.switch_button.config(borderwidth=0)
        self.mouse_hover_change(self.switch_button, "Switch")

        # bottom right button
        self.run_button = Button(self.right_options_frame, text="Run", font=self.font, justify=LEFT,command=self.test)
        self.run_button.place(x=OPTIONS_INNER_FRAME_WIDTH/2,y=OPTIONS_INNER_FRAME_HEIGHT/2,width=OPTIONS_INNER_FRAME_WIDTH/2,height=OPTIONS_INNER_FRAME_HEIGHT/2)
        self.run_button.config(borderwidth=0)
        self.mouse_hover_change(self.run_button, "Run")


        # ---- If player chooses FIGHT ----
        self.fight_button.bind("<Button-1>", self.moves_GUI)


        self.pokemon_name_box = Label(self.root, text="PLACEHOLDER",font=self.font) # self.get_pokemon_name_pl











        '''self.pokemon_hp = Frame(self.root)
        self.pokemon_hp.grid(row=3, column=0)

        self.pokemon_remaining = Frame(self.root)
        self.pokemon_remaining.grid(row=4, column=0)'''


if __name__ == '__main__':
    window = Window()
    window.root.mainloop()
