class Player:

    def __init__(self,pokemon,team,items):

        self.pokemon = pokemon
        self.team = team
        self.items = items

    def get_pokemon(self):
        return self.pokemon

    def get_team(self):
        return self.team

    def get_items(self):
        return self.items