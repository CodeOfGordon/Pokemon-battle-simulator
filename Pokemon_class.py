import csv
import random
from Move_class import create_moves

class Pokemon:

    def __init__(self,index,name,type,hp,attack,defence,level,moves=[]):
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
            'leve' : self.level,
            'moves' : self.moves
        }

    def __repr__(self):
        return f"{self.index},{self.name},{self.type},{self.hp},{self.attack},{self.defence},{self.level},{self.moves}"

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
    pokemon_moves = []
    try:
        all_moves = create_moves(filename)
        while len(pokemon_moves) < 4:
            move = all_moves[random.randint(1,165)]
            if move["type"] == type:
                pokemon_moves.append([move])
    except FileNotFoundError:
        print("File not found.")
    return pokemon_moves

def make_pokemon(filename):
    pokedex = {}
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                pokedex[row["#"]] = Pokemon(row["#"],row["Name"],row["Type"],row["HP"],row["Attack"],row["Defense"])
    except FileNotFoundError:
        print("File not found.")
    return pokedex

print(make_pokemon("pokemon.csv"))