from dinosaur import Dinosaur

class Herd:
    
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino1 = Dinosaur("Big Rex", 50)
        self.dinosaurs.append(dino1)
        dino2 = Dinosaur("Rip Raptor", 50)
        self.dinosaurs.append(dino2)
        dino3 = Dinosaur("Clawdia", 50)
        self.dinosaurs.append(dino3)

