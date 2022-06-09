import csv

class Fight:

    def __init__(self,move,damage,pokemon):

        self.move = move
        self.damage = damage
        self.pokemon = pokemon

    def get_move(self):
        return self.move

    def get_damage(self):
        return self.damage

    def get_pokemon(self):
        return self.pokemon

def get_multiplier(filename,attacker_type,defender_type):
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
    return damage_multiplier

def determine_damage(multiplier,attacker_level,move_power,attack_stat,defence_stat):
    first_bracket = ((2*attacker_level)/5)+2
    second_bracket = ((attack_stat/defence_stat)/50)+2
    damage = ((first_bracket*move_power*second_bracket)*multiplier)*5
    return damage