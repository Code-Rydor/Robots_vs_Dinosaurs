from dinosaur import Dinosaur

class Herd:
    
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino1 = Dinosaur("Big Rex", 40)
        self.dinosaurs.append(dino1)
        dino2 = Dinosaur("Rip Raptor", 40)
        self.dinosaurs.append(dino2)
        dino3 = Dinosaur("Clawdia", 40)
        self.dinosaurs.append(dino3)

