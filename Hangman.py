
word = "Programming"
guess = ""
lives = 6

while lives > 0:
    count = 0
    for char in word:
        if char.lower() in guess.lower():
            print(char, end="")
        else:
            print("_", end="")
            count += 1
    if count == 0:
        print("\nThe word is \"", word, "\". You won!", sep="")
        break

    userinput = input("\nYour guess: ")
    if len(userinput) != 1:
        print("You can only guess ONE letter at once!")
    elif userinput.lower() in guess:
        print("You already guessed that letter.")
    else:
        guess += userinput
        if userinput.lower() not in word.lower():
            lives -= 1
            if lives == 0:
                print("You lost! Try again next time.")
            else:
                print("Guess again! You only have {} \u2764\uFE0F  left.".format(lives))
            