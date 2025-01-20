import random
import string

def generate_password(length=12):
    """
    Generate a random password with a mix of letters, digits, and symbols.
    
    Args:
        length (int): Length of the password (default is 12).
    
    Returns:
        str: The generated password.
    """
    if length < 4:  # Ensure the password is long enough for complexity
        raise ValueError("Password length must be at least 4 characters")

    # Define character pools
    letters = string.ascii_letters  # Uppercase and lowercase letters
    digits = string.digits          # Numbers 0-9
    symbols = string.punctuation    # Special characters

    # Ensure at least one character from each category
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest of the password length with a random selection of all character types
    all_characters = letters + digits + symbols
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

def main():
    try:
        print("Welcome to the Password Generator!")
        length = int(input("Enter the desired password length (minimum 4): "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
