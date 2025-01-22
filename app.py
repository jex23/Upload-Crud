import random

def guess_the_number():
    """
    A simple number-guessing game where the user tries to guess
    a randomly generated number within a range.
    """
    print("Welcome to the Number Guessing Game!")

    try:
        lower_bound = int(input("Enter the lower bound of the range: "))
        upper_bound = int(input("Enter the upper bound of the range: "))

        if lower_bound >= upper_bound:
            raise ValueError("Lower bound must be less than the upper bound.")

        target = random.randint(lower_bound, upper_bound)
        attempts = 0

        print(f"I have picked a number between {lower_bound} and {upper_bound}. Can you guess it?")

        while True:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < target:
                print("Too low! Try again.")
            elif guess > target:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    guess_the_number()
