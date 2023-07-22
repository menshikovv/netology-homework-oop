class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            if lecturer in self.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return (
            self.name == other.name
            and self.surname == other.surname
            and self.gender == other.gender
            and self.finished_courses == other.finished_courses
            and self.courses_in_progress == other.courses_in_progress
            and self.grades == other.grades
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        avg_grade = self.calculate_avg_grade()
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses)
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
            f"Курсы в процессе изучения: {courses_in_progress_str}\n"
            f"Завершенные курсы: {finished_courses_str}"
        )

    def calculate_avg_grade(self):
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        if all_grades:
            return sum(all_grades) / len(all_grades)
        else:
            return 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return "ошибка"

    def __eq__(self, other):
        if not isinstance(other, Mentor):
            return False
        return self.name == other.name and self.surname == other.surname

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __str__(self):
        avg_grade = self.calculate_avg_grade()
        return f"{super().__str__()}\nСредняя оценка за лекции: {avg_grade:.1f}"

    def calculate_avg_grade(self):
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        if all_grades:
            return sum(all_grades) / len(all_grades)
        else:
            return 0

    def __lt__(self, other):
        return self.calculate_avg_grade() < other.calculate_avg_grade()

    def __le__(self, other):
        return self.calculate_avg_grade() <= other.calculate_avg_grade()

    def __gt__(self, other):
        return self.calculate_avg_grade() > other.calculate_avg_grade()