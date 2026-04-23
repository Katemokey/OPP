class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] =[grade]
        else:
            return "Ошибка"

    def __str__(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        average_grade = sum(all_grades)/len(all_grades) if all_grades else 0
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False

        self_grades = [g for lst in self.grades.values() for g in lst]
        other_grades = [g for lst in other.grades.values() for g in lst]

        average_self = sum(self_grades) / len(self_grades) if self_grades else 0
        average_other = sum(other_grades) / len(other_grades) if other_grades else 0

        return average_self == average_other

    def __gt__(self, other):
        if not isinstance(other, Student):
            return False

        self_grades = [g for lst in self.grades.values() for g in lst]
        other_grades = [g for lst in other.grades.values() for g in lst]

        average_self = sum(self_grades) / len(self_grades) if self_grades else 0
        average_other = sum(other_grades) / len(other_grades) if other_grades else 0

        return average_self > average_other

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        average_grade = sum(all_grades)/len(all_grades) if all_grades else 0
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}'

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return False

        self_grades = [g for lst in self.grades.values() for g in lst]
        other_grades = [g for lst in other.grades.values() for g in lst]

        average_self = sum(self_grades) / len(self_grades) if self_grades else 0
        average_other = sum(other_grades) / len(other_grades) if other_grades else 0

        return average_self == average_other

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return False

        self_grades = [g for lst in self.grades.values() for g in lst]
        other_grades = [g for lst in other.grades.values() for g in lst]

        average_self = sum(self_grades) / len(self_grades) if self_grades else 0
        average_other = sum(other_grades) / len(other_grades) if other_grades else 0

        return average_self > average_other

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

print(best_student.grades)

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка

print(lecturer.grades)  # {'Python': [7]}

some_reviewer = Reviewer('Kate', 'Malinina')
print(some_reviewer)
some_lecturer = Lecturer('Piter', 'Popov')
print(some_lecturer)
some_student = Student('Ilya','Ivanov','F')
print(some_student)

lec1 = Lecturer('Иван', 'Иванов')
lec1.grades = {'Python': [8, 9, 10]}

lec2 = Lecturer('Петр', 'Петров')
lec2.grades = {'Python': [5, 6, 7]}

print(lec1 > lec2)   # True
print(lec1 == lec2)  # False
print(lec1 == 'строка')  # False

reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Анна', 'Сидорова')
reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2.courses_attached += ['Python', 'Java']

lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Мария', 'Смирнова')
lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2.courses_attached += ['Python', 'Java']

student_1 = Student('Алексей', 'Кузнецов', 'м')
student_2 = Student('Ольга', 'Новикова', 'ж')
student_1.courses_in_progress += ['Python', 'Git']
student_2.courses_in_progress += ['Python', 'Java']
student_1.finished_courses += ['Введение в программирование']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Java', 7)

student_1.rate_lecture(lecturer_1, 'Python', 9)
student_1.rate_lecture(lecturer_1, 'Git', 8)
student_2.rate_lecture(lecturer_2, 'Python', 10)
student_2.rate_lecture(lecturer_2, 'Java', 7)

print(student_1)
print(reviewer_1)
print(lecturer_1)

print(f"student_1 > student_2: {student_1 > student_2}")
print(f"lecturer_1 == lecturer_2: {lecturer_1 == lecturer_2}")
print(f"student_1 == lecturer_1: {student_1 == lecturer_1}")

def average_students_grade(students_list, course):
    total_grade = 0
    count = 0
    for student in students_list:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])
    return total_grade / count if count > 0 else 0

def average_lecturers_grade(lecturers_list, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total_grade / count if count > 0 else 0

print(f"Средняя оценка студентов за курс Python: {average_students_grade([student_1, student_2], 'Python')}")
print(f"Средняя оценка лекторов за курс Python: {average_lecturers_grade([lecturer_1, lecturer_2], 'Python')}")
print(f"Средняя оценка студентов за курс Git: {average_students_grade([student_1, student_2], 'Git')}")