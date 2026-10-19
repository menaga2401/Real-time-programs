#4th program-Number Guessing Game
import random

number=random.randint(1,10)
guess=int(input("Guess a number from 1 and 10:"))
if guess == number:
          print("Congrats! You guessed correctly.")
else:
    print("Wrong guess!")
    print("The correct number is",number)
