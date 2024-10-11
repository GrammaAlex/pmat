#!/usr/bin/python3
import os
import string

def is_valid_name(name):
    return name[0].isupper() and name[1:].islower() and all(c in string.ascii_letters for c in name)

def greet_names_from_file(filename):
    with open(filename, 'r') as file:
        names = file.readlines()

    with open('error.txt', 'w') as error_file:
        for name in names:
            name = name.strip()
            if is_valid_name(name):
                print(f"Hello, {name}!")
            else:
                error_file.write(f"Invalid name: {name}n")

def greet_user():
    try:
        while True:
            name = input("Please enter your name: ").strip()
            if is_valid_name(name):
                print(f"Hello, {name}!")
            else:
                print(f"Invalid name: {name}. It must start with a lowercase letter and contain only lowercase letters.")
    except KeyboardInterrupt:
        print("nGoodbye!")

def main():
    mode = input("Choose mode (1 - file, 2 - user): ").strip()
    if mode == '1':
        filename = input("Enter the filename: ").strip()
        if os.path.isfile(filename):
            greet_names_from_file(filename)
        else:
            print(f"File '{filename}' does not exist.")
    elif mode == '2':
        greet_user()
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
