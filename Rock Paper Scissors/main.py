##############################################
# Rock Paper Scissors                        #
# Author: Jacob Waters                       #
# Github: github.com/jpwaters09              #
# Contact me: jpwaters.github@gmail.com      #
# Follow my WhatsApp Channel: bit.ly/3sr99ZO #
##############################################

from os import system
from time import sleep
import random

########## Type windows / linux in the quotation marks depending on you operating system ##########
WindowsOrLinux = "windows"                                                                        #
###################################################################################################

if WindowsOrLinux == "windows":
  def clear():
    system('cls')
elif WindowsOrLinux == "linux":
  def clear():
    system('clear')

clear()
user_wins = 0
computer_wins = 0
options = ["r", "p", "s"]

print("Rock Paper Scissors:")
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
    sleep(4)
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
