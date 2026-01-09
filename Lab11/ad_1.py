import json


class Student:
    def __init__(
        self, name: str, email: str, grade: str, is_adult: bool, grades: list[int]
    ):
        self.name = name
        self.email = email
        self.grade = grade
        self.is_adult = is_adult
        self.grades = grades
        self.grades_avg = 0.0
        self.calculate_avg()

    def calculate_avg(self):
        if self.grades:
            self.grades_avg = sum(self.grades) / float(len(self.grades))

    def __repr__(self):
        return f"name: {self.name} | email: {self.email} | grade: {self.grade} | is_adult: {self.is_adult} | grades: {self.grades} | avg_grade: {self.grades_avg} |"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
            "grade": self.grade,
            "is_adult": self.is_adult,
            "grades": self.grades,
            "grades_avg": self.grades_avg,
        }


FILEPATH = "students.json"


def load_students(filepath: str) -> list[type[Student]]:
    with open(filepath) as file:
        students = []
        data = json.load(file)
        for student in data["students"]:
            students.append(
                Student(
                    student["name"],
                    student["email"],
                    student["grade"],
                    student["is_adult"],
                    student["grades"],
                )
            )
        return students


def save_students(filepath: str, students: list[type[Student]]) -> None:
    data = {"students": [student.to_dict() for student in students]}

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


s = load_students(FILEPATH)
print(s)
save_students("students_updated.json", s)

ns = load_students("students_updated.json")
print(ns)
