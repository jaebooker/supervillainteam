import random
class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        random_int = random.randint(self.attack_strength // 2, self.attack_strength)
        return random_int

    def update_attack(self, newStrength):
        self.attack_strength = newStrength
class Villain:
    def __init__(self, name):
        self.abilities = list()
        self.name = name
    def add_ability(self, ability):
        self.abilities.append(ability)
    def attack(self):
        for i in self.abilities:
            print(i.attack())
class Weapon(Ability):
    def attack(self):
        random_int = random.randint(0, 7)
class Team:
    def init(self, team_name):
        self.name = team_name
        self.villains = list()

    def add_villain(self, Villain):
        villains.append(Villain)

    def remove_villain(self, name):
        count = 0
        for i in self.villains:
            if i.name == name:
                self.villains.pop(i)
                count = 1
        if count == 0:
            print("not found")
            return name
    def find_villain(self, name):
        count = 0
        for i in self.villains:
            if i.name == name:
                return i
                count = 1
        if count == 0:
            print("not found")
            return name

    def view_all_villains(self):
        for i in self.villains:
            print(i)
vil = Villain("Joker")
print(vil.attack())
ability = Ability("Divine Speed", 300)
vil.add_ability(ability)
print(vil.attack())
new_ability = Ability("Super Human Strength", 800)
vil.add_ability(new_ability)
print(vil.attack())
