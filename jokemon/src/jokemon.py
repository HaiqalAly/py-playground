import random

class Jokemon:
    def __init__(self, name, type, hp=100, strength=20):
        self.name = name
        self.type = type
        self.hp = hp
        self.strength = strength

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            return self.faint()
        return f"{self.name} took {amount} damage! HP is now {self.hp}."

    def attack(self, opponent):
        # Calculate damage
        damage = self.strength + random.randint(-5, 5)
        print(f"{self.name} attacks {opponent.name} with {self.type} power!")
        return opponent.take_damage(damage)

    def faint(self):
        return f"{self.name} has fainted!"

class Battle:
    def __init__(self, jokemon1: Jokemon, jokemon2: Jokemon):
        self.jokemon1 = jokemon1
        self.jokemon2 = jokemon2
        self.turn = 0

    def play_round(self):
        # Determine who is attacking and who is defending
        attacker = self.jokemon1 if self.turn % 2 == 0 else self.jokemon2
        defender = self.jokemon2 if self.turn % 2 == 0 else self.jokemon1
        
        result = attacker.attack(defender)
        self.turn += 1
        return result

    def is_over(self):
        return self.jokemon1.hp <= 0 or self.jokemon2.hp <= 0