
guesses = 0
guessed_letters = []
word = "programmer"


while guesses < 5:
    guess = input("Hi. Please guess a letter.")

    if set(word).intersection(set(guessed_letters)) == set(word):
        break

    if guess in word and guess not in guessed_letters:
        print("Correct!")
        guessed_letters.append(guess)
        print("So far you've used ", guessed_letters, "as letters.")
        print("You've got",5-guesses,"guesses left.")

    elif guess not in word and guess not in guessed_letters:
        guesses += 1
        print("Wrong!")
        guessed_letters.append(guess)
        print("So far you've used ", guessed_letters, "as letters.")
        print("You've got",5-guesses,"guesses left.")

    elif guess in guessed_letters:
        print("You've already guessed that letter, please guess again.")

    else:
        print("ERROR")

if set(word).intersection(set(guessed_letters)) == set(word):
    print("You won! The word is \'{}\'".format(word))
else:
    print("You lost. The word is \'{}\'".format(word))
