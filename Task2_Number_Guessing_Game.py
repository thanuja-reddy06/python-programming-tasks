import random

def guessing_game():
    number = random.randint(1, 100)
    print("Guess the number between 1 and 100!")

    while True:
        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct! 🎉")
            break

guessing_game()
