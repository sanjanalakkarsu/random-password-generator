import random
import string
def generate_character(lowercase=True,uppercase=True,symbols=True,numbers=True):

    character_set = ' '
    if lowercase:
        character_set+= string.ascii_lowercase
    if uppercase:
        character_set+= string.ascii_uppercase
    if symbols:
        character_set+= string.punctuation
    if numbers:
        character_set+= string.digits
    return character_set

def generate_password(length,character_set):
    password = ' '
    for i in range(length):
        password+= random.choice(character_set)
    return password

def main():
    length = int(input("Enter the length of the password:"))
    lowercase = input("Should the password contain lowercase?").lower()=='yes'
    uppercase = input("Should the password contain uppercase?").lower()=='yes'
    symbols = input("Should the password contain symbols?").lower()=='yes'
    numbers = input("Should the password contain numbers?").lower()=='yes'

    character_set = generate_character(lowercase,uppercase,symbols,numbers)
    password = generate_password(length,character_set)
    
    if password:
        print(f"Random password generated from the given input is: {password}")
    else:
        print("Could not generate the password")

if __name__ == "__main__":
    main()