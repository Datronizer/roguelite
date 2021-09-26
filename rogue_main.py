import random
import math
import os

class Entity:
    def __init__(self, name, health, strength, agility, intelligence):
        """Constructs all base and tertiary stats."""
        # These are the main stats. Most stats stem from this.
        self.name = name
        self.health = health    # Starting health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

        # These are the derived stats. These will be subject to change.
        self.bonus_health = strength
        self.armor = agility
        self.mana = intelligence
        self.insight = math.ceil(intelligence * (1.5 - random.random()))

class Player(Entity):
    def statcheck(self):
        print("{} is an player with: {} strength, {} agility, {} intelligence.".format(self.name, self.strength, self.agility, self.intelligence))
        print("{} has {} starting HP and {} starting MP\n".format(self.name, self.health, self.mana))

class Enemy(Entity):
    def analyze(self, insight):
        if insight < 4: # Might change this to a variable to make things unpredictable
            print("Your insight is too low to analyze this enemy. You need at least 4. You have {}.".format(insight))
        elif insight > 4:
            print("{} is an enemy with: {} strength, {} agility, {} intelligence.".format(self.name, self.strength, self.agility, self.intelligence))
            if insight > 7:
                print("{} currently has {} HP and {} MP\n".format(self.name, self.health, self.mana))

class Event:
    def __init__(self, list_of_entities_involved):
        self.list_of_entities_involved = list_of_entities_involved # Must include 1 player
    def participants(self):
        for entity in self.list_of_entities_involved:
            print(type(entity))
    def initcombat(self):
        """Starts combat and analyzes the attack order"""
        attackorder = sorted(self.list_of_entities_involved, key = lambda participant: participant.agility, reverse = True)
        return attackorder

# Player1 = Player('Erith', 80, 8, 11, 11)
# Player1.statcheck()

Player2 = Player('Yobungus', 150, 16, 10, 4)
Player2.statcheck()

# Entity1 = Entity('Dingus', 100, 10, 7, 4)
# Entity1.analyze(Player1.insight)

# Entity2 = Entity('Bobingus', 50, 2, 13, 3)
# Entity2.statcheck()

Enemy1 = Enemy('Big Rat', 10, 1, 3, 0)
# Enemy1.analyze(Player1.insight)
Enemy1.analyze(Player2.insight)

Encounter = Event([Player2, Enemy1])
# Encounter.participants()
print(Encounter.initcombat())
