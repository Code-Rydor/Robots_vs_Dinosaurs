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
        play_game = True
        while play_game is True:
            self.show_dino_opponent_options()
            self.show_robo_opponent_options()
            self.dino_turn()
            if len(self.herd.dinosaurs) == 0 or len(self.fleet.robots) == 0: #for some reason, this wont run and I dont know why
                play_game = False
                self.display_winners()
            self.show_robo_opponent_options()
            self.show_dino_opponent_options()
            self.robo_turn()
            if len(self.herd.dinosaurs) == 0 or len(self.fleet.robots) == 0: #for some reason, this wont run and I dont know why
                play_game = False
                self.display_winners()
                    
    print("")

    def dino_turn(self):
        self.chosen_dino.attack(self.chosen_robo)
        if self.chosen_robo.health <= 0:
            self.fleet.robots.remove(self.chosen_robo)
            print(f"Oh snap! {self.chosen_robo.name} is dead!")
        else:
            print(f"{self.chosen_dino.name} attacked {self.chosen_robo.name} doing {self.chosen_dino.attack_power} damage, leaving {self.chosen_robo.name} with {self.chosen_robo.health} health remaining!")

    print("")
        
    def robo_turn(self):
        self.chosen_robo.attack(self.chosen_dino)
        if self.chosen_dino.health <= 0:
            self.herd.dinosaurs.remove(self.chosen_dino)
            print(f"Oh snap! {self.chosen_dino.name} is dead!")
        else:
            print(f"{self.chosen_robo.name} attacked {self.chosen_dino.name} doing {self.chosen_robo.weapon.attack_power} damage, leaving {self.chosen_dino.name} with {self.chosen_dino.health} health remaining!")

    def show_dino_opponent_options(self):
        print("")
        count = 1

        for dino in self.herd.dinosaurs:
            print(f"Enter {count} to use {dino.name}")
            count += 1
        user_dino_choice = input("Choose a dinosaur: ")
        if user_dino_choice == "1":
            self.chosen_dino = self.herd.dinosaurs[0]
        elif user_dino_choice == "2":
            self.chosen_dino = self.herd.dinosaurs[1]
        elif user_dino_choice == "3":
            self.chosen_dino = self.herd.dinosaurs[2]
    def show_robo_opponent_options(self):
        print("")
        count = 1

        for robo in self.fleet.robots:
            print(f"Enter {count} to use {robo.name}")
            count +=1
        user_robo_choice = input("Choose a robot: ")
        if user_robo_choice == "1":
            self.chosen_robo = self.fleet.robots[0]
        elif user_robo_choice == "2":
            self.chosen_robo = self.fleet.robots[1]
        elif user_robo_choice == "3":
            self.chosen_robo = self.fleet.robots[2]

    def display_winners(self):
        if self.herd.dinosaurs == 0: #I forgot to add len()
            print("This fight is over!")
            print("The winning team is Robots!")
        elif self.fleet.robots == 0: #I forgot to add len()
            print("This fight is over!")
            print("The winning team is Dinosaurs!")
        