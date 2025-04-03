import random

def generate_number():
    """Generate a random number between 1 and 100."""
    return random.randint(1, 100)

def play_game():
    number_to_guess = generate_number()
    attempts = 0

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = input("Enter your guess: ")
        attempts += 1

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
