import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Enter the number: "))
        if guess < random_number:
            print("You are too low, Try Again")
        elif guess > random_number:
            print("You are too high, try again")
    print(f"congrats, You guessed the right number {random_number}")

guess(5)