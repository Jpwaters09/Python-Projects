##############################################
# Computer Quiz                              #
# Author: Jacob Waters                       #
# Github: github.com/jpwaters09              #
# Contact me: jpwaters.github@gmail.com      #
# Follow my WhatsApp Channel: bit.ly/3sr99ZO #
##############################################

from os import system
from time import sleep

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
print("Computer Quiz:")
sleep(2)
clear()

input("Press enter To Start: ")
clear()

score = 0

print("Question 1!")
sleep(4)
clear()

answer = input("What Does CPU Stand For? ")

if answer.lower() == "central processing unit":
  score += 1
  clear()
  print("Correct!")
  print("\nYou Have Got " + str(score) + "/4 Questions Correct So Far!")
  print("\nYou Have Got " + str((score/4) * 100) + "% Correct So Far!")
  sleep(2)
  clear()
  
else:
  clear()
  print("Incorrect!")
  print("\nYou Have Got " + str(score) + "/4 Questions Correct So Far!")
  print("\nYou Have Got " + str((score/4) * 100) + "% Correct So Far!")
  sleep(4)
  clear()

print("Question 2!")
sleep(4)
clear()

answer = input("What Does GPU Stand For? ")

if answer.lower() == "graphics processing unit":
  score += 1
  clear()
  print("Correct!")
  print("\nYou Have Got " + str(score) + "/4 Questions Correct So Far!")
  print("\nYou Have Got " + str((score/4) * 100) + "% Correct So Far!")
  sleep(2)
  clear()

else:
  clear()
  print("Incorrect!")
  print("\nYou Have Got " + str(score) + "/4 Questions Correct So Far!")
  print("\nYou Have Got " + str((score/4) * 100) + "% Correct So Far!")
  sleep(4)
  clear()

print("Question 3!")
sleep(4)
clear()

answer = input("What Does RAM Stand For? ")

if answer.lower() == "random access memory":
  score += 1
  clear()
  print("Correct!")
  print("\nYou Have Got " + str(score) + "/4 Questions Correct So Far!")
  print("\nYou Have Got " + str((score/4) * 100) + "% Correct So Far!")
  sleep(2)
  clear()

else:
  clear()
  print("Incorrect!")
  print("\nYou Have Got " + str(score) + "/4 Questions Correct So Far!")
  print("\nYou Have Got " + str((score/4) * 100) + "% Correct So Far!")
  sleep(4)
  clear()

print("Question 4!")
sleep(4)
clear()

answer = input("What Does PSU Stand For? ")

if answer.lower() == "power supply unit":
  score += 1
  clear()
  print("Correct!")
  print("\nYou Have Got " + str(score) + "/4 Questions Correct So Far!")
  print("\nYou Have Got " + str((score/4) * 100) + "% Correct So Far!")
  sleep(2)
  clear()

else:
  clear()
  print("Incorrect!")
  print("\nYou Have Got " + str(score) + "/4 Questions Correct So Far!")
  print("\nYou Have Got " + str((score/4) * 100) + "% Correct So Far!")
  sleep(4)
  clear()

print("End Of Computer Quiz!")
sleep(4)

print("\nYou Have Got " + str(score) + "/4 Questions Correct!")
sleep(1)
print("\nYou Have Got " + str((score/4) * 100) + "% Correct!")
sleep(2)

if score == 4:
  clear()
  print("Well Done You Have Got 100.0%!")
  sleep(1)
  print("\nYou Won!")
  sleep(2)
  clear()

else:
  clear()
  print("Please Try The Computer Quiz Again!")
  sleep(1)
  print("\nYou Lost!")
  sleep(2)
  clear()
