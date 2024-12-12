import pytest
import os
import tempfile
from database.database import Database, EmployeeTable, DepartmentTable

@pytest.fixture
def temp_employee_file():
    """ Создаем временный файл для таблицы рабочих """
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    yield temp_file.name
    os.remove(temp_file.name)

@pytest.fixture
def temp_department_file():
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    yield temp_file.name
    os.remove(temp_file.name)

#Пример, как используются фикстуры
@pytest.fixture
def database(temp_employee_file, temp_department_file):
    """ Данная фикстура задает БД и определяет таблицы. """
    db = Database()

    # Используем временные файлы для тестирования файлового ввода-вывода в EmployeeTable и DepartmentTable
    employee_table = EmployeeTable()
    employee_table.FILE_PATH = temp_employee_file
    department_table = DepartmentTable()
    department_table.FILE_PATH = temp_department_file

    db.register_table("employees", employee_table)
    db.register_table("departments", department_table)

    return db

def test_insert_employee(database):
    database.insert("employees", "1 Alice 30 70000")
    database.insert("employees", "2 Bob 28 60000")

    # Проверяем вставку, подгружая с CSV
    employee_data = database.select("employees", 1, 2)
    print(employee_data)
    assert len(employee_data) == 2
    assert employee_data[0] == {'id': '1', 'name': 'Alice', 'age': '30', 'salary': '70000'}
    assert employee_data[1] == {'id': '2', 'name': 'Bob', 'age': '28', 'salary': '60000'}

def test_unique_composite_index_employee(database):
    database.insert("employees", "1 Alice 30 70000 101")
    with pytest.raises(ValueError, match="Duplicate composite index"):
        database.insert("employees", "1 Alice 30 70000 101")

def test_unique_index_department(database):
    database.insert("departments", "101 HR")
    with pytest.raises(ValueError, match="Duplicate department_id"):
        database.insert("departments", "101 HR")
    
def test_join_employees_departments(database):
    database.insert("employees", "1 Alice 30 70000 101")
    database.insert("employees", "2 Bob 28 60000 102")
    database.insert("departments", "101 HR")
    database.insert("departments", "102 IT")

    joined_data = database.join("employees", "departments")

    expected_result = [
        {"id": "1", "name": "Alice", "age": "30", "salary": "70000", "department_id": "101", "department_name": "HR"},
        {"id": "2", "name": "Bob", "age": "28", "salary": "60000", "department_id": "102", "department_name": "IT"}
    ]

    assert joined_data == expected_result


def test_csv_files_absence(temp_employee_file, temp_department_file):
    assert not os.path.exists(temp_employee_file)
    assert not os.path.exists(temp_department_file)