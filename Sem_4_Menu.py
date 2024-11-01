from Sem_4_Functions import *

def menu(list_students_grades):
    """
    The menu for the user to use the functions
    :param list_students_grades: The list of students and their grades
    """
    print("""
    Menu:
    1. Show all the students and their grades
    2. Add a student
    3. Find a student by name
    4. Delete a student by name
    5. Show all student with grades higher than a number
    6. Show the student with the maximum grade
    7. Show all the students whose name start with a string
    8. Remove all the students with a grade smaller than 5
    9. Remove all the students whose name are palindrome
    10. Compute the frequency of a name
    11. Compute the average grade of students whose grade is greater than 5
    12. Sort the students by grade (descending)
    13. Show the top n students by grade
    14. Exit
    """)
    while True:
        user_input = input()
        if user_input == "exit":
            break
        elif user_input == '1':
            print(list_students_grades)
        elif user_input == '2':
            print("Type the name of the student")
            name = input()
            print("Type the grade of the student")
            student_add(list_students_grades, name, int(input()))
        elif user_input == '3':
            print("Type the name of the student")
            print(find_by_name(list_students_grades, input()))
        elif user_input == '4':
            print("Type the name of the student")
            delete_by_name(list_students_grades, input())
        elif user_input == '5':
            print("Type the grade")
            print(grades_higher_than(list_students_grades,int(input())))
        elif user_input == '6':
            print(maximum_grade(list_students_grades))
        elif user_input == '7':
            print("Type the string")
            print(name_starting_with(list_students_grades, input()))
        elif user_input == '8':
            print(remove_grade_smaller_5(list_students_grades))
        elif user_input == '9':
            print(delete_name_palindrome(list_students_grades))
        elif user_input == '10':
            print("Type the name of the student")
            print(frequency_name(list_students_grades, input()))
        elif user_input == '11':
            print(average_grade(list_students_grades))
        elif user_input == '12':
            print(sort_students_by_grade(list_students_grades))
        elif user_input == '13':
            print("Type a nuber")
            print(top_n_students_by_grade(list_students_grades, int(input())))
        else: print("Incorrect input")

if __name__ == '__main__':
    list_students_grades = []
    menu(list_students_grades)