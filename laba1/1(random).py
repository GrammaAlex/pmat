#!/usr/bin/python3
import random
import sys

def generate_random_number():
    try:
        return random.randint(-10, 10)
    except Exception as e:
        raise RuntimeError(f"Error generating random number: {e}")

def main():
    try:
        number = generate_random_number()
        print(f"Generated number: {number}")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
