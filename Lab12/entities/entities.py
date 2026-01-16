from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Float

__all__ = ["Employee", "Product", "EmployeeORM", "ProductORM"]


class Employee:
    def __init__(self, id: int, name: str, position: str, department: str):
        self.employee_id = id
        self.name = name
        self.position = position
        self.department = department

    def __str__(self):
        return f"Employee({self.employee_id}, {self.name}, {self.position}, {self.department})"


class Product:
    def __init__(self, id: int, name: str, price: float, category: str):
        self.product_id = id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product({self.product_id}, {self.name}, {self.price}, {self.category})"


class Base(DeclarativeBase):
    pass


class EmployeeORM(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    position: Mapped[str] = mapped_column(String)
    department: Mapped[str] = mapped_column(String)


class ProductORM(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    price: Mapped[Float] = mapped_column(Float)
    category: Mapped[str] = mapped_column(String)
