import random

def roll_dice(sides=6, rolls=1):
    """
    Simulate rolling a dice with a specified number of sides and rolls.

    Parameters:
        sides (int): Number of sides on the dice. Default is 6.
        rolls (int): Number of dice rolls. Default is 1.

    Returns:
        list: A list of roll outcomes.
    """
    if sides < 2:
        raise ValueError("A dice must have at least 2 sides.")
    if rolls < 1:
        raise ValueError("Number of rolls must be at least 1.")

    return [random.randint(1, sides) for _ in range(rolls)]

if __name__ == "__main__":
    try:
        sides = int(input("Enter the number of sides on the dice (minimum 2): "))
        rolls = int(input("Enter the number of rolls: "))
        outcomes = roll_dice(sides, rolls)
        print(f"You rolled: {outcomes}")
    except ValueError as e:
        print("Error:", e)
