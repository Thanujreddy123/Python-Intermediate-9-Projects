#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
print("Welcome to the Number Guessing Game!")
gametype=input("You want hard or easy:->")
lifeline=0
if gametype=="hard":
  lifeline=5
else:
  lifeline=10
import random
number=random.randint(1,100)
flag=False
while lifeline>0 and not flag:
  guess=int(input("Guess a number from 1 to 100: "))
  if guess==number:
    print(f"you found it you won the number is {number}")
    flag=True
  elif guess>number:
    print("Too high")
    lifeline-=1
    print(f"you have only{lifeline}")
  else:
    print("Too low")
    lifeline-=1
    print(f"you have only{lifeline}")

if lifeline==0:
  print("you lost the game")
    

