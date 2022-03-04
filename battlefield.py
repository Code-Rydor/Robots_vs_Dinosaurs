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
        press_to_continue = input("Enter 0 to attack: ")
        if press_to_continue == "0":
            print("")
            print("FIGHT!!!")
            print("")
            self.dino_turn()
        elif press_to_continue != "0":
            press_to_continue = input("Enter 0 to attack: ")
    print("")
        press_to_continue = input("Enter 0 to attack: ")
        if press_to_continue == "0":
            print("")
            self.robo_turn()
        elif press_to_continue != "0":
            press_to_continue = input("Enter 0 to attack: ")
            

    def dino_turn(self):
            self.herd.dinosaurs[0].attack(self.fleet.robots[0])
            self.herd.dinosaurs[1].attack(self.fleet.robots[1])
            self.herd.dinosaurs[2].attack(self.fleet.robots[2])
    print("")
        
    def robo_turn(self):
        self.fleet.robots[0].attack(self.herd.dinosaurs[0])
        self.fleet.robots[1].attack(self.herd.dinosaurs[1])
        self.fleet.robots[2].attack(self.herd.dinosaurs[2])
    print("")
    
    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass
