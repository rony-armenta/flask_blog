class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.score = 0

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"💀 {self.name} has been defeated!")
        else:
            print(f"💥 {self.name} health: {self.health}")

    def heal(self, amount):
        self.health = amount
        if self.health > 100:
            print(f"Player's health shouldn't be more than 100")
            self.health = 100
        elif self.health >= 3 <= 10:
            self.health += amount
            print(f"{self.health}")
        else:
            print(f"{self.name} health: {self.health}")

    def add_score(self, points):
        self.score += points
        print(f"⭐ {self.name} score: {self.score}")


# --- LET'S PLAY ---

# Creating two unique instances
p1 = Player("DragonSlayer")
p2 = Player("ShadowNinja")

# Using the methods
p1.add_score(50)      # self is p1 here
p2.take_damage(98)    # self is p2 here
p1.heal(40)

print(
    f"\nFinal Stats: {p1.name} has {p1.score} points. {p2.name} has {p2.health} health.")
