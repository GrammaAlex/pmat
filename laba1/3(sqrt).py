#!/usr/bin/env python3

import math
import sys

try:
    # Чтение значения C из stdin
    C = float(sys.stdin.readline().strip())

    # Вычисление квадратного корня
    if C < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")

    sqrt_result = math.sqrt(C)

    # Запись результата в output.txt
    with open("output.txt", "w") as output_file:
        output_file.write(f"{sqrt_result}\n")

    # Логирование значения C
    with open("logs.txt", "a") as log_file:
        log_file.write(f"C = {C}\n")

except Exception as e:
    # Запись ошибки в файл errors.txt
    with open("errors.txt", "a") as error_file:
        error_file.write(f"Error: {str(e)}\n")
    sys.exit(1)

