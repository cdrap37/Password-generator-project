import random
import string

def generate_password(length, uppercase=True, lowercase=True, digits=True, special_chars=True):
    """
    Generates a random password with the specified length and character types.

    Parameters:
        length (int): The length of the password.
        uppercase (bool): Whether to include uppercase letters. Default is True.
        lowercase (bool): Whether to include lowercase letters. Default is True.
        digits (bool): Whether to include digits. Default is True.
        special_chars (bool): Whether to include special characters. Default is True.

    Returns:
        str: The generated password.
    """
    # Create a pool of characters based on the selected character types
    char_pool = ""
    if uppercase:
        char_pool += string.ascii_uppercase
    if lowercase:
        char_pool += string.ascii_lowercase
    if digits:
        char_pool += string.digits
    if special_chars:
        char_pool += string.punctuation

    # Generate the password by randomly selecting characters from the pool
    password = "".join(random.choice(char_pool) for _ in range(length))
    return password


if __name__ == "__main__":
    length = int(input("Enter the desired length of the password: "))
    uppercase = bool(input("Include uppercase letters? (y/n): ").lower() == "y")
    lowercase = bool(input("Include lowercase letters? (y/n): ").lower() == "y")
    digits = bool(input("Include digits? (y/n): ").lower() == "y")
    special_chars = bool(input("Include special characters? (y/n): ").lower() == "y")

    password = generate_password(length, uppercase, lowercase, digits, special_chars)
    print("Generated Password:", password)
