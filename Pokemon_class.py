class Pokemon:

    def __init__(self,index,name,type,hp,attack,defence,moves):
        self.index = index
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.moves = moves

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

    def get_moves(self):
        return self.moves