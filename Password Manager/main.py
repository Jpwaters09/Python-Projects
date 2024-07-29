################################################
## Password Manager                           ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2024 Jacob Waters            ##
## Contact me: jpwaters.github@gmail.com      ##
################################################

from os import system
from time import sleep
from cryptography.fernet import Fernet
import platform

system('pip install cryptography')

if platfrom.system() == "Windows":
  def clear():
    system('cls')
elif platfrom.system() == "Linux":
  def clear():
    system('clear')

elif platfrom.system() == "Darwin":
  def clear():
    system('clear')

def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)

######## Delete the "#" before write_key() to generate a new key then replace it after you have run the code #########
#write_key()                                                                                                         #
######################################################################################################################

def load_key():
  file = open("key.key", "rb")
  key = file.read()
  file.close()
  return key

clear()
print("Password Manager:")

sleep(2)
clear()

m_passwd = input("Please Type a Master Password? ")

clear()

print("Master Password Set!")

sleep(2)
clear()

while True:
  passwd = input("What Is The Master Password? ")

  if passwd == m_passwd:
    clear()
    print("Master Password Correct!")
    sleep(2)
    clear()
    break
  else:
    clear()
    print("Master Password Incorrect, Please Try Again!")
    sleep(4)
    clear()
    while True:
      break

key = load_key()
fer = Fernet(key)

clear()


def view():
  with open("passwords.txt", "r") as f:
    for line in f.readlines():
      accounts = line.rstrip()
      user, passwd = accounts.split("|")
      print("User Name:",
      fer.decrypt(user.encode()).decode(), "|", "Password:",
      fer.decrypt(passwd.encode()).decode())


def add():
  a_name = input("Account Name: ")
  a_passwd = input("Password: ")

  with open("passwords.txt", "a") as f:
    f.write(fer.encrypt(a_name.encode()).decode() + "|" + fer.encrypt(a_passwd.encode()).decode() + "\n")


while True:
  print("Type a To Add a New Password.")
  print("Type v To View Existing Passwords.")
  print("Type l To Lock The Password Manager.")
  print("Press q To Quit.\n")
  mode = input().lower()
  if mode == "l":
    clear()
    lock = input("Do You Want To Lock The Password Manager [Y/n]? ").lower()
    if lock == "y":
      clear()
      m_lock = input("What is The Master Password? ")
      if m_lock == m_passwd:
        clear()
        while True:
          clear()
          s_lock = input("Password Manager is Locked, Press u To Unlock? ")
          if s_lock == "u":
            clear()
            ms_lock = input("What is The Master Password? ")
            if ms_lock == m_passwd:
              clear()
              break

            else:
              clear()
              print("Incorrect Master Password, Please Try Again!")
              sleep(4)
              clear()
              while True:
                break

      else:
        clear()
        print("Incorrect Master Password, Please Try Again!")
        sleep(4)
        clear()
        
    if lock == "n":
      clear()
      while True:
        break

  if mode == "q":
    clear()
    quit = input("Do You Want To Quit [Y/n]? ").lower()
    if quit == "n":
      clear()
      while True:
        break
    if quit == "y":
      clear()
      m_quit = input("What is The Master Password? ")
      if m_quit == m_passwd:
        clear()
        break
      else:
        clear()
        print("Incorrect Master Password, Please Try Again!")
        sleep(4)
        clear()

  if mode == "v":
    clear()
    while True:
      v_passwd = input("What is The Master Password? ")
      if v_passwd == m_passwd:
        clear()
        print("Accounts:")
        view()
        v_view = input("\nPress b To Go Back? ").lower()
        clear()
        if v_view == "b":
          break
            
      else:
        clear()
        print("Incorrect Master Password, Please Try Again!")
        sleep(4)
        clear()
        break

  if mode == "a":
    clear()
    a_passwd = input("What is The Master Password? ")
    if a_passwd == m_passwd:
      clear()
      add()
      clear()
      print("Account Added!")
      sleep(2)
      clear()
    else:
      clear()
      print("Incorrect Master Password, Please Try Again!")
      sleep(4)
      clear()

  if mode != "a" and "v" and "q" and "l":
    clear()
