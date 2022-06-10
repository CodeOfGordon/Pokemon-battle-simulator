import csv

class Move:

    def __init__(self,name,type,damage,status="None"):

        self.name = name
        self.status = status
        self.type = type
        self.damage = damage
        self.attributes = {
        'name' : self.name,
        'type' : self.type,
        'damage' : self.damage,
        'status' : self.status}

    def __repr__(self):
        return f"{self.name},{self.type},{self.damage},{self.status}"

    def __getitem__(self,item):
        return self.attributes[item]

    def get_name(self):
        return self.name

    def get_status(self):
        return self.status

    def get_type(self):
        return self.type

    def get_damage(self):
        return self.damage

def create_moves(filename):
    ''' (str) -> dict
    Creates and returns a dictionary of every move possible
    '''
    moves = {}
    count = 0
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                count += 1
                moves[count] = Move(row["Name"],row["Type"],row["Power"])
    except FileNotFoundError:
        print("File not found.")
    return moves