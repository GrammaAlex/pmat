#!/usr/bin/env python3

import random
import sys

try:
    # Чтение значения A из stdin
    A = int(sys.stdin.readline().strip())

    # Генерация случайного числа B
    B = random.randint(-10, 10)

    # Логирование значения B
    with open("logs.txt", "a") as log_file:
        log_file.write(f"B = {B}\n")

    # Проверка деления на ноль
    if B == 0:
        raise ZeroDivisionError("Division by zero encountered.")

    # Вычисление отношения
    result = A / B

    # Вывод результата
    print(result)

except Exception as e:
    # Запись ошибки в файл errors.txt
    with open("errors.txt", "a") as error_file:
        error_file.write(f"Error: {str(e)}\n")
    sys.exit(1)

