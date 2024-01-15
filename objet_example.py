
class Player:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def perdre_hp(self, hp):
        self.health -= hp

    def __str__(self):
        return (self.name)


p = Player("Michel", 100, 10)
p.perdre_hp(10)
p.name    # -> Michel
p.name = "Machin"
print(p)  # -> Michel
