class Fight:

    def __init__(self,move,damage,multiplier,pokemon):

        self.move = move
        self.damage = damage
        self.multiplier = multiplier
        self.pokemon = pokemon

    def get_move(self):
        return self.move

    def get_damage(self):
        return self.damage

    def get_multiplier(self):
        return self.multiplier

    def get_pokemon(self):
        return self.pokemon