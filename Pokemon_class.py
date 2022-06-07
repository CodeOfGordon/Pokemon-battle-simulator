class Pokemon:

    def __init__(self,name,type,stats,moves):
        self.name = name
        self.type = type
        self.stats = stats
        self.moves = moves

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type
    
    def get_stats(self):
        return self.stats

    def get_moves(self):
        return self.moves