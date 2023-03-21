class Person:                       # класс "Человек"
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Parent(Person):               # класс "Родитель"
    ...


class Teacher(Person):              # класс "Учитель"
    def __init__(self, name, subject, classes):
        super().__init__(name)
        self.subject = subject
        self.classes = classes

        for class_item in classes:
            class_item.add_teacher(self)


class Student(Person):              # класс "Ученик"
    def __init__(self, name, my_class, mother, father):
        # super().__init__(name)
        self.name = name
        self.my_class = my_class
        self.mother = mother
        self.father = father

        my_class.add_student(self)

    def __repr__(self):
        return self.name


class Subject:                     # класс "Предмет"
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title


class Class:                        # класс "Класс"
    def __init__(self, title):
        self.title = title
        self.students = []
        self.teachers = []

    def add_student(self, student):         # добавление ученика в класс
        self.students.append(student)

    def add_teacher(self, teacher):         # добавление учителя в класс
        self.teachers.append(teacher)

    def __repr__(self):
        return self.title


class School:                       # класс "Школа"
    def __init__(self, name, classes):
        self.name = name
        self.classes = classes

    def __repr__(self):
        return self.name

    def __repr__(self):
        return self.classes


    def get_classes(self):                              # список классов школы
        print("классы школы: ", self.classes, "\n")

    def get_students_in_class(self, class_name):        # список учеников класса
        print(f"Ученики {class_name} класса школы {self.name}: ")
        for class_item in self.classes:
            if class_name == class_item.title:
                print(class_item.students, "\n")

    def get_teachers_in_class(self, class_name):        # список учетилей класса
        print(f"Список учителей класса {class_name}:")
        for class_item in self.classes:
            if class_name == class_item.title:
                print(class_item.teachers, "\n")

    def get_subjects_in_class(self, class_name):        # список предметов класса
        print(f"Список предметов класса {class_name}: ")
        for class_item in self.classes:
            if class_name == class_item.title:
                for teacher in class_item.teachers:
                    print(teacher.subject)

    def get_subjects_in_student(self, student_name):
        print(f"Список предметов ученика {student_name}: ")
        for c in self.classes:
            for student in c.students:
                if str(student) == student.name:            # если ученик в классе №


    # def get_parent_in_class(self, class_name):
    #     print(f"Список родителей учеников класса {class_name}: ")
    #     for class_item in self.classes:
    #         if class_name == class_item.title:
    #             print(class_item.parent, "\n")

class_1A = Class("1 А")                                                 # создаём классы
class_1B = Class("1 Б")
class_5A = Class("5 А")
class_5B = Class("5 Б")

parent1 = Parent("Г-н Иванов")                                          # создаём учеников с их родителями
parent2 = Parent("Г-жа Иванова")
child1 = Student("Иванов Иван", class_1A, parent1, parent2)             # все двойняшки :)
child2 = Student("Иванова Мария", class_1A, parent1, parent2)

parent3 = Parent("Г-н Сидоров")
parent4 = Parent("Г-жа Сидорова")
child3 = Student("Сидоров Пётр", class_1B, parent3, parent4)
child4 = Student("Сидорова Наталья", class_1B, parent3, parent4)

parent5 = Parent("Г-н Петров")
parent6 = Parent("Г-жа Петрова")
child5 = Student("Петров Сергей", class_5A, parent5, parent6)
child6 = Student("Петрова Анастасия", class_5A, parent5, parent6)

parent7 = Parent("Г-н Шариков")
parent8 = Parent("Г-жа Шарикова")
child7 = Student("Шариков Андрей", class_5B, parent7, parent8)
child8 = Student("Шарикова Анна", class_5B, parent7, parent8)

subject1 = Subject("Математика")                                        # создаём предметы
subject2 = Subject("Литература")
subject3 = Subject("Окружающий мир")
subject4 = Subject("Физика")
subject5 = Subject("Химия")

teacher1 = Teacher("Учитель Архимед", subject1, [class_1A, class_1B, class_5A, class_5B])   # создаём учителей
teacher2 = Teacher("Учитель Гололь", subject2, [class_1B, class_5A])
teacher3 = Teacher("Учитель Шекспир", subject2, [class_1A, class_5B])
teacher4 = Teacher("Учитель Циолковский", subject3, [class_1A, class_1B])
teacher5 = Teacher("Учитель Ньютон", subject4, [class_5A, class_5B])
teacher6 = Teacher("Учитель Менделеев", subject5, [class_5A, class_5B])

school = School("№ 55", [class_1A, class_1B, class_5A, class_5B])
# school.get_classes()
# school.get_students_in_class("1 А")
# school.get_students_in_class("1 Б")
# school.get_students_in_class("5 А")
# school.get_students_in_class("5 Б")
# school.get_subjects_in_class("1 А")
# school.get_subjects_in_class("1 Б")
# school.get_subjects_in_class("5 А")
# school.get_subjects_in_class("5 Б")
# school.get_teachers_in_class("1 Б")
# school.get_teachers_in_class("1 А")
# school.get_teachers_in_class("5 А")
# school.get_teachers_in_class("5 Б")
school.get_subjects_in_student("Иванов Иван")