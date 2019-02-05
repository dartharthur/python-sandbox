from .base import Base

class Warrior(Base):
    def __init__(self, name, strength):
        super().__init__(name)
        self.strength = strength

    
    def get_strength():
        return self.strength
