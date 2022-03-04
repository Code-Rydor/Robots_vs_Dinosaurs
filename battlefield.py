import random
from fleet import Fleet
from herd import Herd
  
#(/10 points): As a developer, I want the battle to conclude once either all the robots in the Fleet have their health points reach 
#              zero or all of the dinosaurs in the Herd have their health points reach zero. 
 
#Bonus Points: 

#(/5 points): As a developer, I want a Robot to have the ability to choose from a List of different weapons that will be then assigned 
#             as its own weapon.  
  
#(/5 points): As a developer, I want a Dinosaur to have the ability to choose its attack name from a tuple of different attack names 
#             before attacking a Robot in battle. 
  
#(/2 points): As a developer, I want a Robot to have a power level and a Dinosaur to have an energy, which will decrease by 10 every 
#             time they attack.

class Battlefield:
   
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.chosen_dino = 0
        self.chosen_robo = 0

    def run_game(self):
        self.display_welcome()
        self.battle()

    def display_welcome(self):
        print("")
        print("Welcome to the Battledome!")
        print("")
        print(f"On team Robots we have {self.fleet.robots[0].name}, {self.fleet.robots[1].name}, and {self.fleet.robots[2].name}...")
        print("And...")
        print(f"On team Dinosaurs we have {self.herd.dinosaurs[0].name}, {self.herd.dinosaurs[1].name}, and {self.herd.dinosaurs[2].name}...")
        print("")
        print("Let's get ready to rrruuummmbbbllleee!")
        print("")

    def battle(self):
        while (self.fleet.robots != []) and (self.herd.dinosaurs != []):
            self.show_dino_opponent_options()
            self.show_robo_opponent_options()
            self.dino_turn()
            self.robo_turn()
    print("")

    def dino_turn(self):
        self.chosen_dino.attack(self.chosen_robo)
        if self.chosen_robo.health <= 0:
            self.fleet.robots.pop(self.chosen_robo)
            print(f"Oh snap! {self.chosen_robo.name} is dead!")
        else:
            print(f"{self.chosen_dino.name} attacked {self.chosen_robo.name} doing {self.chosen_dino.attack_power} damage, leaving {self.chosen_robo.name} with {self.chosen_robo.health} health remaining!")

    print("")
        
    def robo_turn(self):
        self.chosen_robo.attack(self.chosen_dino)
        if self.chosen_dino.health <= 0:
            self.herd.dinosaurs.pop(self.chosen_dino)
            print(f"Oh snap! {self.chosen_dino.name} is dead!")
        else:
            print(f"{self.chosen_robo.name} attacked {self.chosen_dino.name} doing {self.chosen_robo.weapon.attack_power} damage, leaving {self.chosen_dino.name} with {self.chosen_dino.health} health remaining!")

    def show_dino_opponent_options(self):
        print("")
        print(f"Press 1 for {self.herd.dinosaurs[0].name} ({self.herd.dinosaurs[0].health} health)")
        print(f"Press 2 for {self.herd.dinosaurs[1].name} ({self.herd.dinosaurs[1].health} health)")
        print(f"Press 3 for {self.herd.dinosaurs[2].name} ({self.herd.dinosaurs[2].health} health)")
        self.chosen_dino = input("Choose a dinosaur: ")
        if self.chosen_dino == "1":
            self.chosen_dino = self.herd.dinosaurs[0]
        elif self.chosen_dino == "2":
            self.chosen_dino = self.herd.dinosaurs[1]
        elif self.chosen_dino == "3":
            self.chosen_dino = self.herd.dinosaurs[2]
        
    def show_robo_opponent_options(self):
        print("")
        print(f"Press 1 for {self.fleet.robots[0].name} ({self.fleet.robots[0].health} health)")
        print(f"Press 2 for {self.fleet.robots[1].name} ({self.fleet.robots[1].health} health)")
        print(f"Press 3 for {self.fleet.robots[2].name} ({self.fleet.robots[2].health} health)")
        self.chosen_robo = input("Choose a robot: ")
        if self.chosen_robo == "1":
            self.chosen_robo = self.fleet.robots[0]
        elif self.chosen_robo == "2":
            self.chosen_robo = self.fleet.robots[1]
        elif self.chosen_robo == "3":
            self.chosen_robo = self.fleet.robots[2]

    def display_winners(self):
        pass
