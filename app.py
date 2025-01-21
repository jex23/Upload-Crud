import random
import string

def generate_random_code(length=8, use_letters=True, use_numbers=True):
    """
    Generate a random code with the specified length and character set.

    Args:
        length (int): Length of the random code.
        use_letters (bool): Include letters in the code.
        use_numbers (bool): Include numbers in the code.

    Returns:
        str: A randomly generated code.
    """
    if not use_letters and not use_numbers:
        raise ValueError("At least one of use_letters or use_numbers must be True.")

    character_pool = []
    if use_letters:
        character_pool.extend(string.ascii_letters)  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_numbers:
        character_pool.extend(string.digits)  # '0123456789'

    return ''.join(random.choices(character_pool, k=length))

# Example usage:
if __name__ == "__main__":
    code_length = 10  # Set the desired code length
    random_code = generate_random_code(length=code_length, use_letters=True, use_numbers=True)
    print("Generated Random Code:", random_code)
