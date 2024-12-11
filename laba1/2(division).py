#!/usr/bin/python3
import random
import sys

def main():
    try:
        # Чтение ввода
        input_data = input("Enter a number: ").strip()
        if not input_data:
            raise EOFError("No input provided.")

        # Преобразование ввода в целое число
        A = int(input_data)
        B = random.randint(-10, 10)

        # Проверка деления на ноль и выполнение вычисления
        result = A / B
        print(result)

    except ValueError:
        print("Error: Input must be an integer.", file=sys.stderr)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.", file=sys.stderr)
    except EOFError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
    finally:
        print("Execution finished.", file=sys.stderr)

if __name__ == "__main__":
    main()
