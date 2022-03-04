
from weapon import Weapon

class Robot:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Laser", 40)

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f"{self.name} attacked {dinosaur.name} doing {self.weapon.attack_power} damage, leaving {dinosaur.name} with {dinosaur.health} health remaining!")
