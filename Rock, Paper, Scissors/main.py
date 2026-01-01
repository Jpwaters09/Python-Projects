################################################
## Rock, Paper, Scissors                      ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2026 Jacob Waters            ##
## Contact me: jpwaters09.business@gmail.com  ##
################################################

from os import system
from time import sleep
import random
import platform

if platform.system() == "Windows":
  def clear():
    system('cls')
    
elif platform.system() == "Linux":
  def clear():
    system('clear')

elif platform.system() == "Darwin":
  def clear():
    system('clear')

clear()
user_wins = 0
computer_wins = 0
options = ["r", "p", "s"]

print("Rock, Paper, Scissors:")
sleep(2)
clear()

input("Press enter to start: ")
clear()

while True:
  user_input = input("Type r for Rock, p for Paper, s for Scissors, v To View Results: ").lower()
  if user_input == "v":
    clear()
    break
  if user_input not in options:
    clear()
    print("Please Type r, p, s!")
    sleep(4)
    clear()
    continue
  random_number = random.randint(0, 2)
  computer_pick = options[random_number]
  print("\nComputer Picked", computer_pick + ".")
  if user_input == computer_pick:
    print("\nIt Was a Draw!")
    sleep(2)
    clear()
  elif user_input == "r" and computer_pick == "s":
    print("\nYou Won!")
    user_wins += 1
    sleep(2)
    clear()
  elif user_input == "p" and computer_pick == "r":
    print("\nYou Won!")
    user_wins += 1
    sleep(2)
    clear()
  elif user_input == "s" and computer_pick == "p":
    print("\nYou Won!")
    user_wins += 1
    sleep(2)
    clear()
  else:
    print("\nYou Lost!")
    computer_wins += 1
    sleep(2)
    clear()

print("You Won", user_wins, "Time/s.")
sleep(2)
print("\nThe Computer Won", computer_wins, "time/s.")

if user_wins == computer_wins:
  sleep(4)
  clear()
  print("It Was a Draw!")
  sleep(2)
  clear()
elif user_wins > computer_wins:
  sleep(4)
  clear()
  print("You Won!")
  sleep(2)
  print("\nThe Computer Lost!")
  sleep(4)
  clear()
elif computer_wins > user_wins:
  sleep(4)
  clear()
  print("The Computer Won")
  sleep(4)
  print("\nYou Lost!")
  sleep(4)
  clear()
