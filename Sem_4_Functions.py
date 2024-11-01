students_and_grades = [("Madalin",8),("Iannis",10),("Felix",9)]

def print_students(list_students_grades:list):
    """
    Print all the students and their grades
    :param list_students_grades: The list of students and their grades
    :raises TypeError: If the list_students_grades is not a list
    """
    if not isinstance(list_students_grades, list):
        raise TypeError("The list_students_grades is not a list")
    print(list_students_grades)

def student_add(list_students_grades:list,student:str,grade:int):
    """
    Add a new student and a grade to the list
    :param list_students_grades: The list where the student is added
    :param student: The name of the student
    :param grade: The grade of the student
    :return list_students_grades: The updated list
    :raises TypeError: If the input data is incorrect
    """
    if not isinstance(list_students_grades,list) or not isinstance(student,str) or not isinstance(grade,int):
        raise TypeError("Invalid input")
    list_students_grades.append((student,grade))
    return list_students_grades

def find_by_name(list_students_grades:list,name:str):
    """
    Find a student by name
    :param list_students_grades: The list of students and their grades
    :param name: The name of the student to find
    :return i: The student and the grade of the student
    raises TypeError: If the input data is incorrect
    """
    if not isinstance(list_students_grades,list) or not isinstance(name,str):
        raise TypeError("Invalid input")
    for i in list_students_grades:
        if i[0] == name:
            return i

def delete_by_name(list_students_grades:list,name:str):
    """
    Delete a student by name
    :param list_students_grades: The list of students and their grades
    :param name: The name of the student to delete
    :return list_students_grades: The updated list
    raises TypeError: If the input data is incorrect
    """
    if not isinstance(list_students_grades,list) or not isinstance(name,str):
        raise TypeError("Invalid input")
    for i in list_students_grades:
        if i[0] == name:
            list_students_grades.remove(i)
    return list_students_grades

def grades_higher_than(list_students_grades:list,grade:int):
    """
    Show all the students that have a higher grade than grade
    :param list_students_grades: The list of students and their grades
    :param grade: The grade to be compared to
    :return higher_grades: The list of students that have a higher grade
    :raises TypeError: If the input data is incorrect
    """
    if not isinstance(list_students_grades,list) or not isinstance(grade,int):
        raise TypeError("Invalid input")
    higher_grades = []
    for i in list_students_grades:
        if i[1] > grade:
            higher_grades.append(i)
    return higher_grades

def maximum_grade(list_students_grades:list):
    """
    Find the stundent with the maximu grade
    :param list_students_grades: The list of students and their grades
    :return student_max_grade: The student with the maximum grade
    raises TypeError: If the input data is incorrect
    """
    if not isinstance(list_students_grades,list):
        raise TypeError("Invalid input")
    max_grade = 0
    student_max_grade = []
    for i in list_students_grades:
        if i[1] > max_grade:
            max_grade = i[1]
            student_max_grade = i
    return student_max_grade

def name_starting_with(list_students_grades:list, start:str):
    """
    Find the students whose name start with a specified string
    :param list_students_grades: The list of students and their grades
    :param start: The string to start with
    :return start_name: The list with all the students whose name start with the specified string
    raises TypeError: If the input data is incorrect
    """
    if not isinstance(list_students_grades,list) or not isinstance(start,str):
        raise TypeError("Invalid input")
    start_name = []
    for i in list_students_grades:
        if i[0].startswith(start):
            start_name.append(i)
    return start_name

def remove_grade_smaller_5(list_students_grades:list):
    """
    Remove all the students with a grade smaller than 5
    :param list_students_grades: The list of students and their grades
    :return list_students_grades: The updated list
    :raises TypeError: If the input data is incorrect
    """
    if not isinstance(list_students_grades,list):
        raise TypeError("Invalid input")
    for i in list_students_grades:
        if i[1] < 5:
            list_students_grades.remove(i)
    return list_students_grades

def is_palindrome(string:str):
    """
    Check if a string is a Palindorme
    :param string: The string to check
    :return: True if the string is a Palindorme, False otherwise
    :raises TypeError: If the input data is incorrect
    """
    if not isinstance(string,str):
        raise TypeError("Invalid input")
    string = string.lower()
    return string == string[::-1]

def delete_name_palindrome(list_students_grades:list):
    """
    Delete the students whose names are palindromes
    :param list_students_grades: The list of students and their grades
    :return list_students_grades: The updated list
    :raises TypeError: If the input data is incorrect
    """
    if not isinstance(list_students_grades,list):
        raise TypeError("Invalid input")
    for i in list_students_grades:
        if is_palindrome(str(i[0])):
            list_students_grades.remove(i)
    return list_students_grades

def frequency_name(list_students_grades:list, name:str):
    """
    Determine the frequency of a name
    :param list_students_grades: The list of students and their grades
    :param name: The name for which the frequency is to be determined
    :return name_frequency: The frequency of the name
    :raises TypeError: If the input data is incorrect
    """
    if not isinstance(list_students_grades,list) or not isinstance(name,str):
        raise TypeError("Invalid input")
    name_frequency = 0
    for i in list_students_grades:
        if i[0] == name:
            name_frequency += 1
    return name_frequency

def average_grade(list_students_grades:list):
    """
    Compute the average grade of students with a grade higher than 5
    :param list_students_grades: The list of students and their grades
    :return average: The average grade of the students
    :raises TypeError: If the input data is incorrect
    """
    if not isinstance(list_students_grades,list):
        raise TypeError("Invalid input")
    sum = 0.0
    for i in list_students_grades:
        if i[1] > 5:
            sum += i[1]
    return sum / len(remove_grade_smaller_5(list_students_grades))

def sort_students_by_grade(list_students_grades:list):
    """
    Sort all the students by grade in descending order
    :param list_students_grades: The list of students and their grades
    :return sorted_list: The sorted list
    :raises TypeError: If the input data is incorrect
    """
    if not isinstance(list_students_grades,list):
        raise TypeError("Invalid input")
    list_students_grades.sort(key = lambda x: x[1], reverse = True)
    return list_students_grades

def top_n_students_by_grade(list_students_grade:list,n:int):
    """
    Find the top students according to their grade
    :param list_students_grade: The list of students and their grades
    :param n: The number of students in the top
    :return: The list of the top n students
    :raises TypeError: If the input data is incorrect
    """
    if not isinstance(list_students_grade,list) or not isinstance(n,int):
        raise TypeError("Invalid input")
    return sort_students_by_grade(list_students_grade)[:n]