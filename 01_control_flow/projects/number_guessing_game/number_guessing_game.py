import random

# Number guessing game
print("Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    try:
        guess = int(input(f"Guess a number between 1 and 100 (Attempt {attempts + 1}/{max_attempts}): "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break
    except ValueError:
        print("Please enter a valid number!")

if attempts == max_attempts:
    print(f"Game over! The number was {secret_number}")
