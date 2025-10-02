# dice.py
import random 
input("\nPress ENTER to roll the dice..")
class Dice:

    def rollD4(self):
        """Roll a 4-sided dice (D4)"""
        return random.randint(1, 4)
        
    def rollD6(self):
        """Roll a 6-sided dice (D6)"""
        return random.randint(1, 6)

    def rollD8(self):
        """Roll an 8-sided dice (D8)"""
        return random.randint(1, 8)

    def rollD12(self):
        """Roll a 12-sided dice (D12)"""
        return random.randint(1, 12)

    def rollD20(self):
        """Roll a 20-sided dice (D20)"""
        return random.randint(1, 20)

    def rollD100(self):
        """Roll a 100-sided dice (D100)"""
        return random.randint(1, 100)
