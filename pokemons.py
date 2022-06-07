from tkinter import *

root = Tk()
root.title("Pokemon")
root.geometry("1200x700")
CENTERX = 1200/2
CENTERY = 700/2


class ChoosePokemon:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()

        self.label = Label(self.frame, text="Choose your Pokemon",font="Helvetica 20 bold")
        self.label.place(x=CENTERX, y=650)


















root.mainloop()