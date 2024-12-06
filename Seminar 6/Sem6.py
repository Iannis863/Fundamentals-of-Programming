class Student:
    def __init__(self, id:int, name:str, grades:list, group:str):
        self.id = id
        self.name = name
        self.grades = grades
        self.group = group

    def __str__(self):
        return str(self.id) + ". " + self.name + " - " + str(self.grades) + " - " + self.group

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_grades(self):
        return self.grades

    def get_group(self):
        return self.group

    def set_id(self, id:int):
        self.id = id

    def set_name(self, name:str):
        self.name = name

    def set_grades(self, grades:list):
        self.grades = grades

    def set_group(self, group:str):
        self.group = group

    def __eq__(self, other):
        return self.id == other.__id and self.name == other.__name and self.grades == other.__grades and self.group == other.__group


class StudentRepository:
    def __init__(self):
        self.__students = []

    def add_student(self, student:Student):
        self.__students.append(student)

    def insert_student(self, student:Student, index:int):
        self.__students.insert(index,student)

    def nr_of_students(self):
        return len(self.__students)

    def get_index(self, id:int):
        return [index for index,student in enumerate(self.__students) if student.id == id]

    def get_students(self):
        return [student.__str__() for student in self.__students]

    def get_student(self, id:int):
        return [student.__str__() for student in self.__students if student.id == id]

    def update_student_index(self, index:int, student:Student):
        self.__students[index] = student

    def update_student_id(self, student:Student, id:int):
        index = self.get_index(id)[0]
        self.update_student_index(index, student)

    def delete_student_index(self, index:int):
        self.__students.pop(index)

    def delete_student_id(self, id:int):
        index = self.get_index(id)[0]
        self.delete_student_index(index)

    def get_student_max_avg_grade(self):
        max_avg_grade = 0
        for i, student in enumerate(self.__students):
            if sum(student.grades) / len(student.grades) >= max_avg_grade:
                max_avg_grade = sum(student.grades) / len(student.grades)
                std = i
        return self.__students[std]

    def get_student_max_grade(self):
        max_grade = 0
        for i, student in enumerate(self.__students):
            if max(student.grades) >= max_grade:
                max_grade = max(student.grades)
                std = i
        return self.__students[std]

    def get_avg_max_grade_group(self, group:str):
        return sum([max(student.grades) for student in self.__students if student.group == group]) / len([student for student in self.__students if student.group == group])

    def get_min_grade_group(self, group:str):
        return min([min(student.grades) for student in self.__students if student.group == group])

    