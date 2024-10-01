class Reviewer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Имя: {self.first_name}\nФамилия: {self.last_name}'


class Lecturer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    @property
    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def __str__(self):
        return f'Имя: {self.first_name}\nФамилия: {self.last_name}\nСредняя оценка за лекции: {self.average_grade:.1f}'

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    def __le__(self, other):
        return self.average_grade <= other.average_grade

    def __eq__(self, other):
        return self.average_grade == other.average_grade

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __ge__(self, other):
        return self.average_grade >= other.average_grade


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []
        self.courses_in_progress = []
        self.finished_courses = []

    def add_grade(self, grade, course):
        self.grades.append((grade, course))

    @property
    def average_grade(self):
        if self.grades:
            return sum(grade for grade, course in self.grades) / len(self.grades)
        return 0

    def __str__(self):
        courses_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        return (f'Имя: {self.first_name}\n'
                f'Фамилия: {self.last_name}\n'
                f'Средняя оценка за домашние задания: {self.average_grade:.1f}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    def __le__(self, other):
        return self.average_grade <= other.average_grade

    def __eq__(self, other):
        return self.average_grade == other.average_grade

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __ge__(self, other):
        return self.average_grade >= other.average_grade


# Создание экземпляров
reviewer1 = Reviewer("Иван", "Иванов")
reviewer2 = Reviewer("Петр", "Петров")

lecturer1 = Lecturer("Анна", "Сидорова")
lecturer2 = Lecturer("Сергей", "Кузнецов")

student1 = Student("Алексей", "Алексеев")
student2 = Student("Мария", "Маринина")

# Добавление оценок
lecturer1.add_grade(9)
lecturer1.add_grade(8)

lecturer2.add_grade(10)
lecturer2.add_grade(7)

student1.add_grade(8, "Python")
student1.add_grade(9, "Python")

student2.add_grade(10, "Python")
student2.add_grade(7, "Python")

# Установка курсов
student1.courses_in_progress = ["Python", "Git"]
student1.finished_courses = ["Введение в программирование"]

student2.courses_in_progress = ["Python", "Git"]
student2.finished_courses = ["Введение в программирование"]

# Вызов методов и вывод информации
print(reviewer1)
print(reviewer2)

print(lecturer1)
print(lecturer2)

print(student1)
print(student2)

# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def average_student_grade(students, course_name):
    total_grade = 0
    count = 0
    for student in students:
        for grade, course in student.grades:
            if course == course_name:
                total_grade += grade
                count += 1
    return total_grade / count if count > 0 else 0

# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def average_lecturer_grade(lecturers):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        total_grade += lecturer.average_grade
        count += 1
    return total_grade / count if count > 0 else 0

# Подсчет средней оценки за домашние задания по курсу "Python"
students = [student1, student2]
avg_student_grade = average_student_grade(students, "Python")
print(f'Средняя оценка за домашние задания по курсу "Python": {avg_student_grade:.1f}')

# Подсчет средней оценки за лекции всех лекторов
lecturers = [lecturer1, lecturer2]
avg_lecturer_grade = average_lecturer_grade(lecturers)
print(f'Средняя оценка за лекции всех лекторов: {avg_lecturer_grade:.1f}')
