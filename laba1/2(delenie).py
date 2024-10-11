#!/usr/bin/python3
import random
import sys

def main():
    try:
        A = int(sys.stdin.read().strip())
        B = random.randint(-10, 10)

        if B == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")

        result = A / B
        print(result)
    except ValueError as e:
        print("Invalid input:", e, file=sys.stderr)
    except ZeroDivisionError as e:
        print(e, file=sys.stderr)
    except Exception as e:
        print(e, file=sys.stderr)

if __name__ == "__main__":
    main()
