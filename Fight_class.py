import csv

class Fight:

    def __init__(self,move,damage,pokemon,enemy_pokemon):

        self.move = move
        self.damage = damage
        self.pokemon = pokemon
        self.enemy_pokemon = enemy_pokemon

    def get_move(self):
        return self.move

    def get_damage(self):
        return self.damage

    def get_pokemon(self):
        return self.pokemon

    def get_enemy_pokemon(self):
        return self.enemy_pokemon

def get_multiplier(filename,attacker_type,defender_type):
    ''' (str,str,str) -> int
    Determines and returns the multiplier used in damage calculation based on a pokemons attack stat and defence stat
    >>> get_multiplier("multiplier.csv","normal","normal")
    1
    '''
    damage_multiplier = 0
    attacker_type = attacker_type.capitalize()
    defender_type = defender_type.capitalize()
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Attacker"] == attacker_type:
                    damage_multiplier = row[defender_type]
    except FileNotFoundError:
        print("File not found.")
    return int(damage_multiplier)

def determine_damage(multiplier,attacker_level,move_power,attack_stat,defence_stat):
    ''' (int,int,int,int,int) -> float
    Determines and returns the damage done by an attacker
    >>> determine_damage(1,50,30,25,25)
    idk
    '''
    first_bracket = ((2*attacker_level)/5)+2
    second_bracket = ((attack_stat/defence_stat)/50)+2
    damage = ((first_bracket*move_power*second_bracket)*multiplier)*5
    return damage