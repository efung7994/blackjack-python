import random
import os

clear = lambda: os.system('clear')

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



def blackjack():
  cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q"]

  computer_cards = []
  player_cards = []
  game = True
  while game:
      computer_cards.append(random.choice(cards))
      player_cards.append(random.choice(cards))
      player_cards.append(random.choice(cards))
      player_total = calc_cards(player_cards)
      computer_total = calc_cards(computer_cards)
      calc_cards(player_cards)
      print(f"Player Cards: {player_cards}")
      print(f"Player Total: {player_total}")
      print(f"Computer Cards: {computer_cards}")
      print(f"Computer Total: {computer_total}")
      while player_total < 21:
        hit = input("Do you want to hit? y/n: ")
        if hit.lower() == "y" and player_total < 21:
            clear()
            player_cards.append(random.choice(cards))
            player_total = calc_cards(player_cards)
            print(f"Player Cards: {player_cards}")
            print(f"Player Total: {player_total}")
            print(f"Computer Cards: {computer_cards}")
            print(f"Computer Total: {computer_total}")
        else:
            break
      if player_total > 21:
          print("You Lose!")
          again = input("Play again? y/n: ")
          if again == "y":
              player_cards = []
              computer_cards = []
              player_total = 0
              computer_total = 0
              clear()
              blackjack()
          else: 
              break
      elif player_total == 21:
          print("BLACKJACK!")
          again = input("Play again? y/n: ")
          if again == "y":
              player_cards = []
              computer_cards = []
              player_total = 0
              computer_total = 0
              clear()
              blackjack()
          else:
              break
      while computer_total < player_total or computer_total <= 17:
          computer_cards.append(random.choice(cards))
          computer_total = calc_cards(computer_cards)
      if computer_total > 21:
          clear()
          print(f"Player Cards: {player_cards}")
          print(f"Player Total: {player_total}")
          print(f"Computer Cards: {computer_cards}")
          print(f"Computer Total: {computer_total}")
          print("You win!")
          again = input("Play again? y/n: ")
          if again == "y":
              player_cards = []
              computer_cards = []
              player_total = 0
              computer_total = 0
              clear()
              blackjack()
          else:
              break
      elif computer_total > player_total:
          clear()
          print(f"Player Cards: {player_cards}")
          print(f"Player Total: {player_total}")
          print(f"Computer Cards: {computer_cards}")
          print(f"Computer Total: {computer_total}")
          print("You Lose!")
          again = input("Play again? y/n: ")
          if again == "y":
              player_cards = []
              computer_cards = []
              player_total = 0
              computer_total = 0
              clear()
              blackjack()
          else:
              break
    
blackjack()