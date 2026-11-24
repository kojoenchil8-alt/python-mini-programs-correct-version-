import random

def play_number_guess():
    """Play a console number guessing game from 1 to 20. """
    secret_number = random.randint(1,20)
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("I'm thinking  of a number between 1 and 20.")

    while True:
        guess_input = input("\nEnter your guess (or 'q' to quit): ")

        if guess_input == 'q':
            print(f"Game ended! The number was {secret_number}.")
            break

        if not guess_input.isdigit():
            print("Please enter a valid number between 1 and 20.")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess < 1 or guess > 20:
            print("Out of range! Pick a number from 1 to 20.")
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Correct! you guessed{secret_number} in  {attempts} tries.")
            break


if __name__ == "__main__":
    play_number_guess()