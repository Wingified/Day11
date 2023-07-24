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

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

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
      
    
  
  




    
  
  
