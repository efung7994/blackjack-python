import random

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q"]

computer_cards = []
computer_total = 0

player_cards = []
player_tot = 0

game = True

def calc_player_cards():
    player_total = 0
    for card in player_cards:
        ace = False
        if card in ("J", "K", "Q", "10"):
            player_total += 10
        elif card == "A":
            ace = True
        else:
            value = int(card)
            player_total += value
        if ace == True:
            if player_total + 11 > 21:
                player_total += 1
            else:
                player_total += 11
    player_tot = player_total            
    print(player_tot)

while game:
    computer_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    print(computer_cards)
    print(player_cards)
    draw = True
    while draw:
      calc_player_cards()
      while player_tot < 21:
        hit = input("Do you want to hit? y/n: ")
        if hit.lower() == "y" and player_tot < 21:
            player_cards.append(random.choice(cards))
            print(player_cards)
            calc_player_cards()
        else:
            draw = False
    print(player_tot)


    for card in computer_cards:
        ace = False
        if card in ("J", "K", "Q", "10"):
            computer_total += 10
        elif card == "A":
            ace = True
        else:
            value = int(card)
            computer_total += value
    
