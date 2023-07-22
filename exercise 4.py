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
            return "ошибка"

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

    def __ge__(self, other):
        return self.calculate_avg_grade() >= other.calculate_avg_grade()


class Reviewer(Mentor):
    pass


student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Введение в программирование']
student1.grades = {'Python': [10, 9, 8], 'Введение в программирование': [7, 8, 9]}

student2 = Student('John', 'Doe', 'male')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['ООП']
student2.grades = {'Python': [9, 8, 10], 'ООП': [8, 9, 9]}

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']
lecturer1.grades = {'Python': [9, 8, 9]}

lecturer2 = Lecturer('Jane', 'Smith')
lecturer2.courses_attached += ['ООП']
lecturer2.grades = {'Основы ООП': [7, 8, 9]}

reviewer1 = Reviewer('Another', 'Person')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Mister', 'Review')
reviewer2.courses_attached += ['ООП']

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

print(lecturer1 > lecturer2 )
print(student1 < student2)

def calculate_avg_hw_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)
    else:
        return 0

def calculate_avg_lecture_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)
    else:
        return 0

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

course_name = 'Python'
avg_hw_grade = calculate_avg_hw_grade(students_list, course_name)
print(f"Средняя оценка за домашние задания по курсу '{course_name}': {avg_hw_grade:.1f}")

avg_lecture_grade = calculate_avg_lecture_grade(lecturers_list, course_name)
print(f"Средняя оценка за лекции по курсу '{course_name}': {avg_lecture_grade:.1f}")
