word = "programming"
guess = ''

while True:
    count = 0
    for char in word:
        if char in guess:
            print(char, end="")
        else:
            print("_", end="")
            count += 1
    if count == 0:
        print("\nThe word is \"", word, "\". You won!", sep="")
        break

    userinput = input("\nYour guess: ")
    if len(userinput) > 1:
        print("You can only guess ONE letter at once!")
    else:
        guess += userinput.lower()
        if userinput.lower() not in word:
            print("Guess again!")