from abc import ABC, abstractmethod
import csv
import os


class SingletonMeta(type):
    """ Синглтон метакласс для Database. """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    """ Класс-синглтон базы данных с таблицами, хранящимися в файлах. """

    def __init__(self):
        self.tables = {}

    def register_table(self, table_name, table):
        self.tables[table_name] = table

    def insert(self, table_name, data):
        table = self.tables.get(table_name)
        if table:
            table.insert(data)
        else:
            raise ValueError(f"Table {table_name} does not exist.")

    def select(self, table_name, *args):
        table = self.tables.get(table_name)
        return table.select(*args) if table else None

    def join(self, table1_name, table2_name, join_attr="department_id"):
        table1 = self.tables.get(table1_name)
        table2 = self.tables.get(table2_name)

        if not table1 or not table2:
            raise ValueError("One or both tables do not exist.")

        result = []
        for row1 in table1.data:
            for row2 in table2.data:
                if row1[join_attr] == row2[join_attr]:
                    merged_row = {**row1, **row2}
                    result.append(merged_row)
        return result


class Table(ABC):
    """ Абстрактный базовый класс для таблиц с вводом/выводом файлов CSV. """

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def select(self, *args):
        pass


class EmployeeTable(Table):
    """ Таблица сотрудников с методами ввода-вывода из файла CSV. """
    ATTRS = ('id', 'name', 'age', 'salary', 'department_id')
    FILE_PATH = 'employee_table.csv'

    def __init__(self):
        self.data = []
        self.load()  # Подгружаем из CSV-файла сразу при инициализации

    def insert(self, data):
        entry = dict(zip(self.ATTRS, data.split()))

        if any(
            e['id'] == entry['id'] and e['department_id'] == entry['department_id']
            for e in self.data
        ):
            raise ValueError("Duplicate composite index (id, department_id) detected.")

        self.data.append(entry)
        self.save()

    def select(self, start_id, end_id):
        return [entry for entry in self.data if start_id <= int(entry['id']) <= end_id]

    def save(self):
        with open(self.FILE_PATH, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.ATTRS)
            writer.writeheader()
            writer.writerows(self.data)

    def load(self):
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, 'r') as f:
                reader = csv.DictReader(f)
                self.data = [row for row in reader]
        else:
            self.data = []


class DepartmentTable(Table):
    """ Таблица подразделений с вводом-выводом в/из CSV файла. """
    ATTRS = ('department_id', 'department_name')
    FILE_PATH = 'department_table.csv'

    def __init__(self):
        self.data = []
        self.load()

    def insert(self, data):
        entry = dict(zip(self.ATTRS, data.split()))

        if any(e['department_id'] == entry['department_id'] for e in self.data):
            raise ValueError("Duplicate department_id detected.")

        self.data.append(entry)
        self.save()

    def select(self, department_name):
        return [entry for entry in self.data if entry['department_name'] == department_name]

    def save(self):
        with open(self.FILE_PATH, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.ATTRS)
            writer.writeheader()
            writer.writerows(self.data)

    def load(self):
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, 'r') as f:
                reader = csv.DictReader(f)
                self.data = [row for row in reader]
        else:
            self.data = []
