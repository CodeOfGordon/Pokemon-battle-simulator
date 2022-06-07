class Move:

    def __init__(self,name,status,type,damage):

        self.name = name
        self.status = status
        self.type = type
        self.damage = damage

    def get_name(self):
        return self.name

    def get_status(self):
        return self.status

    def get_type(self):
        return self.type

    def get_damage(self):
        return self.damage