from Assignment_3_Classes import *
import unittest

class TestFunctions(unittest.TestCase):
    def test_init_valid_input(self):
        point = MyPoint((1,2),'red')
        self.assertEqual(point.position, (1,2))
        self.assertEqual(point.color, 'red')

    def test_init_invalid_coordinates(self):
        with self.assertRaises(TypeError) as error:
            MyPoint((3, '4'), 'red')
        self.assertEqual(str(error.exception), "The coordinates must be a tuple of 2 integers")

    def test_init_invalid_color_type(self):
        with self.assertRaises(TypeError) as error:
            MyPoint((3, 4), 123)
        self.assertEqual(str(error.exception), "The color must be a string")

    def test_init_invalid_color_value(self):
        with self.assertRaises(ValueError) as error:
            MyPoint((3, 4), 'orange')
        self.assertEqual(str(error.exception), "The color should be red, green, blue, yellow or magenta")

    def test_get_x(self):
        point = MyPoint((1,2),'red')
        self.assertEqual(point.get_x(), 1)

    def test_get_y(self):
        point = MyPoint((1,2),'red')
        self.assertEqual(point.get_y(), 2)

    def test_get_color(self):
        point = MyPoint((1,2),'red')
        self.assertEqual(point.get_color(), 'red')

    def test_set_x(self):
        point = MyPoint((1,2),'red')
        point.set_x(2)
        self.assertEqual(point.get_x(), 2)

    def test_set_x_invalid(self):
        with self.assertRaises(TypeError) as error:
            point = MyPoint((1,2),'red')
            point.set_x('a')
            self.assertEqual(str(error.exception), "The coordinates must be integers")

    def test_set_y(self):
        point = MyPoint((1,2),'red')
        point.set_y(3)
        self.assertEqual(point.get_y(), 3)

    def test_set_y_invalid(self):
        with self.assertRaises(TypeError) as error:
            point = MyPoint((1,2),'red')
            point.set_y('a')
            self.assertEqual(str(error.exception), "The coordinates must be integers")

    def test_set_color(self):
        point = MyPoint((1,2),'red')
        point.set_color('blue')
        self.assertEqual(point.get_color(), 'blue')

    def test_set_color_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            point = MyPoint((1,2),'red')
            point.set_color(1)
            self.assertEqual(str(error.exception), "The color must be a string")

    def test_set_color_invalid_value(self):
        with self.assertRaises(ValueError) as error:
            point = MyPoint((1,2),'red')
            point.set_color('black')
            self.assertEqual(str(error.exception), "The color should be red, green, blue, yellow or magenta")

    def test_update(self):
        point = MyPoint((1,2),'red')
        point.update((2,3),'blue')
        self.assertEqual(point.get_x(), 2)
        self.assertEqual(point.get_y(), 3)
        self.assertEqual(point.get_color(), 'blue')

    def test_update_invalid_coordinates(self):
        with self.assertRaises(TypeError) as error:
            point = MyPoint((1,2),'red')
            point.update((2,3,4),'blue')
            self.assertEqual(str(error.exception), "The coordinates must be a tuple of 2 integer")

    def test_update_invalid_color_type(self):
        with self.assertRaises(TypeError) as error:
            point = MyPoint((1,2),'red')
            point.update((2,3),1)
            self.assertEqual(str(error.exception), "The color must be a string")

    def test_update_invalid_color_value(self):
        with self.assertRaises(ValueError) as error:
            point = MyPoint((1,2),'red')
            point.update((2,3), 'black')
            self.assertEqual(str(error.exception), "The color should be red, green, blue, yellow or magenta")

    def test_str(self):
        point = MyPoint((1,2),'red')
        self.assertEqual(str(point), "Point (1,2) of color red")

    def test_add_point(self):
        points = PointRepository()
        point = MyPoint((1,2),"red")
        self.assertEqual(points.add_point(point),"Point (1,2) of color red")

    def test_get_points(self):
        points = PointRepository()
        point_1 = MyPoint((1,2),"red")
        point_2 = MyPoint((3,4),"blue")
        points.add_point(point_1)
        points.add_point(point_2)
        self.assertEqual(points.get_points(), "Point (1,2) of color red, Point (3,4) of color blue")

    def test_str_repo(self):
        points = PointRepository()
        point = MyPoint((1,2),"red")
        points.add_point(point)
        self.assertEqual(points.__str__(), "Point (1,2) of color red")

    def test_get_point(self):
        points = PointRepository()
        point = MyPoint((1, 2), "red")
        points.add_point(point)
        self.assertEqual(points.get_point(0), "Point (1,2) of color red")

    def test_get_points_color(self):
        points = PointRepository()
        point_1 = MyPoint((1, 2), "red")
        point_2 = MyPoint((3,4), "blue")
        point_3 = MyPoint((5,6), "red")
        points.add_point(point_1)
        points.add_point(point_2)
        points.add_point(point_3)
        self.assertEqual(points.get_points_color("red"), "Point (1,2) of color red, Point (5,6) of color red")

    def test_get_points_square(self):
        points = PointRepository()
        point_1 = MyPoint((1,2),"red")
        point_2 = MyPoint((3,4),"blue")
        point_3 = MyPoint((5,6),"green")
        points.add_point(point_1)
        points.add_point(point_2)
        points.add_point(point_3)
        self.assertEqual(points.get_points_square((3,6),2),"Point (3,4) of color blue, Point (5,6) of color green")

    def test_distance(self):
        points = PointRepository()
        point_1 = MyPoint((1,2),"red")
        point_2 = MyPoint((4,6),"blue")
        points.add_point(point_1)
        points.add_point(point_2)
        self.assertEqual(points.distance(0,1),5)

    def test_min_distance(self):
        points = PointRepository()
        point_1 = MyPoint((1, 2), "red")
        point_2 = MyPoint((10, 11), "blue")
        point_3 = MyPoint((4, 6), "green")
        points.add_point(point_1)
        points.add_point(point_2)
        points.add_point(point_3)
        self.assertEqual(points.get_min_distance(),5)

    def test_update_repo(self):
        points = PointRepository()
        point_1 = MyPoint((1,2),"red")
        point_2 = MyPoint((5,6),"green")
        points.add_point(point_1)
        points.add_point(point_2)
        self.assertEqual(points.update(0,(3,4),"blue"), "Point (3,4) of color blue, Point (5,6) of color green")

    def test_delete_point(self):
        points = PointRepository()
        point_1 = MyPoint((1,2),"red")
        point_2 = MyPoint((5,6),"green")
        points.add_point(point_1)
        points.add_point(point_2)
        self.assertEqual(points.delete_point(1), "Point (1,2) of color red")

    def test_delete_points_square(self):
        points = PointRepository()
        point_1 = MyPoint((1, 2), "red")
        point_2 = MyPoint((3, 4), "blue")
        point_3 = MyPoint((5, 6), "green")
        points.add_point(point_1)
        points.add_point(point_2)
        points.add_point(point_3)
        self.assertEqual(points.delete_points_square((3,6),2),"Point (1,2) of color red")

    def test_get_points_circle(self):
        points = PointRepository()
        point_1 = MyPoint((1,2),"red")
        point_2 = MyPoint((5,6),"green")
        points.add_point(point_1)
        points.add_point(point_2)
        self.assertEqual(points.get_points_circle((3,4),2),"Point (1,2) of color red, Point (5,6) of color green")

    def test_get_points_rectangle(self):
        points = PointRepository()
        point_1 = MyPoint((1, 2), "red")
        point_2 = MyPoint((3, 4), "blue")
        point_3 = MyPoint((5, 6), "green")
        points.add_point(point_1)
        points.add_point(point_2)
        points.add_point(point_3)
        self.assertEqual(points.get_points_rectangle((3,6),2,2),"Point (3,4) of color blue, Point (5,6) of color green")

    def test_get_max_distance(self):
        points = PointRepository()
        point_1 = MyPoint((1, 2), "red")
        point_2 = MyPoint((3, 4), "blue")
        point_3 = MyPoint((4, 6), "green")
        points.add_point(point_1)
        points.add_point(point_2)
        points.add_point(point_3)
        self.assertEqual(points.get_max_distance(),5)

    def test_nr_points_color(self):
        points = PointRepository()
        point_1 = MyPoint((1, 2), "red")
        point_2 = MyPoint((3, 4), "blue")
        point_3 = MyPoint((5, 6), "red")
        points.add_point(point_1)
        points.add_point(point_2)
        points.add_point(point_3)
        self.assertEqual(points.nr_points_color("red"),2)

    def test_update_color(self):
        points = PointRepository()
        point_1 = MyPoint((1, 2), "red")
        point_2 = MyPoint((3, 4), "blue")
        point_3 = MyPoint((5, 6), "green")
        points.add_point(point_1)
        points.add_point(point_2)
        points.add_point(point_3)
        self.assertEqual(points.update_color((5,6),"red"),"Point (1,2) of color red, Point (3,4) of color blue, Point (5,6) of color red")

    def test_shift_x_axis(self):
        points = PointRepository()
        point_1 = MyPoint((1, 2), "red")
        point_2 = MyPoint((3, 4), "blue")
        point_3 = MyPoint((5, 6), "green")
        points.add_point(point_1)
        points.add_point(point_2)
        points.add_point(point_3)
        self.assertEqual(points.shift_x_axis(2),"Point (3,2) of color red, Point (5,4) of color blue, Point (7,6) of color green")

    def test_shift_y_axis(self):
        points = PointRepository()
        point_1 = MyPoint((1, 2), "red")
        point_2 = MyPoint((3, 4), "blue")
        point_3 = MyPoint((5, 6), "green")
        points.add_point(point_1)
        points.add_point(point_2)
        points.add_point(point_3)
        self.assertEqual(points.shift_y_axis(2),"Point (1,4) of color red, Point (3,6) of color blue, Point (5,8) of color green")

    def test_delete_coords(self):
        points = PointRepository()
        point_1 = MyPoint((1, 2), "red")
        point_2 = MyPoint((3, 4), "blue")
        point_3 = MyPoint((5, 6), "green")
        points.add_point(point_1)
        points.add_point(point_2)
        points.add_point(point_3)
        self.assertEqual(points.delete_coords((5,6)),"Point (1,2) of color red, Point (3,4) of color blue")

    def test_delete_points_circle(self):
        points = PointRepository()
        point_1 = MyPoint((1, 2), "red")
        point_2 = MyPoint((3, 4), "blue")
        point_3 = MyPoint((5, 7), "green")
        points.add_point(point_1)
        points.add_point(point_2)
        points.add_point(point_3)
        self.assertEqual(points.delete_points_circle((3, 4), 2), "Point (5,7) of color green")

    def test_delete_distance(self):
        points = PointRepository()
        point_1 = MyPoint((1, 2), "red")
        point_2 = MyPoint((3, 4), "blue")
        point_3 = MyPoint((5, 7), "green")
        points.add_point(point_1)
        points.add_point(point_2)
        points.add_point(point_3)
        self.assertEqual(points.delete_distance(point_2, 2), "Point (5,7) of color green")

if __name__ == '__main__':
    unittest.main()