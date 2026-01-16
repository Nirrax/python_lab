import json
from gc import callbacks

import sqlalchemy
from entities import EmployeeORM, ProductORM
from sqlalchemy.engine import URL


def create_connection(
    driver: str, username: str, password: str, host: str, port: int, database: str
) -> sqlalchemy.engine.Connection:
    url = URL.create(
        drivername=driver,
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
    )
    engine = sqlalchemy.create_engine(url)
    return engine.connect()


def get_employees(connection: sqlalchemy.engine.Connection) -> list[EmployeeORM]:
    query = sqlalchemy.select(EmployeeORM)
    result = connection.execute(query)
    return result.fetchall()


def get_products(connection: sqlalchemy.engine.Connection) -> list[ProductORM]:
    query = sqlalchemy.select(ProductORM)
    result = connection.execute(query)
    return result.fetchall()


def sort_employees_by_surname(employees: list[EmployeeORM]) -> list[EmployeeORM]:
    return sorted(employees, key=lambda e: e.name.split()[1])


def export_employees_to_json(employees, filename="employees.json") -> None:
    data = [
        {
            "id": e.id,
            "name": e.name,
            "position": e.position,
            "department": e.department,
        }
        for e in employees
    ]

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def calculate_average_price(products: list[ProductORM]) -> float:
    total_price = sum(product.price for product in products)
    return total_price / len(products)


conn = create_connection(
    driver="mysql+pymysql",
    username="root",
    password="",
    host="localhost",
    port=3306,
    database="company",
)

employees = get_employees(conn)
products = get_products(conn)

export_employees_to_json(sort_employees_by_surname(employees))
print(f"Average price of products: {calculate_average_price(products):.2f}")
