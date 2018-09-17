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
    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.weapons = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0
    def add_ability(self, ability):
        self.abilities.append(ability)
    def add_weapon(self, weapon):
        self.weapons.append(weapon)
    def attack(self):
        for i in self.abilities:
            return i.attack()
    def defend(self):
        if self.health == 0:
            print("Sorry, this person is quite dead, I'm afraid.")
            return 0
        else:
            for i in self.armors:
                return i.defend()

    def take_damage(self, damage_amt):
        self.health -= damage_amt
        if self.health < 1:
            print("TERMINATED!")
            self.death += 1

    def add_kill(self, num_kills):
        print("EXTERMINATED!")
        self.kills += num_kills
class Weapon(Ability):
    def _init_(self, name, damage):
        self.name = name
        self.damage = damage
    def attack(self):
        random_int = random.randint(0, self.damage)
class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.villains = list()

    def add_villain(self, Villain):
        self.villains.append(Villain)

    def remove_villain(self, name):
        count = 0
        for i in self.villains:
            if i == name:
                self.villains.pop() #will change
                count = 1
        if count == 0:
            print("not found")
            return name
    def find_villain(self, name):
        count = 0
        for i in self.villains:
            if i == name:
                print(i.name)
                count = 1
        if count == 0:
            print("not found")
            return name

    def view_all_villains(self):
        for i in self.villains:
            print(i.name)

    def attack(self, other_team):
        sum = 0
        for i in self.villains:
            sum += i.attack()
        for i in other_team.villains:
            sum -= i.defend()
        if sum > 0:
            other_team.deal_damage(sum)
            for i in other_team.villains:
                if i.deaths > 0:
                    self.kills += i.deaths
        else:
            return sum

    def defend(self, damage_amt):
        sum = 0
        for i in self.villains:
            sum += i.defend()
        return sum

    def deal_damage(self, damage):
        ndamage = damage // len(self.villains)
        for i in self.villains:
            i.take_damage(ndamage)

    def revive_heroes(self, health=100):
        for i in self.villains:
            i.health = health

    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminal.
        """

    def update_kills(self):
        for i in self.villains:
            i.add_kill(1)
class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        defense = random.randint(0, self.defense)
        return defense
class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def build_team_one(self, team):
        self.team_one = team

    def build_team_two(self, team):
        self.team_two = team

    def team_battle(self):
        """
        To the death!
        """

    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """
vil = Villain("Joker")
venom = Villain("Venom")
thanos = Villain("Thanos")
darkside = Villain("Dark Side")
print(vil.attack())
ability = Ability("Divine Speed", 300)
vil.add_ability(ability)
print(vil.attack())
new_ability = Ability("Super Human Strength", 800)
vil.add_ability(new_ability)
print(vil.attack())
team_exterminate = Team("Team Exterminate")
team_subordinate = Team("Team Subordinate")
team_exterminate.add_villain(vil)
print(team_exterminate.find_villain(vil))
print(team_exterminate.view_all_villains())
team_exterminate.remove_villain(vil)
print(team_exterminate.view_all_villains())
bane = Villain("Bane")
bweapon = Weapon("Mace", 800)
tweapon = Weapon("Glove", 100000)
dweapon = Weapon("Army of a the Planet Dark Side", 100000)
bability = Ability("Monologuing", 10)
tability = Ability("Being Thanos", 10000)
dability = Ability("Being Dark Side", 10000)
bane.add_ability(bability)
bane.add_weapon(bweapon)
thanos.add_ability(tability)
darkside.add_ability(dability)
team_subordinate.add_villain(bane)
team_subordinate.add_villain(vil)
team_subordinate.add_villain(darkside)
team_exterminate.add_villain(venom)
team_exterminate.add_villain(thanos)
