import mysql.connector as mysql
from entities import Employee, Product
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection


def create_connection(
    host: str, user: str, password: str, database: str
) -> PooledMySQLConnection | MySQLConnectionAbstract | None:
    try:
        connection = mysql.connect(
            host=host, user=user, passwd=password, database=database
        )
        print("Connected to MySQL")
    except mysql.Error as e:
        connection = None
        print(f"Connection error: {e}")
    return connection


def run_migrations(connection: PooledMySQLConnection | MySQLConnectionAbstract) -> None:
    if connection and connection.is_connected():
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS employees (id INT PRIMARY KEY, name VARCHAR(255), position VARCHAR(255), department VARCHAR(255))"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS products (id INT PRIMARY KEY, name VARCHAR(255), price FLOAT, category VARCHAR(255))"
        )
        connection.commit()
        cursor.close()
        print("Migrations completed.")

    else:
        print("Connection not established.")


def add_employee(
    connection: PooledMySQLConnection | MySQLConnectionAbstract,
    employee: Employee,
) -> None:
    if connection and connection.is_connected():
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO employees (id, name, position, department) VALUES (%s, %s, %s, %s)",
                (
                    employee.employee_id,
                    employee.name,
                    employee.position,
                    employee.department,
                ),
            )
            connection.commit()
            print(f"Employee added: {employee}")

        except mysql.Error as e:
            print(f"Error adding Employee: {e}")

        cursor.close()

    else:
        print("Connection not established.")


def add_product(
    connection: PooledMySQLConnection | MySQLConnectionAbstract,
    product: Product,
) -> None:
    if connection and connection.is_connected():
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO products (id, name, price, category) VALUES (%s, %s, %s, %s)",
                (
                    product.product_id,
                    product.name,
                    product.price,
                    product.category,
                ),
            )
            connection.commit()
            print(f"Product added: {product}")

        except mysql.Error as e:
            print(f"Error adding product: {e}")

        cursor.close()

    else:
        print("Connection not established.")


conn = create_connection("localhost", "root", "", "company")
if not conn:
    exit(-1)

run_migrations(conn)

e1 = Employee(1, "John Doe", "Manager", "Sales")
e2 = Employee(2, "Jane Smith", "Salesperson", "Sales")
p1 = Product(1, "Laptop", 999.99, "Electronics")
p2 = Product(2, "Smartphone", 499.99, "Electronics")

add_employee(conn, e1)
add_employee(conn, e2)
add_product(conn, p1)
add_product(conn, p2)
