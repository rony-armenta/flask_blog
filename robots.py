class Robot:
    def __init__(self, name, world, creator):
        self.name = name  # Storing 'name' inside THIS specific robot
        self.world = world
        self.__brand = creator

    def say_hello(self):
        # Without 'self', the robot wouldn't know which name to use!
        print(f"Hello, my name is {self.name}, I'm from {self.world} and my brand it's {self.__brand}")


# Create two DIFFERENT robots
bot1 = Robot("R2-D2", "Alpha02", "Tesla")
bot2 = Robot("C-3PO", "Centaury-ft3", "AWS")

bot1.say_hello()  # 'self' becomes bot1 -> "Hello, my name is R2-D2"
bot2.say_hello()  # 'self' becomes bot2 -> "Hello, my name is C-3PO"
