from Sem_4_Functions import *
import unittest

class TestFunctions(unittest.TestCase):

    def test_print_students(self):
        list_students_grades = [("Iannis",10)]
        self.assertEqual(print_students(list_students_grades), print("Iannis",10))

    def test_student_add(self):
        list_student_grades = [("Iannis",10)]
        self.assertEqual(student_add(list_student_grades,"Felix",9), [("Iannis",10),("Felix",9)])

    def test_find_by_name(self):
        list_student_grades = [("Iannis",10)]
        self.assertEqual(find_by_name(list_student_grades,"Iannis"), ("Iannis",10))

    def test_delete_by_name(self):
        list_student_grades = [("Iannis",10),("Felix",9)]
        self.assertEqual(delete_by_name(list_student_grades,"Felix"),[("Iannis",10)])

    def test_grades_higher_than(self):
        list_student_grades = [("Iannis",10)]
        self.assertEqual(grades_higher_than(list_student_grades,9), [("Iannis",10)])

    def test_maximum_grade(self):
        list_student_grades = [("Iannis",10),("Felix",9)]
        self.assertEqual(maximum_grade(list_student_grades),("Iannis",10))

    def test_name_starting_with(self):
        list_student_grades = [("Iannis",10),("Ianos",8),("Felix",9)]
        self.assertEqual(name_starting_with(list_student_grades,"Ian"),[("Iannis",10),("Ianos",8)])

    def test_remove_grade_smaller_than_5(self):
        list_student_grades = [("Iannis",10),("Ianos",4),("Felix",9)]
        self.assertEqual(remove_grade_smaller_5(list_student_grades),[("Iannis",10),("Felix",9)])

    def test_delete_name_palindrome(self):
        list_student_grades = [("Iannis",10),("ana,9")]
        self.assertEqual(delete_name_palindrome(list_student_grades),[("Iannis",10)])

    def test_frequency_name(self):
        list_student_grades = [("Iannis",10),("Felix",9),("Iannis",8)]
        self.assertEqual(frequency_name(list_student_grades,"Iannis"),2)

    def test_average_grade(self):
        list_student_grades = [("Iannis",10),("Ianos",4),("Felix",9)]
        self.assertEqual(average_grade(list_student_grades),9.5)

    def test_sort_students_by_grade(self):
        list_students_grades = [("Madalin",8),("Iannis",10),("Felix",9)]
        self.assertEqual(sort_students_by_grade(list_students_grades),[("Iannis",10),("Felix",9),("Madalin",8)])

    def test_top_n_students_by_grade(self):
        list_students_grades = [("Madalin", 8), ("Iannis", 10), ("Felix", 9)]
        self.assertEqual(top_n_students_by_grade(list_students_grades,2), [("Iannis", 10), ("Felix", 9)])

if __name__ == '__main__':
    unittest.main()