from dinosaur import Dinosaur

class Herd:
    
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        dino1 = Dinosaur("Big Rex", 40)
        self.dinosaurs.append(dino1)
        dino2 = Dinosaur("Rip Raptor", 40)
        self.dinosaurs.append(dino2)
        dino3 = Dinosaur("Claw Dad", 40)
        self.dinosaurs.append(dino3)
herd1 = Herd()
herd1.create_herd()
