import random

def generate_random_code(length=8, use_letters=True, use_numbers=True, use_special_chars=False):
    """
    Generate a random code with the specified length and character set.

    Args:
        length (int): Length of the random code.
        use_letters (bool): Include letters in the code.
        use_numbers (bool): Include numbers in the code.
        use_special_chars (bool): Include special characters in the code.

    Returns:
        str: A randomly generated code.
    """
    if not use_letters and not use_numbers and not use_special_chars:
        raise ValueError("At least one of use_letters, use_numbers, or use_special_chars must be True.")

    character_pool = ''
    if use_letters:
        character_pool += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_numbers:
        character_pool += '0123456789'
    if use_special_chars:
        character_pool += '!@#$%^&*()-_=+[]{}|;:,.<>?/'

    return ''.join(random.choice(character_pool) for _ in range(length))

# Example usage:
if __name__ == "__main__":
    code_length = 16  # Set the desired code length
    random_code = generate_random_code(length=code_length, use_letters=True, use_numbers=True, use_special_chars=True)
    print("Generated Random Code:", random_code)
