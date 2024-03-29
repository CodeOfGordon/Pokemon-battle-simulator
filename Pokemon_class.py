import csv
import random
from Move_class import create_all_moves

class Pokemon:

    def __init__(self,index,name,type,hp,attack,defence,moves,level=50):
        self.index = index
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.moves = moves
        self.level = level
        self.attributes = {
            'index' : self.index,
            'name' : self.name,
            'type' : self.type,
            'hp' : self.hp,
            'attack' : self.attack,
            'defence' : self.defence,
            'moves' : self.moves,
            'level' : self.level
        }

    def __repr__(self):
        return f"{self.index},{self.name},{self.type},{self.hp},{self.attack},{self.defence},{self.level},{self.moves}"

    def __getitem__(self,item):
        return self.attributes[item]

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type
    
    def get_hp(self):
        return self.hp

    def get_attack(self):
        return self.attack

    def get_defence(self):
        return self.defence

    def get_level(self):
        return self.level

    def get_moves(self):
        return self.moves

def make_moves(type,filename):
    ''' (str,str) -> list
    Determines and returns 4 random moves for a pokemon depending on its type
    '''
    pokemon_moves = []
    try:
        all_moves = create_all_moves(filename)
        all_type_moves = []
        all_normal_moves = []
        for move in all_moves:
            if all_moves[move]['type'] == type:
                all_type_moves.append(all_moves[move])
            elif all_moves[move]['type'] == "Normal":
                all_normal_moves.append(all_moves[move])
        while len(pokemon_moves) < 4:
            if len(all_type_moves) > 0:
                move = all_type_moves[random.randint(1,len(all_type_moves))-1]
            else:
                move = all_normal_moves[random.randint(1,len(all_normal_moves))-1]
            add_move = True
            for existing_move in pokemon_moves:
                if move == existing_move:
                    add_move = False
            if add_move == True:
                pokemon_moves.append([move])
                try:
                    all_type_moves.remove(move)
                except ValueError:
                    pass

    except FileNotFoundError:
        print("File not found.")
    return pokemon_moves

def make_pokemon(filename):
    ''' (str) -> dict
    Creates and returns a dictionary containing every pokemon and their name, type, hp, attack stat, defense stat, level, and moves
    '''
    pokedex = {}
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                pokedex[row["#"]] = Pokemon(row["#"],row["Name"],row["Type"],row["HP"],row["Attack"],row["Defense"],[])
    except FileNotFoundError:
        print("File not found.")
    return pokedex