import random

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q"]

computer_cards = []
computer_total = 0

player_cards = []


game = True

def calc_cards(array):
    total = 0
    for card in array:
        ace = False
        if card in ("J", "K", "Q", "10"):
            total += 10
        elif card == "A":
            ace = True
        else:
            value = int(card)
            total += value
        if ace == True:
            if total + 11 > 21:
                total += 1
            else:
                total += 11   
    return total

while game:
    computer_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    print(computer_cards)
    print(player_cards)
    player_tot = calc_cards(player_cards)
    print(player_tot)
    calc_cards(player_cards)
    while player_tot < 21:
      hit = input("Do you want to hit? y/n: ")
      if hit.lower() == "y" and player_tot < 21:
          player_cards.append(random.choice(cards))
          print(player_cards)
          player_tot = calc_cards(player_cards)
          print(player_tot)
    print("End")
    if player_tot > 21:
        print("You Lose!")
        game = False
        again = input("Play again? y/n")
        if again == "y":
            player_cards = []
            computer_cards = []
            game = True
    elif player_tot == 21:
        print("BLACKJACK!")
        game = False
        again = input("Play again? y/n")
        if again == "y":
            player_cards = []
            computer_cards = []
            game = True
    
