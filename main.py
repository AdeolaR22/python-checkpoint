 
import random

print("Welcome to the Guess the Number game!")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Ask the player to enter a guess
guess = int(input("I'm thinking of a number between 1 and 100. Can you guess it? "))

# Continue playing until the correct number is guessed
while guess != secret_number:

    if guess > secret_number:
        print("Your guess is too high. Guess again.")

    else:
        print("Your guess is too low. Guess again.")

    guess = int(input("Enter your guess: "))

print("Congratulations! You guessed the number correctly!")

