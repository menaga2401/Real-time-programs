#6th program-Hangman game
word = "Menagah"
guessed = ""

while True:
    letter = input("Guess a letter:")

    if letter in word:
        guessed = guessed + letter
        print("Correctly guessed!")
    else:
        print("Wrongly guessed!")

    result = ""

    for ch in word:
        if ch in guessed:
            result = result + ch + ""
        else:
            result = result + "_"


