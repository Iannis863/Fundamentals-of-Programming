import math
import numpy as np
import matplotlib.pyplot as plt


class MyPoint:
    def __init__(self,coordinates:tuple[int,int],color:str):
        """
        Initialize a point
        :param coordinates: A tuple of 2 integers indicating the x and y coordinates of the point
        :param color: The color of the point
        :raises: TypeError, ValueError
        """
        if not isinstance(coordinates, tuple) or not isinstance(coordinates[0], int) or not isinstance(coordinates[1],int) or len(coordinates) != 2:
            raise TypeError("The coordinates must be a tuple of 2 integers")
        if not isinstance(color,str):
            raise TypeError("The color must be a string")
        if color not in ['red','green','blue','yellow','magenta']:
            raise ValueError("The color should be red, green, blue, yellow or magenta")
        self.position = coordinates
        self.color = color

    def get_x(self):
        """
        Returns the x coordinate of the point
        :return: The x coordinate of the point
        """
        return self.position[0]

    def get_y(self):
        """
        Returns the y coordinate of the point
        :return: Returns the y coordinate of the point
        """
        return self.position[1]

    def get_color(self):
        """
        Returns the color value of the point
        :return: Returns the color value of the point
        """
        return self.color

    def set_x(self,coord_x:int):
        """
        Sets the x coordinate of the point
        :param coord_x: The x coordinate of the point
        :raises: TypeError
        """
        if not isinstance(coord_x,int):
            raise TypeError("The coordinates must be integers")
        self.position = (coord_x,self.position[1])

    def set_y(self,coord_y:int):
        """
        Sets the y coordinate of the point
        :param coord_y: The y coordinate of the point
        :raises: TypeError
        """
        if not isinstance(coord_y,int):
            raise TypeError("The coordinates must be integers")
        self.position = (self.position[0],coord_y)

    def set_color(self,color:str):
        """
        Sets the color value of the point
        :param color: The color value of the point
        :raises: TypeError, ValueError
        """
        if not isinstance(color,str):
            raise TypeError("The color must be a string")
        if color not in ['red','green','blue','yellow','magenta']:
            raise ValueError("The color should be red, green, blue, yellow or magenta")
        self.color = color

    def update(self,coordinates:tuple[int,int],color:str):
        """
        Updates the point with the new coordinates and the new color
        :param coordinates: The new coordinates of the point
        :param color: The new color of the point
        :return: The updated point
        :raises: TypeError, ValueError
        """
        if not isinstance(coordinates,tuple) or not isinstance(coordinates[0],int) or not isinstance(coordinates[1],int) or len(coordinates) != 2:
            raise TypeError("The coordinates must be a tuple of 2 integers")
        if not isinstance(color,str):
            raise TypeError("The color must be a string")
        if color not in ['red', 'green', 'blue', 'yellow', 'magenta']:
            raise ValueError("The color should be red, green, blue, yellow or magenta")
        self.position = coordinates
        self.color = color
        return self

    def __str__(self):
        """
        Return a string representation of the point
        :return: The string representation of the point
        """
        return f"Point ({self.get_x()},{self.get_y()}) of color {self.get_color()}"


