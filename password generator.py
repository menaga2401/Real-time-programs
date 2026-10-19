#3rd program-Password Generator
import random
import string

characters = string.ascii_letters + string.digits
password=""

for i in range(5):
    password = password + random.choice(characters)

print("Generated Password:",password)

#5th program-Rock,paper,scissor game

#import random
user = input("Enter rock, paper, or scissors:")
computer = random.choice(["rock", "paper", "scissors"])
print("Computer choice:",computer)

if user == computer:
    print("It's a tie!")
elif user == "rock" and computer == "scissors":
    print("You Win!")
elif user == "scissors" and computer == "paper":
    print("You Win!")
elif user == "paper" and computer == "rock":
    print("You Win!")
else:
    #print("Computer wins!")
