"""Program Name: Lab9-emaliugina-1.py
   Author: Elizaveta Maliugina
   Purpose: Runs the main game. Creates the Player objects and manages the game loop and rules.
   Date: 9/26/2026"""

from player import Player
from coin import Coin

def main():
    """Function that runs the game using the Player class and a while loop, as well as multiple if-else statements and variables."""
    my_coin = Coin()

    player1 = Player("Player 1", 20, my_coin)
    player2 = Player("Player 2", 20, my_coin)

    print("--- Coin Match Game ---")

    print(f"{player1.get_name()} wallet: {player1.get_wallet()} coins")
    print(f"{player2.get_name()} wallet: {player2.get_wallet()} coins")

    play_again = input(f"\nDo you want to play? (y/n):  ")
    while play_again.lower() == 'y':
        print("\nTossing...")

        if player1.get_wallet() <=0:
            print(f"\nGame Over! {player1.get_name()} has 0 coins and loses!")
            break
        elif player2.get_wallet() <=0:
            print(f"\nGame Over! {player2.get_name()} has 0 coins and loses!")
            break

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"\n{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print(f"\n...Match! {player1.get_name()} wins this round.")
        else:
            player2.win_coin()
            player1.lose_coin()
            print(f"\n...No match! {player2.get_name()} wins this round.")

        print(f"\n{player1.get_name()} wallet: {player1.get_wallet()} coins")
        print(f"{player2.get_name()} wallet: {player2.get_wallet()} coins")

        play_again = input("\nDo you want to play another round? (y/n):  ")

    print("\n=== Final Results ===")

    p1_coins = player1.get_wallet()
    p2_coins = player2.get_wallet()

    print(f"\n{player1.get_name()}: {p1_coins}")
    print(f"{player2.get_name()}: {p2_coins}")

    if p1_coins > p2_coins:
        print(f"Winner: {player1.get_name()}!")
    elif p2_coins > p1_coins:
        print(f"Winner: {player2.get_name()}!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()