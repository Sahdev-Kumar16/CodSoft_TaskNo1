import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    if length < 6:
        return "Password length should be at least 6 characters."

    character_pool = string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        return "At least one character type must be selected."

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def password_generator():
    while True:
        try:
            length = int(input("Enter desired password length (minimum 6): "))
            use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
            use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
            use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

            password = generate_password(length, use_uppercase, use_numbers, use_special)
            print(f"Generated password: {password}")
        except ValueError:
            print("Please enter a valid number.")

        next_action = input("Do you want to generate another password? (yes/no): ")
        if next_action.lower() != 'yes':
            break

if __name__ == "__main__":
    password_generator()
