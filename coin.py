"""Program Name: coin.py
   Author: Elizaveta Maliugina
   Purpose: Create a coin class that represents a single, tossable coin for lab 2.
   Date: 9/26/2026"""

import random

class Coin:
    def __init__(self, sideup="Heads"):
        self.sideup = sideup
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = "Heads"
        else:
            self.side_up = "Tails"
    def get_sideup(self):
        return self.sideup
