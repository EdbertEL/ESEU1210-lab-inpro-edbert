import random

def hangman(secretWord):
    guess = ""
    lives = 6

    while lives > 0:
        # Display word
        count = 0
        for char in secretWord:
            if char.lower() in guess.lower():
                print(char, end="")
            else:
                print("_", end="")
                count += 1
        if count == 0:
            print("\nThe word is \"", secretWord, "\". You won!", sep="")
            break
        # Check word
        userinput = input("\nYour guess: ")
        if len(userinput) != 1:
            print("You can only guess ONE letter at once!")
        elif userinput.lower() in guess:
            print("You already guessed that letter.")
        else:
            guess += userinput
            if userinput.lower() not in secretWord.lower():
                lives -= 1
                if lives == 0:
                    print("You lost! Try again next time. The word was",secretWord)
                else:
                    print("Guess again! You only have {} \u2764\uFE0F  left.".format(lives))

word_list = list(open('kamuskata.txt'))
word = random.choice(word_list).rstrip("\n")

hangman(word)
            