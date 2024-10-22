from Functions import *
import unittest

class TestFunctions(unittest.TestCase):
    def test_add_1(self):
        lst = []
        self.assertEqual(add(lst, 1), [1])
    def test_add_2(self):
        lst = [1]
        self.assertEqual(add(lst, 2), [1,2])
    def test_add_invalid_type(self):
        with self.assertRaises(TypeError):
            add(1,1)

    def test_insert_1(self):
        lst = []
        self.assertEqual(insert(lst, 0,1), [1])
    def test_insert_2(self):
        lst = [1]
        self.assertEqual(insert(lst, 1,2), [1,2])
    def test_insert_invalid_type(self):
        with self.assertRaises(TypeError):
            insert(1,1,1)

    def test_remove_1(self):
        lst = [1,2,3]
        self.assertEqual(remove(lst, 1), [2,3])
    def test_remove_2(self):
        lst = [1,2,3]
        self.assertEqual(remove(lst, 2), [1,3])
    def test_remove_invalid_type(self):
        with self.assertRaises(TypeError):
            remove(1,1)

    def test_remove_range_1(self):
        lst = [1,2,3]
        self.assertEqual(remove_range(lst, 1,2), [1])
    def test_remove_range_2(self):
        lst = [1,2,3]
        self.assertEqual(remove_range(lst, 2,2), [1,2])
    def test_remove_range_invalid_type(self):
        with self.assertRaises(TypeError):
            remove_range(1,1,1)

    def test_replace_1(self):
        lst = [1,2,3]
        self.assertEqual(replace(lst, 1,2), [2,2,3])
    def test_replace_2(self):
        lst = [1,2,3]
        self.assertEqual(replace(lst, 2,3), [1,3,3])
    def test_replace_invalid_type(self):
        with self.assertRaises(TypeError):
            replace(1,1,1)

    def test_prime_1(self):
        lst = [1,2,3]
        self.assertEqual(prime(lst,0,2), [2,3])
    def test_prime_2(self):
        lst = [1,2,3]
        self.assertEqual(prime(lst,1,2), [2,3])
    def test_prime_invalid_type(self):
        with self.assertRaises(TypeError):
            prime(1,1,1)

    def test_odd_1(self):
        lst = [1,2,3]
        self.assertEqual(odd(lst,0,2), [1,3])
    def test_odd_2(self):
        lst = [1,2,3]
        self.assertEqual(odd(lst,1,2), [3])
    def test_odd_invalid_type(self):
        with self.assertRaises(TypeError):
            odd(1,1,1)

    def test_sum_1(self):
        lst = [1,2,3]
        self.assertEqual(sum_s(lst,0,2), 6)
    def test_sum_2(self):
        lst = [1,2,3]
        self.assertEqual(sum_s(lst,1,2), 5)
    def test_sum_invalid_type(self):
        with self.assertRaises(TypeError):
            sum_s(1,1,1)

    def test_gcd_1(self):
        lst = [1,2,3]
        self.assertEqual(gcd(lst,0,2), 1)
    def test_gcd_2(self):
        lst = [1,2,3]
        self.assertEqual(gcd(lst,1,2), 1)
    def test_gcd_invalid_type(self):
        with self.assertRaises(TypeError):
            gcd(1,1,1)

    def test_max_1(self):
        lst = [1,2,3]
        self.assertEqual(max_x(lst,0,2), 3)
    def test_max_2(self):
        lst = [1,2,3]
        self.assertEqual(max_x(lst,1,2), 3)
    def test_max_invalid_type(self):
        with self.assertRaises(TypeError):
            max_x(1,1,1)

    def test_filter_prime_1(self):
        lst = [1,2,3]
        self.assertEqual(filter_prime(lst),[2,3])
    def test_filter_prime_2(self):
        lst = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(filter_prime(lst),[2,3,5,7])
    def test_filter_prime_invalid_type(self):
        with self.assertRaises(TypeError):
            filter_prime(1)

    def test_filter_negatives_1(self):
        lst = [1,2,3]
        self.assertEqual(filter_negatives(lst),[])
    def test_filter_negatives_2(self):
        lst = [1,-2,3,-4,5,-6,7,-8,9]
        self.assertEqual(filter_negatives(lst),[-2,-4,-6,-8])
    def test_filter_negatives_invalid_type(self):
        with self.assertRaises(TypeError):
            filter_negatives(1)

    """
    def test_undo_1(self):
        lst = [1,2,3]
        l_undo = [1,2]
        self.assertEqual(undo(lst),l_undo)
    """


if __name__ == '__main__':
    unittest.main()

