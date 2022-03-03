from robot import Robot

class Fleet:
    
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot1 = Robot("Surge")
        self.robots.append(robot1)
        robot2 = Robot("Mr. Metal")
        self.robots.append(robot2)
        robot3 = Robot("Blitz")
        self.robots.append(robot3)

