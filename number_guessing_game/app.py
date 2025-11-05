import random


def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    for i in range(11):
        try:
            # Get player's guess
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1

            # Validate the guess
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            # Check the guess
            if abs(guess - secret_number) <= 5:
                print("You are close! Keep guessing.")
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(
                    "Congratulations! You guessed the secret number in",
                    attempts,
                    "attempts.",
                )
                break
        except ValueError:
            print("Please enter a valid number.")
            continue


if __name__ == "__main__":
    number_guessing_game()
