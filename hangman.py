import random

words = ["banana","trade","water","machine","rotate","military","communication","vegetable","rocket","stone","dictionary","bee","power","life","balance","country","economy"]

def hangman():
    word = random.choice(words)
    word_length = len(word)
    display = ["_"] * word_length
    guessed = False
    guessed_letters = []
    tries = 7
    pointer_position = 0

    print("HANGMAN")
    print(" " * pointer_position + "^")

    while not guessed and tries > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You have already guessed the letter", guess)
        elif guess not in word:
            print(guess, "is not in the word.")
            tries -= 1
            pointer_position += 1
            guessed_letters.append(guess)
        else:
            print("Good job,", guess, "is in the word!")
            guessed_letters.append(guess)
            for i in range(word_length):
                if word[i] == guess:
                    display[i] = guess

        print("HANGMAN")
        print(" " * pointer_position + "^")
        print(" ".join(display))
        print("\n")

        if "_" not in display:
            guessed = True

    if guessed:
        print("Phew… you are saved")
    else:
        print("You are hanged. The word was " + word)

def play_again():
    while True:
        answer = input("Would you like to play again? (y/n): ").lower()
        if answer == "y":
            hangman()
        elif answer == "n":
            break
        else:
            print("Invalid input. Please enter yes or no.")

hangman()
play_again()
