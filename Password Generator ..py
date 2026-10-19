#3rd program-Password Generator
import random
import string

characters = string.ascii_letters + string.digits
password=""

for i in range(5):
    password = password + random.choice(characters)

print("Generated Password:",password)
