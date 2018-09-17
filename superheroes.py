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
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0
    def add_ability(self, ability):
        self.abilities.append(ability)
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
    def attack(self):
        random_int = random.randint(0, 7)
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
        if len(self.villains) == len(other_team):
            for i in self.villains:
                sum += i.attack()
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
        """
        self.team_one = None
        self.team_two = None
        """

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """

    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """
vil = Villain("Joker")
print(vil.attack())
ability = Ability("Divine Speed", 300)
vil.add_ability(ability)
print(vil.attack())
new_ability = Ability("Super Human Strength", 800)
vil.add_ability(new_ability)
print(vil.attack())
team_exterminate = Team("Team Exterminate")
team_exterminate.add_villain(vil)
print(team_exterminate.find_villain(vil))
print(team_exterminate.view_all_villains())
team_exterminate.remove_villain(vil)
print(team_exterminate.view_all_villains())
