class Move:

    def __init__(self, name, status, type, damage):
        self.name = name
        self.status = status
        self.type = type
        self.damage = damage

    def get_name_move(self):
        return self.name
    
    def get_status_move(self):
        return self.status
    
    def get_type_move(self):
        return self.type
    
    def get_damage_move(self):
        return self.damage