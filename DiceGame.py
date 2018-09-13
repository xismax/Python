"""The program should do the following:
Roll a pair of dice.
Add the values of the roll.
Ask the user to guess a number.
Compare the user's guess to the total value.
Determine the winner (user or computer)."""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(input("Guess a number: "))
  return guess
  
def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides * 2
  print ("The maximum possible value is: %d" % max_val)
  guess = get_user_guess()
  if guess > max_val:
  	print ("No guessing higher than the maximum possible value!")
  else:
    print ("Rolling...")
    sleep(2)
    print ("The 1st roll is: %d" % first_roll)
    sleep(1)
    print ("The 2nd roll is: %d" % second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print ("The total value is: %d" % total_roll)
    print ("Result...")
    sleep(1)
    if guess == total_roll:
    	print ("You won!!!")
    else:
      print ("Sorry, you loose, better luck next time.")
    
roll_dice(6)