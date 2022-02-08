# class - attributes - methods

class SuperHero:

    # this is the constructor | blueprint of attributes
    def __init__(self, n, a, s):
        self.name = n
        self.ability = a
        self.suit = s
        # nemisis
        # sidekick

    # down here will be our methods

    # method to introduce hero
    def intro(self):
        print(f"Hi, my name is {self.name}, my super power is {self.ability}, I like wearing {self.suit}.")
        return self

# make our stuff happen down here
super_hero1 = SuperHero("Jim", "Making Slim Jims", "Overalls")
super_hero2 = SuperHero("Felix", "CSS Reducing", "Gold Plated Armor")
super_hero3 = SuperHero("Raef", "Sword", "Bandana")

super_hero1.intro()
super_hero2.intro()
super_hero3.intro()

