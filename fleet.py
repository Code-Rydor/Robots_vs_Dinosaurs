from robot import Robot

class Fleet:
    
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot1 = Robot("Aluminor")
        self.robots.append(robot1)
        robot2 = Robot("Steely")
        self.robots.append(robot2)
        robot3 = Robot("Iron Eye")
        self.robots.append(robot3)

