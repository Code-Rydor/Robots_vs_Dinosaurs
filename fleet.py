from robot import Robot

class Fleet:
    
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robot1 = Robot("Surge")
        self.robots.append(robot1)
        robot2 = Robot("Mr. Metal")
        self.robots.append(robot2)
        robot3 = Robot("Blitz")
        self.robots.append(robot3)
fleet1 = Fleet()
fleet1.create_fleet()

