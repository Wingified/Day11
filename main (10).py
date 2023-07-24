############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
#Removed, didn't use.

#Code Below -----------------------------------------------------------------------------------
import art
game_start = input("Would you like to play Blackjack? Y or N: ").lower()
if game_start == "y":
  print(art.logo)
else:
  print("nerd")

import random
from replit import clear
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
card1 = (random.choices(cards))
card2 = (random.choices(cards))
card3 = (random.choices(cards))

cpucard1 = (random.choices(cards))
cpucard2 = (random.choices(cards))
cpucard3 = (random.choices(cards))
cpucard4 = (random.choices(cards))
conversion = [ int(card1) for card1 in cards ]

card_total = sum(card1 + card2)
cpucard_total = sum(cpucard1 + cpucard2)

card_total2 = sum(card1 + card2 + card3)
cpucard_total2 = sum(cpucard1 + cpucard2 + cpucard3)

print(f"Your cards: {card1}, {card2}  Score: {card_total}")
print(f"CPU's first card: {cpucard1} ")

if cpucard_total == 21:
  print("CPU wins!")
else:
  if card_total == 21:
    print("Blackjack. You win!") 
  if card_total2 == 21:
    print("Blackjack. You win!") 

ace = cards[12]
if ace + card_total > 21:
  ace=1
if ace + cpucard_total > 21:
  ace=1

card_draw = input("Draw another card? Y or N: ").lower()
if card_draw == "y":
  print(f"Your score is now {card_total2}")
else:
  print("Understood.")
print("The CPU is now drawing cards")
while cpucard_total2 < 16:
  cpucard_total2 + random.choice(cards)
print(f"The CPU's score is now {cpucard_total2}")
if card_draw == "y":
  card_total = card_total2

if card_total == cpucard_total2:
  print("Tie game!")
if cpucard_total2 < 21:
  if card_total > 21:
    print("You went over. You lose!")
  elif card_total < 21:
    if card_total > cpucard_total2:
      print("You have the closer score. You win!")
    elif card_total < cpucard_total2:
      print("The CPU has the closer score. You lose!")

if cpucard_total2 > 21:
  if card_total < 21:
    print("The CPU went over. You win!")
  elif card_total > 21:
      if card_total > cpucard_total2:
        print("The CPU has the closer score. You lose!")
      elif card_total < cpucard_total2:
        print("You havye the closer score. You win!")

playagain = input("Play again? Y or N").lower()
if playagain == "y":
  clear()
  print("Restart game because I forgot to define play_again. ")
      
    
  
  




    
  
  
