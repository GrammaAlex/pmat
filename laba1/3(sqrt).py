#!/usr/bin/python3
import sys
import math

def main():
    try:
        number = float(sys.stdin.read().strip())

        if number < 0:
            raise ValueError("Cannot calculate square root of a negative number.")

        result = math.sqrt(number)

        with open('output.txt', 'w') as f:
            f.write(str(result))
    except ValueError as e:
        print(e, file=sys.stderr)
    except Exception as e:
        print(e, file=sys.stderr)

if __name__ == "__main__":
    main()
