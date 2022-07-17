class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calculate_mean_grade(self):
        grades = []
        for course in self.grades:
            grades += self.grades[course]
        mean_grade = sum(grades) / len(grades) if grades else 0
        return round(mean_grade, 2)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.calculate_mean_grade() < other.calculate_mean_grade()
        else:
            return 'Ошибка'

    def __str__(self):
        print_data = f'Имя: {self.name}\n' \
                     f'Фамилия: {self.surname}\n' \
                     f'Средняя оценка за домашние задания: {self.calculate_mean_grade()}\n' \
                     f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                     f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return print_data


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calculate_mean_grade(self):
        grades = []
        for course in self.grades:
            grades += self.grades[course]
        mean_grade = sum(grades) / len(grades) if grades else 0
        return round(mean_grade, 2)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_mean_grade() < other.calculate_mean_grade()
        else:
            return 'Ошибка'

    def __str__(self):
        print_data = f'Имя: {self.name}\n' \
                     f'Фамилия: {self.surname}\n' \
                     f'Средняя оценка за лекции: {self.calculate_mean_grade()}\n'
        return print_data


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
        print_data = f'Имя: {self.name}\n' \
                     f'Фамилия: {self.surname}\n'
        return print_data


def mean_students_grade_per_course(students_list, course):
    grades = []
    for student in students_list:
        if course in student.grades:
            grades += student.grades.get(course)
    mean_grade = sum(grades) / len(grades) if grades else 0
    return round(mean_grade, 2)


def mean_lecturers_grade_per_course(lecturers_list, course):
    grades = []
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            grades += lecturer.grades.get(course)
    mean_grade = sum(grades) / len(grades) if grades else 0
    return round(mean_grade, 2)


student_1 = Student('Ivan', 'Ivanov', 'male')
student_2 = Student('Petr', 'Petrov', 'male')

lecturer_1 = Lecturer('Nicolay', 'Lobachevskiy')
lecturer_2 = Lecturer('Stanislav', 'Osipov')

reviewer_1 = Reviewer('Aleksandr', 'Vasiliev')
reviewer_2 = Reviewer('Oleg', 'Mihlin')

student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Python', 'Java']
lecturer_1.courses_attached.append('Python')
lecturer_2.courses_attached += ['Python', 'Java']

student_1.rate_lecturer(lecturer_1, 'Python', 5)
student_1.rate_lecturer(lecturer_1, 'Python', 4)
student_2.rate_lecturer(lecturer_2, 'Python', 4)

reviewer_1.courses_attached += ['Python', 'Java']
reviewer_2.courses_attached += ['Python', 'Java']

reviewer_1.rate_hw(student_1, 'Python', 3)
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_2, 'Java', 5)
reviewer_2.rate_hw(student_2, 'Python', 8)

print(lecturer_1)
print(lecturer_2)

print(reviewer_1)
print(reviewer_2)

print(student_1)
print(student_2)

print('Сравнение лекторов и студентов по средней оценке: ')
print(lecturer_1 > lecturer_2)
print(student_1 < student_2)
print()

best_student = max(student_1, student_2)
print('Лучший студент: ', best_student, sep='\n')

best_lecturer = max(lecturer_1, lecturer_2)
print('Лучший лектор: ', best_lecturer, sep='\n')

print(f'Средняя оценка за домашние задания по всем студентам в рамках курса {"Java"}: ',
      mean_students_grade_per_course([student_1, student_2], 'Java'))
print(f'Средняя оценка за домашние задания по всем студентам в рамках курса {"Python"}: ',
      mean_students_grade_per_course([student_1, student_2], 'Python'))
print()

print(f'Средняя оценка по всем лекторам в рамках курса {"Java"}: ',
      mean_lecturers_grade_per_course([lecturer_1, lecturer_2], 'Java'))
print(f'Средняя оценка по всем лекторам в рамках курса {"Python"}: ',
      mean_lecturers_grade_per_course([lecturer_1, lecturer_2], 'Python'))
print()
