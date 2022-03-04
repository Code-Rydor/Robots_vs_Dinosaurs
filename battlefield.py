from fleet import Fleet
from herd import Herd

class Battlefield:
    
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        print(self.fleet.robots[0].name)
        self.fleet.robots[0].attack(self.herd.dinosaurs[0])#coded by James... follow this example to track dot notations
        self.herd.dinosaurs[0].attack(self.fleet.robots[0])
        pass

    def display_welcome(self):
        print("Welcome to the Battledome!")

    def battle(self):# I call battle() in run_game 
        pass   # calls dino_turn and robot_turn methods

    def dino_turn(self):
        pass

    def robo_turn(self):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass
