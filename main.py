class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'

    def middle_grade(self):
        middle_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_middle = course_sum / len(course_grades)
            middle_sum += course_middle
        if middle_sum == 0:
            return f'Студент еще не получал оценки'
        else:
            return f'{middle_sum / len(self.grades.values()):.2f}'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n'
        res += f'Средняя оценка за домашние задания: {self.middle_grade()} \n'
        res += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
        res += f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, student):
        if not isinstance(student, Student):
            print(f'Такого студента нет')
            return
        return self.middle_grade() < student.middle_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rates = {}


class Lecturer(Mentor):
    def middle_rate(self):
        middle_sum = 0
        for course_grades in self.rates.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_middle = course_sum / len(course_grades)
            middle_sum += course_middle
        if middle_sum == 0:
            return f'Оценки еще не выставлялись'
        else:
            return f'{middle_sum / len(self.rates.values()):.2f}'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        res += f'Средняя оценка {self.middle_rate()}\n'
        return res

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print(f' Такого лектора нет')
            return
        return self.middle_rate() < lecturer.middle_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return res


def grades_students(students_list, course):
    mid_sum_grades = 0
    lectors = 0
    for stud in students_list:
        if course in stud.grades.keys():
            stud_sum_grades = 0
            for grades in stud.grades[course]:
                stud_sum_grades += grades
            mid_stud_sum_grades = stud_sum_grades / len(stud.grades[course])
            mid_sum_grades += mid_stud_sum_grades
            lectors += 1
    if mid_sum_grades == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{mid_sum_grades / lectors:.2f}'


def grades_lecturers(lecturer_list, course):
    mid_sum_rates = 0
    b = 0
    for lecturer in lecturer_list:
        if course in lecturer.rates.keys():
            lecturer_sum_rates = 0
            for rate in lecturer.rates[course]:
                lecturer_sum_rates += rate
            mid_lecturer_sum_rates = lecturer_sum_rates / len(lecturer.rates[course])
            mid_sum_rates += mid_lecturer_sum_rates
            b += 1
    if mid_sum_rates == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{mid_sum_rates / b:.2f}'


first_student = Student('Sebastian', 'Miksch', 'Male')
first_student.finished_courses = ['HTML', 'CSS']
first_student.courses_in_progress = ['PHP', 'JavaScript']

second_student = Student('Steven', 'Kuzmin', 'Male')
second_student.finished_courses = ['Git', 'PHP']
second_student.courses_in_progress = ['Python', 'JavaScript']
students_list = [first_student, second_student]

first_lecturer = Lecturer('Lena', 'Kuzmina')
first_lecturer.courses_attached = ['PHP', 'JavaScript']

second_lecturer = Lecturer('Petr', 'Penkin')
second_lecturer.courses_attached = ['Python']
lecturer_list = [first_lecturer, second_lecturer]

first_reviewer = Reviewer('Jena', 'Markina')
first_reviewer.courses_attached = ['HTML', 'Git', 'JavaScript', 'PHP']

second_reviewer = Reviewer('Alena', 'Markova')
second_reviewer.courses_attached = ['PHP', 'Python', 'CSS']

first_reviewer.rate_hw(first_student, 'PHP', 8)
first_reviewer.rate_hw(first_student, 'PHP', 7)
first_reviewer.rate_hw(first_student, 'PHP', 10)
first_reviewer.rate_hw(first_student, 'JavaScript', 5)
first_reviewer.rate_hw(first_student, 'JavaScript', 8)
first_reviewer.rate_hw(first_student, 'JavaScript', 9)
first_reviewer.rate_hw(first_student, 'HTML', 8)
first_reviewer.rate_hw(first_student, 'HTML', 6)
first_reviewer.rate_hw(first_student, 'CSS', 10)
first_reviewer.rate_hw(first_student, 'CSS', 8)
first_reviewer.rate_hw(first_student, 'CSS', 4)

second_reviewer.rate_hw(second_student, 'Git', 4)
second_reviewer.rate_hw(second_student, 'Git', 2)
second_reviewer.rate_hw(second_student, 'Git', 3)
second_reviewer.rate_hw(second_student, 'PHP', 8)
second_reviewer.rate_hw(second_student, 'PHP', 1)
second_reviewer.rate_hw(second_student, 'PHP', 7)
second_reviewer.rate_hw(second_student, 'Python', 8)
second_reviewer.rate_hw(second_student, 'Python', 10)
second_reviewer.rate_hw(second_student, 'Python', 5)
second_reviewer.rate_hw(second_student, 'JavaScript', 7)
second_reviewer.rate_hw(second_student, 'JavaScript', 4)
second_reviewer.rate_hw(second_student, 'JavaScript', 10)

first_student.rate_lecturer(first_lecturer, 'PHP', 10)
first_student.rate_lecturer(first_lecturer, 'PHP', 5)
first_student.rate_lecturer(first_lecturer, 'PHP', 8)
first_student.rate_lecturer(first_lecturer, 'JavaScript', 6)
first_student.rate_lecturer(first_lecturer, 'JavaScript', 7)
first_student.rate_lecturer(first_lecturer, 'JavaScript', 8)

second_student.rate_lecturer(first_lecturer, 'JavaScript', 10)
second_student.rate_lecturer(first_lecturer, 'JavaScript', 8)
second_student.rate_lecturer(first_lecturer, 'JavaScript', 9)
second_student.rate_lecturer(second_lecturer, 'Python', 10)
second_student.rate_lecturer(second_lecturer, 'Python', 2)
second_student.rate_lecturer(second_lecturer, 'Python', 8)

print(first_student)
print(second_student)

if first_student > second_student:
    print(f'{first_student.name} учится лучше {second_student.name}')
else:
    print(f'{second_student.name} учится лучше {first_student.name}')

print(first_reviewer)
print(second_reviewer)

print(first_lecturer)
print(second_lecturer)

if first_lecturer > second_lecturer:
    print(f'{first_lecturer.name} преподает лучше {second_lecturer.name}')
else:
    print(f'{second_lecturer.name} преподает лучше {first_lecturer.name}')

print(f'Средняя оценка студентов по курсу "PHP": {grades_students(students_list, "PHP")}')
print(f'Средняя оценка студентов по курсу "JavaScript": {grades_students(students_list, "JavaScript")}')
print(f'Средняя оценка студентов по курсу "Python": {grades_students(students_list, "Python")}')

print(f'Средняя оценка лекторов по курсу "PHP": {grades_lecturers(lecturer_list, "PHP")}')
print(f'Средняя оценка лекторов по курсу "JavaScript": {grades_lecturers(lecturer_list, "JavaScript")}')
print(f'Средняя оценка лекторов по курсу "Python": {grades_lecturers(lecturer_list, "Python")}')