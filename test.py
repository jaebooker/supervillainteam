import random
team_list = list()
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
    def add_armor(self, armor):
        self.armors.append(armor)
    def attack(self):
        if self.deaths == 0:
            if self.abilities:
                for i in self.abilities:
                    return i.attack()
            else:
                return 0
        else:
            return 0
    def defend(self):
        if self.health == 0:
            print("Sorry, this person is quite dead, I'm afraid.")
            return 0
        else:
            if self.armors:
                for i in self.armors:
                    return i.defend()
            else:
                return 0

    def take_damage(self, damage_amt):
        self.health -= damage_amt
        if self.health < 1:
            print("TERMINATED!", self.name)
            self.deaths += 1

    def add_kill(self, num_kills):
        print("EXTERMINATED!")
        self.kills += num_kills
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    def attack(self):
        random_int = random.randint(0, self.damage)
        return random_int
class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.villains = list()
        team_list.append(self)

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
            print(i.name, " number 1")

    def attack(self, other_team):
        sum = 0
        for i in self.villains:
            sum += i.attack()
            if i.weapons != None:
                for n in i.weapons:
                    sum += n.attack()
        for i in other_team.villains:
            sum -= i.defend()
        if sum > 0:
            other_team.deal_damage(sum)
            for i in other_team.villains:
                if i.deaths > 0:
                    for v in self.villains:
                        v.kills += i.deaths
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

    def revive_heroes(self, health):
        for i in self.villains:
            i.health = health

    def stats(self):
        for i in self.villains:
            print(i.name, "kills", i.kills)
            print(i.name, "deaths", i.deaths)

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
    def __init__(self, team_one, team_two):
        self.team_one = team_one
        self.team_two = team_two
        self.team_one_score = 0
        self.team_two_score = 0

    def build_team_one(self):
        self.team_one = raw_input("Choose team one: ")

    def build_team_two(self):
        self.team_two = raw_input("Choose team two: ")

    def team_battle(self):
        ran_int = random.randint(1, 2)
        if ran_int == 1:
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
        elif ran_int == 2:
            self.team_two.attack(self.team_one)
            self.team_one.attack(self.team_two)
        else:
            print("I say 'HEY'! What's going on?!")
        print(self.show_stats())
        if self.team_one_score > self.team_two_score:
            print("And the winner is... ")
            print(self.team_one.team_name)
        elif self.team_two_score > self.team_one_score:
            print("And the winner is... ")
            print(self.team_two.team_name)
        else:
            print("It's a... TIE?!?! Lame! Play again!")
    def show_stats(self):

        for i in self.team_one.villains:
            print(i.name, "kills", i.kills)
            self.team_one_score += i.kills
            print(i.name, "deaths", i.deaths)
            self.team_one_score -= i.deaths
        for n in self.team_two.villains:
            print(n.name, "kills", n.kills)
            self.team_two_score += i.kills
            print(n.name, "deaths", n.deaths)
            self.team_two_score -= i.deaths
class Amulet:
    def __init__(self, name, number, possessor):
        self.name = name
        self.number = number
        self.possessor = possessor
    def revive(self):
        if self.number = 1:
            self.possessor.revive_heroes(100)
            self.possessor = None
        else:
            print("Trying to use an amulet you don't possess? Naughty, naughty.")
    def whipe_out(self):
        if self.number = 1:
            #Deal a crushing blow!
        else:
            print("Are you trying to kill your enemies without the amulet?! Me thinks I smell a cheater...")

def team_generator():
    team = Team(raw_input("Choose your team name: "))
    vil1 = Villain(raw_input("Name your first villain: "))
    ability1 = Ability(raw_input("Give your first villain an ability: "), float(raw_input("How powerful is it? (Must be a number) ")))
    weapon1 = Weapon(raw_input("Now they need a weapon. Give your first villain a weapon: "), float(raw_input("How powerful is it? ")))
    vil1.add_ability(ability1)
    vil1.add_weapon(weapon1)
    vil2 = Villain(raw_input("Name your second villain: "))
    ability2 = Ability(raw_input("Give your second villain an ability: "), float(raw_input("How powerful is it? ")))
    weapon2 = Weapon(raw_input("Give your second villain a weapon: "), float(raw_input("How powerful is it? ")))
    vil2.add_ability(ability2)
    vil2.add_weapon(weapon2)
    vil3 = Villain(raw_input("Name your third villain: "))
    ability3 = Ability(raw_input("Give your third villain an ability: "), float(raw_input("How powerful is it? ")))
    weapon3 = Weapon(raw_input("Give your third villain a weapon: "), float(raw_input("How powerful is it? ")))
    vil3.add_ability(ability3)
    vil1.add_weapon(weapon3)
    ability4 = Ability(raw_input("Hell, give your third villain another ability. They're a real baddy: "), float(raw_input("How powerful is it? ")))
    vil1.add_ability(ability4)
    team.add_villain(vil1)
    team.add_villain(vil2)
    team.add_villain(vil3)
    print("Great! We're almost done. Now we want to send your villains into battle. Here's a list of their enemies, with numbers corresponding to each one.")
    for i in range(0, len(team_list)-1):
        if team_list[i].team_name == team.team_name:
            pass
        else:
            print(i, team_list[i].team_name)
    other_team = input("Type the number corresponding to the team you'd like them to take on in mortal combat! ")
    print("And now we just...")
    inty = 0
    for i in range(0, len(team_list)-1):
        if i == other_team:
            enemy_team = team_list[i]
            inty = 1
    if inty == 0:
        print("That's wrong. You screwed it up. You've ruined us all!!")
    user_arena = Arena(team, enemy_team)
    print("Let them fight!")
    print(user_arena.team_battle())

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
shield = Armor("Captain America's Shield", 1800)
thanos.add_armor(shield)
dark_shield = Armor("Dark Shield", 1800)
darkside.add_armor(dark_shield)
print(team_exterminate.view_all_villains())
print(team_subordinate.view_all_villains())
print(team_subordinate.attack(team_exterminate))
print(team_exterminate.attack(team_subordinate))
print(team_subordinate.stats())
new_arena = Arena(team_subordinate, team_exterminate)
print(new_arena.team_battle())
team_generator()