class PointRepository:
    def __init__(self):
        self.points = []

    def add_point(self,point:MyPoint):
        """
        Add a point to the repository
        :param point: The point to add
        :return: The string representation of the repository
        :raises: TypeError
        """
        if not isinstance(point,MyPoint):
            raise TypeError
        self.points.append(point)
        return self.__str__()

    def get_points(self):
        """
        Get all the points in the repository
        :return: The string representation of the repository
        """
        return self.__str__()

    def get_point(self,index:int):
        """
        Get a specific point in the repository
        :param index: The index of the point
        :return: The string representation of the point
        """
        if not isinstance(index,int):
            raise TypeError("The index must be an integer")
        return self.points[index].__str__()

    def get_points_color(self,color:str):
        """
        Get all the points of a color in the repository
        :param color: The color of the points
        :return: The string representation of all the points of the color
        :raises: TypeError, ValueError
        """
        if not isinstance(color,str):
            raise TypeError("The color must be a string")
        if color not in ['red','green','blue','yellow','magenta']:
            raise ValueError("The color should be red, green, blue, yellow or magenta")
        string = ""
        for point in self.points:
            if point.get_color() == color:
                if string == "":
                    string += point.__str__()
                else:
                    string += ", " + point.__str__()
        return string

    def get_points_square(self,coordinates:tuple[int,int],length:int):
        """
        Get all the points of a square in the repository
        :param coordinates: The coordinates of the up-left corner of the square
        :param length: The length of the square
        :return: The string representation of all the points of the square
        :raises: TypeError, ValueError
        """
        if not isinstance(coordinates,tuple) or not isinstance(coordinates[0],int) or not isinstance(coordinates[1],int) or len(coordinates) != 2:
            raise TypeError("The coordinates of the up-left corner must be tuple of 2 integers")
        if not isinstance(length,int):
            raise TypeError("The length of the square must be an integer")
        if length < 0:
            raise ValueError("The length of the square must be positive")
        string = ""
        for point in self.points:
            if coordinates[0] <= point.get_x() <= coordinates[0] + length and coordinates[1] >= point.get_y() >= coordinates[1] - length:
                if string == "":
                    string += point.__str__()
                else:
                    string += ", " + point.__str__()
        return string

    def distance(self,index_1:int,index_2:int):
        """
        Get the distance between two points
        :param index_1: The index of the first point
        :param index_2: The index of the second point
        :return: The distance between the two points
        :raises: TypeError
        """
        if not isinstance(index_1,int) or not isinstance(index_2,int):
            raise TypeError
        point_1 = self.points[index_1]
        point_2 = self.points[index_2]
        return math.sqrt((point_2.get_x() - point_1.get_x()) **2 + (point_2.get_y() - point_1.get_y()) **2)

    def get_min_distance(self):
        """
        Get the minimum distance between all the points in the repository
        :return: The minimum distance between all the points in the repository
        """
        minimum = 99999
        for index_1 in range(len(self.points)):
            for index_2 in range(index_1 + 1,len(self.points)):
                if self.distance(index_1,index_2) < minimum:
                    minimum = self.distance(index_1,index_2)
        return minimum

    def update(self,index:int,coordinates:tuple[int,int],color:str):
        """
        Update a point in the repository
        :param index: The index of the point
        :param coordinates: The new coordinates of the point
        :param color: The new color of the point
        :return: The string representation of all the points in the repository
        :raises TypeError
        """
        if not isinstance(coordinates,tuple) or not isinstance(coordinates[0],int) or not isinstance(coordinates[1],int) or len(coordinates) != 2:
            raise TypeError("The coordinates must be tuple of 2 integers")
        if not isinstance(color,str):
            raise TypeError("The color must be a string")
        self.points[index].update(coordinates,color)
        return self.__str__()

    def delete_point(self,index:int):
        """
        Delete a point in the repository
        :param index: The index of the point
        :return: The string representation of all the points in the repository
        :raises: TypeError, ValueError
        """
        if not isinstance(index,int):
            raise TypeError("The index must be an integer")
        if index not in range(len(self.points)):
            raise ValueError("The index must be valid")
        self.points.pop(index)
        return self.__str__()

    def delete_points_square(self,coordinates:tuple[int,int],length:int):
        """
        Delete all the points in a square
        :param coordinates: The coordinates of the up-left corner of the square
        :param length: The length of the square
        :return: The string representation of all the points in the repository
        :raises: TypeError, ValueError
        """
        if not isinstance(coordinates,tuple) or not isinstance(coordinates[0],int) or not isinstance(coordinates[1],int) or len(coordinates) != 2:
            raise TypeError("The coordinates of the up-left corner must be tuple of 2 integers")
        if not isinstance(length,int):
            raise TypeError("The length of the square must be an integer")
        if length < 0:
            raise ValueError("The length of the square must be positive")
        self.points = [point for point in self.points if not (coordinates[0] <= point.get_x() <= coordinates[0] + length and coordinates[1] >= point.get_y() >= coordinates[1] - length)]
        return self.__str__()

    def get_positions_colors(self):
        """
        Get all positions and colors
        :return: The positions and colors
        """
        position_x = np.array([point.get_x() for point in self.points])
        position_y = np.array([point.get_y() for point in self.points])
        colors = np.array([point.get_color() for point in self.points])
        return position_x, position_y, colors

    def get_points_circle(self, coordinates:tuple[int,int], radius:int):
        """
        Get all the points of a circle
        :param coordinates: The coordinates of the center of the circle
        :param radius: The radius of the circle
        :return: The string representation of all the points of the circle
        :raises: TypeError, ValueError
        """
        string = ""
        if not isinstance(coordinates,tuple) or not isinstance(coordinates[0],int) or not isinstance(coordinates[1],int):
            raise TypeError("The coordinates must be tuple of 2 integers")
        if not isinstance(radius,int):
            raise TypeError("The radius of the circle must be an integer")
        if radius < 0:
            raise ValueError("The radius of the circle must be positive")
        for index, point in enumerate(self.points):
            if (point.get_x() - coordinates[0]) ** 2 <= radius ** 2 and (point.get_y() - coordinates[1]) ** 2 <= radius ** 2:
                if string == "":
                    string += point.__str__()
                else:
                    string += ", " + point.__str__()
        return string

    def get_points_rectangle(self, coordinates:tuple[int,int], length:int, width:int):
        """
        Get all the points in a rectangle
        :param coordinates: The coordinates of the up-left corner of the rectangle
        :param length: The length of the rectangle
        :param width: The width of the rectangle
        :return: The string representation of all the points in the rectangle
        :raises TypeError, ValueError
        """
        if not isinstance(coordinates,tuple) or not isinstance(coordinates[0],int) or not isinstance(coordinates[1],int):
            raise TypeError("The coordinates must be tuple of 2 integers")
        if not isinstance(length,int) or not isinstance(width,int):
            raise TypeError("The length of the rectangle must be an integer")
        if length < 0 or width < 0:
            raise ValueError("The length of the rectangle must be positive")
        string = ""
        for index, point in enumerate(self.points):
            if coordinates[0] <= point.get_x() <= coordinates[0] + length and coordinates[1] >= point.get_y() >= coordinates[1] - width:
                if string == "":
                    string += point.__str__()
                else:
                    string += ", " + point.__str__()
        return string

    def get_max_distance(self):
        """
        Get the maximum distance between all the points in the repository
        :return: The maximum distance between all the points in the repository
        """
        maximum = 0
        for index_1 in range(len(self.points)):
            for index_2 in range(index_1 + 1, len(self.points)):
                if self.distance(index_1, index_2) > maximum:
                    maximum = self.distance(index_1, index_2)
        return maximum

    def nr_points_color(self, color:str):
        """
        Get the number of points of a certain color
        :param color: The color of the points to be counted
        :return: The number of points of a certain color
        :raises TypeError, ValueError
        """
        if not isinstance(color,str):
            raise TypeError("The color must be a string")
        if color not in ['red', 'green', 'blue', 'yellow', 'magenta']:
            raise ValueError("The color should be red, green, blue, yellow or magenta")
        counter = 0
        for point in self.points:
            if point.get_color() == color:
                counter += 1
        return counter

    def update_color(self, coordinates:tuple[int,int], color:str):
        """
        Update the color of a point given its coordinates
        :param coordinates: The coordinates of the point
        :param color: The new color of the point
        :return: The string representation of the points in the repository
        :raises TypeError, ValueError
        """
        if not isinstance(coordinates,tuple) or not isinstance(coordinates[0],int) or not isinstance(coordinates[1],int):
            raise TypeError("The coordinates must be tuple of 2 integers")
        for point in self.points:
            if point.get_x() == coordinates[0] and point.get_y() == coordinates[1]:
                point.set_color(color)
        return self.__str__()

    def shift_x_axis(self, distance:int):
        """
        Shift all the points on the x axis
        :param distance: The distance to shift the points
        :return: The string representation of the points in the repository
        :raises TypeError
        """
        if not isinstance(distance,int):
            raise TypeError("The distance must be an integer")
        for point in self.points:
            point.set_x(point.get_x() + distance)
        return self.__str__()

    def shift_y_axis(self, distance: int):
        """
        Shift all the points on the y axis
        :param distance: The distance to shift the points
        :return: The string representation of the points in the repository
        :raises TypeError
        """
        if not isinstance(distance,int):
            raise TypeError("The distance must be an integer")
        for point in self.points:
            point.set_y(point.get_y() + distance)
        return self.__str__()

    def delete_coords(self, coordinates:tuple[int,int]):
        """
        Delete a point by coordinates
        :param coordinates: The coordinates of the point
        :return: The string representation of the points in the repository
        :raises TypeError
        """
        if not isinstance(coordinates,tuple) or not isinstance(coordinates[0],int) or not isinstance(coordinates[1],int):
            raise TypeError("The coordinates must be tuple of 2 integers")
        for point in self.points:
            if point.get_x() == coordinates[0] and point.get_y() == coordinates[1]:
                self.points.remove(point)
        return self.__str__()

    def delete_points_circle(self, coordinates: tuple[int, int], radius: int):
        """
        Delete all the points of a circle
        :param coordinates: The coordinates of the center of the circle
        :param radius: The radius of the circle
        :return: The string representation of all the points in the repository
        :raises: TypeError, ValueError
        """
        if not isinstance(coordinates, tuple) or not isinstance(coordinates[0], int) or not isinstance(coordinates[1], int):
            raise TypeError("The coordinates must be tuple of 2 integers")
        if not isinstance(radius, int):
            raise TypeError("The radius of the circle must be an integer")
        if radius < 0:
            raise ValueError("The radius of the circle must be positive")
        self.points = [point for point in self.points if not ((point.get_x() - coordinates[0]) ** 2 <= radius ** 2 and (point.get_y() - coordinates[1]) ** 2 <= radius ** 2)]
        return self.__str__()

    def get_point_object(self, index:int):
        """
        Get the point as an object
        :param index: The index of the point
        :return: The requested point object
        :raises TypeError
        """
        if not isinstance(index,int):
            raise TypeError("The index must be an integer")
        return self.points[index]

    def delete_distance(self,point:MyPoint,distance:int):
        """
        Delete all points within a certain distance of a point
        :param point: The point
        :param distance: The distance
        :return: The string representation of the repository
        :raises TypeError, ValueError
        """
        if not isinstance(point,MyPoint):
            raise TypeError("The point must be an instance of MyPoint")
        if not isinstance(distance,int):
            raise TypeError("The distance must be an integer")
        if distance < 0:
            raise ValueError("The distance must be positive")
        self.delete_points_circle((point.get_x(),point.get_y()),distance)
        return self.__str__()

    def plot_points(self):
        """
        Plot all the points in the repository
        """
        position_x, position_y, colors = self.get_positions_colors()
        plt.scatter(position_x, position_y, c=colors,  alpha=0.6)
        plt.show()

    def __str__(self):
        """
        Return a string representation of the repository
        :return: The string representation of the repository
        """
        string = ""
        for point in self.points:
            if string == "":
                string += point.__str__()
            else:
                string += ", " + point.__str__()
        return string