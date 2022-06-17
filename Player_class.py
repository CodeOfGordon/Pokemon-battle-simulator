import random
from Pokemon_class import make_pokemon

class Player:

    def __init__(self,pokemon,team,items):

        self.pokemon = pokemon
        self.team = team
        self.items = items

    def get_pokemon(self):
        return self.pokemon

    def get_team(self):
        return self.team

    #def get_items(self):
        #return self.items

def create_teams(filename):
    '''(str) -> tuple
    Creates 2 teams of 4 random pokemon
    '''
    pokedex = make_pokemon(filename)
    team_1 = []
    team_2 = []
    for x in range(4):
        team_1.append(pokedex[str(random.randint(1,151))])
        team_2.append(pokedex[str(random.randint(1,151))])
    return team_1,team_2