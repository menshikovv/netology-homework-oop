class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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


class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    pass


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Another', 'Person')
cool_reviewer.courses_attached += ['Python']

cool_lecturer.rate_hw(best_student, 'Python', 10)
cool_lecturer.rate_hw(best_student, 'Python', 10)
cool_lecturer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
