import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += specials

    pwd = ""
    has_number = False
    has_special = False

    while len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in specials:
            has_special = True

    while (numbers and not has_number) or (special_characters and not has_special):
        missing_number = numbers and not has_number
        missing_special = special_characters and not has_special

        if missing_number:
            pwd += random.choice(digits)
            has_number = True
        if missing_special:
            pwd += random.choice(specials)
            has_special = True

    return pwd


min_length = int(input("Enter the minimum length of the password: "))
has_number = input("Should the password contain numbers? (y/n): ").lower() == "y"
has_special = input("Should the password contain special characters? (y/n): ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)
