#!/usr/bin/python3
import sys
import math


def main():
    try:
        # Читаем входные данные
        input_data = input("Enter a number: ").strip()

        if not input_data:
            raise ValueError("Input is empty.")

        number = float(input_data)

        # Проверяем, что число не отрицательное
        if number < 0:
            raise ValueError("Cannot calculate square root of a negative number.")

        # Вычисляем квадратный корень
        result = math.sqrt(number)
        # Записываем результат в файл с добавлением, а не перезаписью
        with open('output.txt', 'a') as f:
            f.write(f"{result}\n")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
