SECRET = 7
guesses = 0
while True:
    guess = int(input("Guess: "))
    guesses += 1
    if guess < SECRET:
        print("Too low")
    elif guess > SECRET:
        print("Too high")
    else:
        print("Correct!")
        break
print("Guesses:", guesses)
