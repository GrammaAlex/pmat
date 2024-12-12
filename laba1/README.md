## Установка
1. Сделайте Python-скрипты исполняемыми:
   chmod +x generate.py calc_ratio.py calc_sqrt.py

2. Запустите конвейер:
./1(random).py | ./2(division).py 2> errors.txt | ./3(sqrt).py 2>> errors.txt

3. Ошибки, которые записаны в errors.txt:
Деление на ноль: ZeroDivisionError: Division by zero encountered.
Отрицательный квадратный корень: ValueError: Cannot calculate the square root of a negative number.

4. В файле logs.txt:
A — случайное число, сгенерированное 1(random).py.
B — случайное число, сгенерированное в 2(division).py.
C — результат деления 𝐴/𝐵, переданный в 3(sqrt).py.
Каждое новое выполнение программы добавляет строки в конец файла logs.txt. Таким образом, файл будет содержать историю всех запусков скриптов.
