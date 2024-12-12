#!/usr/bin/env python3

import random
import sys

# Генерация случайного числа A
A = random.randint(-10, 10)

# Логирование значения A
with open("logs.txt", "a") as log_file:
    log_file.write(f"A = {A}\n")

# Вывод A в стандартный вывод
print(A)
