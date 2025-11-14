import csv


class Employee:
    def __init__(
        self, name: str, surname: str, gender: str, address: str, salary: float
    ) -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.address = address
        self.salary = salary

    def __repr__(self):
        return f"Employee({self.name}, {self.surname}, {self.salary})"

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value not in ("K", "M"):
            raise ValueError("Płeć musi być 'K' lub 'M'.")
        self._gender = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Pensja musi być liczbą.")

        if value < 0:
            raise ValueError("Pensja nie może być mniejsza niż 0.")
        self._salary = value

    @classmethod
    def from_csv(cls, filename: str):
        employees = []
        try:
            with open(filename, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    employees.append(
                        cls(
                            row["name"],
                            row["surname"],
                            row["gender"],
                            row["address"],
                            float(row["salary"]),
                        )
                    )
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except ValueError:
            print(f"Invalid data in file {filename}.")
        except Exception as e:
            print(f"An error occurred while reading file {filename}: {e}")
        return employees

    @staticmethod
    def average_salary(employees):
        if not employees:
            return 0
        return sum(emp.salary for emp in employees) / len(employees)


employees = Employee.from_csv("employees.csv")
print("Wczytani pracownicy:")
for e in employees:
    print(e)

avg = Employee.average_salary(employees)
print(f"\nŚrednia pensja: {avg:.2f} zł")

try:
    salary_negative_employee = Employee("Jan", "Kowalski", "M", "Warszawa", -1000)
except ValueError as e:
    print(f"Invalid data: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    non_binary_employee = Employee("Anna", "Nowak", "X", "Kraków", 4500)
except ValueError as e:
    print(f"Invalid data: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
