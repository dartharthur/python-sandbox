class Base:
    def __init__(self, name):
        self.name = name
        self.level = 1
        
        self.agility = 10
        self.intelligence = 10
        self.hitpoints = 10
        self.mana = 10
        self.strength = 10
    
    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def level_up(self):
        self.level += 1

# self.stats = {
#     'agility': 10,
#     'intelligence': 10,
#     'hitpoints': 10,
#     'mana': 10,
#     'strength': 10
# }
