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
        return mean_grade

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
        return mean_grade

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


student_1 = Student('Ivan', 'Ivanov', 'male')
student_2 = Student('Petr', 'Petrov', 'male')

lector_1 = Lecturer('Nicolay', 'Lobachevskiy')
lector_2 = Lecturer('Stanislav', 'Osipov')

reviewer_1 = Reviewer('Aleksandr', 'Vasiliev')
reviewer_2 = Reviewer('Oleg', 'Mihlin')


student_1.courses_in_progress.append('Python')
student_2.courses_in_progress.append('Python')
lector_1.courses_attached.append('Python')
lector_2.courses_attached.append('Python')

student_1.rate_lecturer(lector_1, 'Python', 5)
student_1.rate_lecturer(lector_1, 'Python', 4)
student_2.rate_lecturer(lector_2, 'Python', 4)

reviewer_1.courses_attached.append('Python')
reviewer_1.rate_hw(student_1, 'Python', 3)
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_2, 'Python', 5)


print(lector_1)
print(lector_2)

print(reviewer_1)

print(student_1)
print(student_2)

print(lector_1 > lector_2)
print(student_1 < student_2)
