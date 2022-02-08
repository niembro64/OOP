# class - attributes - methods

class SuperHero:

    population = 0

    # this is the constructor | blueprint of attributes
    def __init__(self, n, a, s, h = 100, p = 5):
        self.name = n
        self.ability = a
        self.suit = s
        self.health = h
        self.attack_power = p
        SuperHero.population += 1
        # nemisis
        # sidekick

    # class methods
    @classmethod
    def printPopulus(cls):
        print(f"Population: {SuperHero.population}")


    # down here will be our methods

    # method to introduce hero
    def intro(self):
        print(f"Hi, my name is {self.name}, my super power is {self.ability}, I like wearing {self.suit}.")
        return self

    # method for fighting
    def attack(self, target):
        # adding logic to decrease health when attacking
        if target.health == 0:
            print(f"Can't attack{target.name}, they are dead.")
        else:
            target.health -= self.attack_power
            if target.health < 0:
                target.health = 0
            print(f"{self.name} used {self.ability} against {target.name}, their health is now {target.health}")
        return self

    # increase attack power
    def train(self):
        self.attack_power += 10
        print(f"{self.name} trained, his attack is now {self.attack_power}.")
        return self

# make our stuff happen down here
super_hero1 = SuperHero("Jim", "Making Slim Jims", "Overalls")
super_hero2 = SuperHero("Felix", "CSS Reducing", "Gold Plated Armor")
super_hero3 = SuperHero("Raef", "Sword", "Bandana")

super_hero1.intro()
super_hero1.printPopulus()
super_hero2.intro()
super_hero1.printPopulus()
super_hero3.intro()
super_hero1.printPopulus()

super_hero1.attack(super_hero2)
super_hero1.attack(super_hero2)
super_hero1.attack(super_hero2)
super_hero1.attack(super_hero2)
super_hero1.train()
super_hero1.attack(super_hero2)
super_hero1.attack(super_hero2)
super_hero1.attack(super_hero2)
super_hero1.attack(super_hero2)
super_hero1.attack(super_hero2)
super_hero1.attack(super_hero2)
super_hero1.attack(super_hero2)
super_hero1.attack(super_hero2)
super_hero1.attack(super_hero2)