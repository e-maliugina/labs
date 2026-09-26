"""Program Name: player.py
   Author: Elizaveta Maliugina
   Purpose: Creates a class that represents a player. A player has a name, has a wallet of coins, and has a Coin object to toss.
   Date: 9/26/2026"""

from coin import Coin

class Player:
    def __init__(self, name, wallet, coin):
        self.name = name
        self.wallet = wallet
        self.__coin = coin
    def toss_coin(self):
        self.__coin.toss()
    def get_coin_side(self):
        return self.__coin.get_sideup()
    def win_coin(self):
        self.wallet += 1
    def lose_coin(self):
        self.wallet -= 1
    def get_wallet(self):
        return self.wallet
    def get_name(self):
        return self.name