class Window:

    def __init__(self,pokemon,run,fight,switch,name,hp,bag,pokemon_left):

        self.pokemon = pokemon
        self.run_button = run
        self.fight_button = fight
        self.switch_button = switch
        self.pokemon_name = name
        self.pokemon_hp = hp
        self.bag_button = bag
        self.pokemon_remaining = pokemon_left

    def get_pokemon(self):
        return self.pokemon

    def get_run_button(self):
        return self.run_button

    def get_fight_button(self):
        return self.fight_button
    
    def get_switch_button(self):
        return self.switch_button

    def get_pokemon_name(self):
        return self.pokemon_name

    def get_pokemon_hp(self):
        return self.pokemon_hp

    def get_bag_button(self):
        return self.bag_button

    def get_pokemon_remaining(self):
        return self.pokemon_remaining