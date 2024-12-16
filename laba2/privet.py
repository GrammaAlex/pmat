#!/usr/bin/python3
import os
import string
import sys

def is_valid_name(name):
    """Проверяет, является ли имя валидным (начинается с маленькой буквы и содержит только буквы)."""
    return name[0].islower() and all(c in string.ascii_letters for c in name)

def greet_names_from_file(filename):
    """Приветствует имена из файла или записывает ошибки в error.txt."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            names = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    except UnicodeDecodeError:
        print(f"Error: Unable to read the file '{filename}'. Make sure it is encoded in UTF-8.")
        return

    with open('error.txt', 'w', encoding='utf-8') as error_file:
        for name in names:
            name = name.strip()
            if is_valid_name(name):
                print(f"Hello, {name}!")
            else:
                error_file.write(f"Invalid name: {name}\n")

def greet_user():
    """Позволяет пользователю вводить имена с приветствием и обработкой ошибок."""
    try:
        while True:
            name = input("Please enter your name: ").strip()
            if is_valid_name(name):
                print(f"Hello, {name}!")
            else:
                print("Invalid name. It must start with a lowercase letter and contain only letters.")
    except KeyboardInterrupt:
        print("\nGoodbye!")

def main():
    """Главная функция: определяет режим работы."""
    if len(sys.argv) > 1:
        # Если передан аргумент, считаем его именем файла
        filename = sys.argv[1]
        if os.path.isfile(filename):
            greet_names_from_file(filename)
        else:
            print(f"File '{filename}' does not exist.")
    else:
        # Если аргумент не передан, запускаем интерактивный режим
        greet_user()

if __name__ == "__main__":
    main()
