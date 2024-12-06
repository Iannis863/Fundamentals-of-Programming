from Seminar_9 import *
import unittest

class TestRecursionFunctions(unittest.TestCase):
    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_ten(self):
        self.assertEqual(fibonacci(10), 55)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_five(self):
        self.assertEqual(factorial(5), 120)

    def test_f_n_3_zero(self):
        self.assertEqual(f_n_3(0), 0)

    def test_f_n_3_five(self):
        self.assertEqual(f_n_3(5), 15)

    def test_recursive_sum_zero(self):
        self.assertEqual(recursive_sum(0), 0)

    def test_recursive_sum_ten(self):
        self.assertEqual(recursive_sum(10), 55)

    def test_pascal_triangle_zero(self):
        self.assertEqual(pascal_triangle(0), [1])

    def test_pascal_triangle_five(self):
        self.assertEqual(pascal_triangle(5), [1, 5, 10, 10, 5, 1])

    def test_min_recursion_zero(self):
        self.assertEqual(min_recursion([]), 1000000000)

    def test_min_recursion_ten(self):
        self.assertEqual(min_recursion([1,2,3,0]), 0)

    def test_max_recursion_zero(self):
        self.assertEqual(max_recursion([]), 0)

    def test_max_recursion_ten(self):
        self.assertEqual(max_recursion([10,8,7,9]), 10)

    def test_recursive_min_single(self):
        self.assertEqual(recursive_min([5]), 5)

    def test_recursive_min_nested(self):
        self.assertEqual(recursive_min([3, [2, [1]]]), 1)

    def test_number_of_occurrences_empty(self):
        self.assertEqual(number_of_occurrences([], 1), 0)

    def test_number_of_occurrences_nested(self):
        self.assertEqual(number_of_occurrences([1, [1, [1]]], 1), 3)

    def test_sequential_search_found(self):
        self.assertEqual(sequential_search_recursive([1, 2, 3], 2), 1)

    def test_sequential_search_not_found(self):
        self.assertEqual(sequential_search_recursive([1, 2, 3], 4), -1)

    def test_binary_search_found(self):
        self.assertEqual(binary_search_recursive([1, 2, 3, 4, 5], 5), 4)

    def test_binary_search_not_found(self):
        self.assertEqual(binary_search_recursive([1, 2, 3, 4, 5], 6), -1)

if __name__ == '__main__':
    unittest.main()