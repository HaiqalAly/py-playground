import random

TYPE_CHART = {
    "Grass": {"Grass": 1.0, "Water": 2.0, "Fire": 0.5},
    "Fire": {"Grass": 2.0, "Water": 0.5, "Fire": 1.0},
    "Water": {"Grass": 0.5, "Water": 1.0, "Fire": 2.0},
}
    
class Battle:
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            return f"{self.name} took {amount} damage! {self.faint()}"
        return f"{self.name} took {amount} damage! HP is now {self.hp}."
    
    def multiplier(self, atk_type, def_type):
        return TYPE_CHART.get(atk_type, {}).get(def_type, {})

    def faint(self):
        return f"{self.name} has fainted!"
    
class Jokemon(Battle):
    def __init__(self, name, type, hp=100, strength=20):
        self.name = name
        self.type = type
        self.hp = hp
        self.strength = strength

    def attack(self, opponent):
        # Type effectiveness
        multiplier = self.multiplier(self.type, opponent.type)

        # Calculate damage
        damage = self.strenght + random.randint(-5, 5)
        total_damage = int(damage * multiplier)

        if multiplier > 1: print("It's super effective!")
        elif multiplier < 1: print("It's not very effective...")

        print(f"{self.name} attacks {opponent.name} with {self.type} power!")
        return opponent.take_damage(total_damage)

class Game:
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