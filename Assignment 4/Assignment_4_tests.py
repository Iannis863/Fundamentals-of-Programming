from Assignment_4_Classes import MyVector, VectorRepository
import unittest
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.vectors = VectorRepository()
        self.vector = MyVector("Vector", "r", 1, [1, 2, 3])
        self.vector_1 = MyVector("Vector 1", "b", 2, [1, 2, 4])
        self.vector_2 = MyVector("Vector 2", "g", 3, [5, 6, 7])

    def test_init_vector(self):
        self.assertEqual(self.vector.name_id, "Vector")
        self.assertEqual(self.vector.color, "r")
        self.assertEqual(self.vector.type, 1)
        self.assertEqual(str(self.vector.values), "[1 2 3]")

    def test_init_vector_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            vector = MyVector([1,2], "r", 1, [1,2,3])
        self.assertEqual(str(error.exception), "Name id must be of type str.")
        with self.assertRaises(TypeError) as error:
            vector = MyVector("Vector", 1, 1, [1,2,3])
        self.assertEqual(str(error.exception), "Color must be of type str.")
        with self.assertRaises(TypeError) as error:
            vector = MyVector("Vector", "r", "e", [1,2,3])
        self.assertEqual(str(error.exception), "Type must be of type int.")
        with self.assertRaises(TypeError) as error:
            vector = MyVector("Vector", "r", 1, "1, 2, 3")
        self.assertEqual(str(error.exception), "Values must be of type list of integers.")

    def test_init_vector_invalid_value(self):
        with self.assertRaises(ValueError) as error:
            vector = MyVector("Vector", "a", 1, [1,2,3])
        self.assertEqual(str(error.exception), "Color must be 'r', 'g', 'b', 'y' or 'm'.")
        with self.assertRaises(ValueError) as error:
            vector = MyVector("Vector", "r", 0, [1,2,3])
        self.assertEqual(str(error.exception), "Type must be greater or equal than 1.")

    def test_str_vector(self):
        self.assertEqual(str(self.vector), "Vector: color - r, type - 1: [1 2 3]")
        self.assertEqual(str(self.vector_1), "Vector 1: color - b, type - 2: [1 2 4]")
        self.assertEqual(str(self.vector_2), "Vector 2: color - g, type - 3: [5 6 7]")

    def test_get_name_id(self):
        self.assertEqual(self.vector.get_name_id(), "Vector")
        self.assertEqual(self.vector_1.get_name_id(), "Vector 1")
        self.assertEqual(self.vector_2.get_name_id(), "Vector 2")

    def test_get_color(self):
        self.assertEqual(self.vector.get_color(), "r")
        self.assertEqual(self.vector_1.get_color(), "b")
        self.assertEqual(self.vector_2.get_color(), "g")

    def test_get_type(self):
        self.assertEqual(self.vector.get_type(), 1)
        self.assertEqual(self.vector_1.get_type(), 2)
        self.assertEqual(self.vector_2.get_type(), 3)

    def test_get_values(self):
        self.assertEqual(str(self.vector.get_values()), "[1 2 3]")
        self.assertEqual(str(self.vector_1.get_values()), "[1 2 4]")
        self.assertEqual(str(self.vector_2.get_values()), "[5 6 7]")

    def test_set_name_id(self):
        self.assertEqual(MyVector("Vector 1","r",1,[1,2,3]).set_name_id("Vector").__str__(), self.vector.__str__())
        self.assertEqual(MyVector("Vector 2","b",2,[1,2,4]).set_name_id("Vector 1").__str__(), self.vector_1.__str__())
        self.assertEqual(MyVector("Vector", "g", 3, [5,6,7]).set_name_id("Vector 2").__str__(), self.vector_2.__str__())

    def test_set_name_id_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            self.vector.set_name_id(1)
        self.assertEqual(str(error.exception), "Name id must be of type str.")

    def test_set_color(self):
        self.assertEqual(MyVector("Vector","b",1,[1,2,3]).set_color("r").__str__(), self.vector.__str__())

    def test_set_color_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            self.vector.set_color(1)
        self.assertEqual(str(error.exception), "Color must be of type str.")

    def test_set_color_invalid_value(self):
        with self.assertRaises(ValueError) as error:
            self.vector.set_color("red")
        self.assertEqual(str(error.exception), "Color must be 'r', 'g', 'b', 'y' or 'm'.")

    def test_set_type(self):
        self.assertEqual(MyVector("Vector","r",3,[1,2,3]).set_type(1).__str__(), self.vector.__str__())

    def test_set_type_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            self.vector.set_type("e")
        self.assertEqual(str(error.exception), "Type must be of type int.")

    def test_set_type_invalid_value(self):
        with self.assertRaises(ValueError) as error:
            self.vector.set_type(0)
        self.assertEqual(str(error.exception), "Type must be greater or equal than 1.")

    def test_set_values(self):
        self.assertEqual(MyVector("Vector","r",1,[4,5,6]).set_values([1,2,3]).__str__(), self.vector.__str__())
        self.assertEqual(MyVector("Vector 1", "b", 2, [1,2,3]).set_values([1,2,4]).__str__(), self.vector_1.__str__())

    def test_set_values_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            self.vector.set_values(1)
        self.assertEqual(str(error.exception), "Values must be of type list of integers.")

    def test_add_scalar(self):
        self.assertEqual(MyVector("Vector","r",1,[-1,0,1]).add_scalar(2).__str__(),self.vector.__str__())
        self.assertEqual(MyVector("Vector 1", "b", 2, [0,1,3]).add_scalar(1).__str__(), self.vector_1.__str__())

    def test_add_scalar_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            self.vector.add_scalar("e")
        self.assertEqual(str(error.exception), "Scalar must be of type int.")

    def test_add_vector(self):
        vector_1 = MyVector("Vector","r",1,[-1,0,1])
        vector_2 = MyVector("Vector","r",1,[0,2,4])
        vector_3 = MyVector("Vector","r",1,[1,4,6])
        self.assertEqual(vector_1.add_vector([1,2,3]).__str__(),vector_2.__str__())
        self.assertEqual(vector_2.add_vector([1,2,2]).__str__(), vector_3.__str__())

    def test_add_vector_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            self.vector.add_vector(1)
        self.assertEqual(str(error.exception), "Values must be of type list of integers.")

    def test_subtract_vector(self):
        vector_1 = MyVector("Vector","r",1,[3,4,5])
        vector_2 = MyVector("Vector","r",1,[2,2,2])
        vector_3 = MyVector("Vector","r",1,[0,1,2])
        self.assertEqual(vector_1.subtract_vector([1,2,3]).__str__(),vector_2.__str__())
        self.assertEqual(vector_2.subtract_vector([2,1,0]).__str__(), vector_3.__str__())

    def test_subtract_vector_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            self.vector.subtract_vector(1)
        self.assertEqual(str(error.exception), "Values must be of type list of integers.")

    def test_multiplication(self):
        vector_1 = MyVector("Vector","r",1,[3,4,5])
        self.assertEqual(vector_1.multiplication([1,2,3]),26)
        self.assertEqual(vector_1.multiplication([2,1,0]),10)

    def test_multiplication_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            self.vector.multiplication(1)
        self.assertEqual(str(error.exception), "Values must be of type list of integers.")

    def test_sum_vector(self):
        self.assertEqual(self.vector.sum_vector(),6)
        self.assertEqual(self.vector_1.sum_vector(),7)
        self.assertEqual(self.vector_2.sum_vector(),18)

    def test_product_vector(self):
        self.assertEqual(self.vector.product_vector(), 6)
        self.assertEqual(self.vector_1.product_vector(), 8)
        self.assertEqual(self.vector_2.product_vector(), 210)

    def test_avg_vector(self):
        self.assertEqual(self.vector.avg_vector(), 2)
        self.assertEqual(self.vector_1.avg_vector(), np.float64(2.3333333333333335))
        self.assertEqual(self.vector_2.avg_vector(),6)

    def test_min_vector(self):
        self.assertEqual(self.vector.min_vector(), 1)
        self.assertEqual(self.vector_1.min_vector(), 1)
        self.assertEqual(self.vector_2.min_vector(), 5)

    def test_max_vector(self):
        self.assertEqual(self.vector.max_vector(), 3)
        self.assertEqual(self.vector_1.max_vector(), 4)
        self.assertEqual(self.vector_2.max_vector(), 7)

    def test_add_vector_repo(self):
        self.vectors.add_vector(self.vector)
        self.assertEqual(len(self.vectors.vectors), 1)
        self.vectors.add_vector(self.vector_1)
        self.assertEqual(len(self.vectors.vectors), 2)

    def test_add_vector_repo_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            self.vectors.add_vector(1)
        self.assertEqual(str(error.exception), "Vector must be of type MyVector.")

    def test_get_vectors(self):
        self.vectors.add_vector(self.vector)
        self.vectors.add_vector(self.vector_1)
        self.vectors.add_vector(self.vector_2)
        self.assertEqual(self.vectors.get_vectors()[0].__str__(), self.vector.__str__())
        self.assertEqual(self.vectors.get_vectors()[1].__str__(), self.vector_1.__str__())
        self.assertEqual(self.vectors.get_vectors()[2].__str__(), self.vector_2.__str__())

    def test_get_vector(self):
        self.vectors.add_vector(self.vector)
        self.vectors.add_vector(self.vector_1)
        self.vectors.add_vector(self.vector_2)
        self.assertEqual(self.vectors.get_vector(0).__str__(), self.vector.__str__())
        self.assertEqual(self.vectors.get_vector(1).__str__(), self.vector_1.__str__())
        self.assertEqual(self.vectors.get_vector(2).__str__(), self.vector_2.__str__())

    def test_get_vector_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            self.vectors.get_vector("e")
        self.assertEqual(str(error.exception), "Index must be of type int.")

    def test_update_vector_index(self):
        self.vectors.add_vector(self.vector)
        self.vectors.add_vector(self.vector_1)
        self.assertEqual(self.vectors.update_vector_index(0,"Vector 1","b",2,[1,2,4]).vectors[0].__str__(), self.vector_1.__str__())
        self.assertEqual(self.vectors.update_vector_index(1,"Vector 2","g",3,[5,6,7]).vectors[1].__str__(), self.vector_2.__str__())

    def test_update_vector_invalid_type(self):
        self.vectors.add_vector(self.vector)
        with self.assertRaises(TypeError) as error:
            self.vectors.update_vector_index("e","Vector 2","g",3,[1,2,3])
        self.assertEqual(str(error.exception), "Index must be of type int.")
        with self.assertRaises(IndexError) as error:
            self.vectors.update_vector_index(1,"Vector 2","g",3,[1,2,3])
        self.assertEqual(str(error.exception), "Index out of range.")
        with self.assertRaises(TypeError) as error:
            self.vectors.update_vector_index(0,1,"g",3,[1,2,3])
        self.assertEqual(str(error.exception), "Name id must be of type str.")
        with self.assertRaises(TypeError) as error:
            self.vectors.update_vector_index(0,"Vector 2",1,3,[1,2,3])
        self.assertEqual(str(error.exception), "Color must be of type str.")
        with self.assertRaises(TypeError) as error:
            self.vectors.update_vector_index(0,"Vector 2","r","e",[1,2,3])
        self.assertEqual(str(error.exception), "Type must be of type int.")
        with self.assertRaises(TypeError) as error:
            self.vectors.update_vector_index(0,"Vector 2","r",1,1)
        self.assertEqual(str(error.exception), "Values must be of type list of integers.")
        with self.assertRaises(ValueError) as error:
            self.vectors.update_vector_index(0,"Vector 2","a",1,[1,2,3])
        self.assertEqual(str(error.exception), "Color must be 'r','g','b','y','m'.")
        with self.assertRaises(ValueError) as error:
            self.vectors.update_vector_index(0,"Vector 2","r",0,[1,2,3])
        self.assertEqual(str(error.exception), "Type must be greater or equal than 1.")

    def test_update_vector_name_id(self):
        self.vectors.add_vector(self.vector)
        self.vectors.add_vector(self.vector_1)
        self.assertEqual(self.vectors.update_vector_name_id("Vector","Vector 1","b",2,[1,2,4]).vectors[0].__str__(), self.vector_1.__str__())
        self.assertEqual(self.vectors.update_vector_name_id("Vector 1","Vector 2","g",3,[5,6,7]).vectors[1].__str__(), self.vector_2.__str__())

    def test_update_vector_name_id_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            self.vectors.update_vector_name_id(1,"Vector 2","g",3,[1,2])
        self.assertEqual(str(error.exception), "Name id must be of type str.")
        with self.assertRaises(TypeError) as error:
            self.vectors.update_vector_name_id("Vector",1,"g",3,[1,2,3])
        self.assertEqual(str(error.exception), "Name id must be of type str.")
        with self.assertRaises(TypeError) as error:
            self.vectors.update_vector_name_id("Vector","Vector 2",1,3,[1,2,3])
        self.assertEqual(str(error.exception), "Color must be of type str.")
        with self.assertRaises(TypeError) as error:
            self.vectors.update_vector_name_id("Vector","Vector 2","r","e",[1,2,3])
        self.assertEqual(str(error.exception), "Type must be of type int.")
        with self.assertRaises(TypeError) as error:
            self.vectors.update_vector_name_id("Vector","Vector 2","r",1,1)
        self.assertEqual(str(error.exception), "Values must be of type list of integers.")
        with self.assertRaises(ValueError) as error:
            self.vectors.update_vector_name_id("Vector","Vector 2","a",1,[1,2,3])
        self.assertEqual(str(error.exception), "Color must be 'r','g','b','y','m'.")
        with self.assertRaises(ValueError) as error:
            self.vectors.update_vector_name_id("Vector","Vector 2","r",0,[1,2,3])
        self.assertEqual(str(error.exception), "Type must be greater or equal than 1.")

    def test_delete_vector_index(self):
        self.vectors.add_vector(self.vector)
        self.vectors.add_vector(self.vector_1)
        self.assertEqual(self.vectors.delete_vector_index(0).vectors[0].__str__(), self.vector_1.__str__())
        self.vectors.add_vector(self.vector)
        self.assertEqual(self.vectors.delete_vector_index(0).vectors[0].__str__(), self.vector.__str__())
        self.vectors.add_vector(self.vector_1)

    def test_delete_vector_index_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            self.vectors.delete_vector_index("e")
        self.assertEqual(str(error.exception), "Index must be of type int.")

    def test_delete_vector_name_id(self):
        self.vectors.add_vector(self.vector)
        self.vectors.add_vector(self.vector_1)
        self.assertEqual(self.vectors.delete_vector_name_id("Vector 1").vectors[0].__str__(), self.vector.__str__())
        self.vectors.add_vector(self.vector_1)
        self.assertEqual(self.vectors.delete_vector_name_id("Vector").vectors[0].__str__(), self.vector_1.__str__())
        self.vectors.add_vector(self.vector)

    def test_delete_vector_name_id_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            self.vectors.delete_vector_name_id(1)
        self.assertEqual(str(error.exception), "Name or id must be of type str.")

    def test_sum_vectors_color(self):
        self.vectors.add_vector(self.vector)
        self.vectors.add_vector(self.vector_1)
        self.vectors.add_vector(self.vector_2)
        self.assertEqual(self.vectors.sum_vectors_color("r"), 6)
        self.assertEqual(self.vectors.sum_vectors_color("b"), 7)
        self.assertEqual(self.vectors.sum_vectors_color("g"), 18)

    def test_delete_all_vectors(self):
        self.vectors.add_vector(self.vector)
        self.assertEqual(self.vectors.delete_all_vectors(),None)
        self.vectors.add_vector(self.vector)
        self.vectors.add_vector(self.vector_1)
        self.assertEqual(self.vectors.delete_all_vectors(), None)
        self.vectors.add_vector(self.vector)
        self.vectors.add_vector(self.vector_1)
        self.vectors.add_vector(self.vector_2)
        self.assertEqual(self.vectors.delete_all_vectors(), None)

    def test_update_color_name_id(self):
        self.vectors.add_vector(self.vector)
        self.vectors.add_vector(self.vector_1)
        self.vectors.add_vector(self.vector_2)
        self.assertEqual(self.vectors.update_color_name_id("Vector", "b")[0].__str__(), MyVector("Vector", "b", 1 , [1,2,3]).__str__())
        self.assertEqual(self.vectors.update_color_name_id("Vector", "g")[0].__str__(), MyVector("Vector", "g", 1 , [1,2,3]).__str__())
        self.assertEqual(self.vectors.update_color_name_id("Vector", "m")[0].__str__(), MyVector("Vector", "m", 1 , [1,2,3]).__str__())

