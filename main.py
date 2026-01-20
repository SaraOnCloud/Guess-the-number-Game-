import random

secret_number = random.randint(1, 100)
guess = None

while guess != secret_number:
    guess = int(input("Guess a number: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")

print("You won!")