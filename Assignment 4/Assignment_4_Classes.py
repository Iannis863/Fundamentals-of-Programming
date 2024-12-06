import numpy as np
import matplotlib.pyplot as plt

class MyVector:
    def __init__(self, name_id:str, color:str, type:int, values:list):
        """
        Initializes a new instance of the Vector class.
        :param name_id: The name or id of the vector.
        :param color: The color of the vector.
        :param type: The type of vector.
        :param values: The values of the vector.
        :raises: TypeError, ValueError
        """
        if not isinstance(name_id, str):
            raise TypeError("Name id must be of type str.")
        if not isinstance(color, str):
            raise TypeError("Color must be of type str.")
        if not isinstance(type, int):
            raise TypeError("Type must be of type int.")
        if not isinstance(values, list):
            raise TypeError("Values must be of type list of integers.")
        if color not in ["r", "g", "b", "y", "m"]:
            raise ValueError("Color must be 'r', 'g', 'b', 'y' or 'm'.")
        if type < 1:
            raise ValueError("Type must be greater or equal than 1.")
        self.name_id = name_id
        self.color = color
        self.type = type
        self.values = np.array(values)

    def __str__(self):
        """
        Create a string representation of the vector.
        :return: The string representation of the vector.
        """
        return str(self.name_id) + ": color - " + self.color + ", type - " + str(self.type) + ": " + str(self.values)

    def get_name_id(self):
        """
        Get the name or id of the vector.
        :return: The name or id of the vector.
        """
        return self.name_id

    def get_color(self):
        """
        Get the color of the vector.
        :return: The color of the vector.
        """
        return self.color

    def get_type(self):
        """
        Get the type of the vector.
        :return: The type of the vector.
        """
        return self.type

    def get_values(self):
        """
        Get the values of the vector.
        :return: The values of the vector.
        """
        return self.values

    def set_name_id(self, name_id:str):
        """
        Sets the name or id of the vector.
        :param name_id: The name or id of the vector.
        :return: The vector.
        :raises: TypeError
        """
        if not isinstance(name_id, str):
            raise TypeError("Name id must be of type str.")
        self.name_id = name_id
        return self

    def set_color(self, color:str):
        """
        Sets the color of the vector.
        :param color: The color of the vector.
        :return: The vector.
        :raises: TypeError, ValueError
        """
        if not isinstance(color, str):
            raise TypeError("Color must be of type str.")
        if color not in ["r", "g", "b", "y", "m"]:
            raise ValueError("Color must be 'r', 'g', 'b', 'y' or 'm'.")
        self.color = color
        return self

    def set_type(self, type:int):
        """
        Sets the type of the vector.
        :param type: The type of the vector.
        :return: The vector.
        :raises: TypeError, ValueError
        """
        if not isinstance(type, int):
            raise TypeError("Type must be of type int.")
        if type < 1:
            raise ValueError("Type must be greater or equal than 1.")
        self.type = type
        return self

    def set_values(self, values:list):
        """
        Sets the values of the vector.
        :param values: The values of the vector.
        :return: The vector.
        :raises: TypeError
        """
        if not isinstance(values, list):
            raise TypeError("Values must be of type list of integers.")
        self.values = np.array(values)
        return self

    def add_scalar(self, scalar:int):
        """
        Adds a scalar to the vector.
        :param scalar: The scalar to add.
        :return: The vector with the scalar added.
        :raises: TypeError
        """
        if not isinstance(scalar, int):
            raise TypeError("Scalar must be of type int.")
        self.values = self.values + scalar
        return self

    def add_vector(self, values:list):
        """
        Add two vectors
        :param values: The values to add.
        :return: The vector with the added values.
        :raises: TypeError
        """
        if not isinstance(values, list):
            raise TypeError("Values must be of type list of integers.")
        self.values = self.values + np.array(values)
        return self

    def subtract_vector(self, values:list):
        """
        Subtract two vectors
        :param values: The values to subtract.
        :return: The vector with the subtracted values.
        :raises: TypeError
        """
        if not isinstance(values, list):
            raise TypeError("Values must be of type list of integers.")
        self.values = self.values - np.array(values)
        return self

    def multiplication(self, values:list):
        """
        Multiplication of two vectors
        :param values: The values to multiply.
        :return: The result of the multiplication.
        :raises: TypeError
        """
        if not isinstance(values, list):
            raise TypeError("Values must be of type list of integers.")
        return self.values.dot(np.array(values))

    def sum_vector(self):
        """
        Computes the sum of the values of the vector.
        :return: The sum of the values of the vector.
        """
        return np.sum(self.values)

    def product_vector(self):
        """
        Computes the product of the values of the vector.
        :return: The product of the values of the vector.
        """
        return np.prod(self.values)

    def avg_vector(self):
        """
        Computes the average of the values of the vector.
        :return: The average of the values of the vector.
        """
        return np.average(self.values)

    def min_vector(self):
        """
        Compute the minimum value of a vector
        :return: The minimum value of a vector
        """
        return np.min(self.values)

    def max_vector(self):
        """
        Compute the maximum value of a vector
        :return: The maximum value of a vector
        """
        return np.max(self.values)


class VectorRepository:
    def __init__(self):
        """
        Initializes the repository.
        """
        self.vectors = []

    def add_vector(self, vector:MyVector):
        """
        Add a vector to the repository.
        :param vector: The vector to add.
        :return: The repository with the added vector.
        :raises: TypeError
        """
        if not isinstance(vector, MyVector):
            raise TypeError("Vector must be of type MyVector.")
        self.vectors.append(vector)
        return self

    def get_vectors(self):
        """
        Get the vectors of the repository.
        :return: The vectors of the repository.
        """
        return self.vectors

    def get_vector(self, index:int):
        """
        Get a vector from the repository of a specific index.
        :param index: The index of the vector.
        :return: The vector of the specified index.
        :raises: TypeError, IndexError
        """
        if not isinstance(index, int):
            raise TypeError("Index must be of type int.")
        if index < 0 or index >= len(self.vectors):
            raise IndexError("Index out of range.")
        return self.vectors[index]

    def update_vector_index(self, index:int, name_id:str, color:str, type:int, values:list):
        """
        Update a vector by index
        :param index: The index
        :param name_id: The name of the vector
        :param color: The color of the vector
        :param type: The type of the vector
        :param values: The values of the vector
        :return: The updated repository
        :raises TypeError, IndexError, ValueError
        """
        if not isinstance(index, int):
            raise TypeError("Index must be of type int.")
        if index < 0 or index >= len(self.vectors):
            raise IndexError("Index out of range.")
        if not isinstance(name_id, str):
            raise TypeError("Name id must be of type str.")
        if not isinstance(color, str):
            raise TypeError("Color must be of type str.")
        if not isinstance(type, int):
            raise TypeError("Type must be of type int.")
        if not isinstance(values, list):
            raise TypeError("Values must be of type list of integers.")
        if color not in ["r","g","b","y","m"]:
            raise ValueError("Color must be 'r','g','b','y','m'.")
        if type < 1:
            raise ValueError("Type must be greater or equal than 1.")
        self.vectors[index].set_name_id(name_id)
        self.vectors[index].set_color(color)
        self.vectors[index].set_type(type)
        self.vectors[index].set_values(values)
        return self

    def update_vector_name_id(self, name_id:str, new_name_id:str, color:str, type:int, values:list):
        """
        Update a vector by name_id
        :param name_id: The name of the vector
        :param new_name_id: The new name of the vector
        :param color: The color of the vector
        :param type: The type of the vector
        :param values: The values of the vector
        :return: The updated repository
        :raises TypeError, ValueError
        """
        if not isinstance(name_id, str):
            raise TypeError("Name id must be of type str.")
        if not isinstance(new_name_id, str):
            raise TypeError("Name id must be of type str.")
        if not isinstance(color, str):
            raise TypeError("Color must be of type str.")
        if not isinstance(type, int):
            raise TypeError("Type must be of type int.")
        if not isinstance(values, list):
            raise TypeError("Values must be of type list of integers.")
        if color not in ["r","g","b","y","m"]:
            raise ValueError("Color must be 'r','g','b','y','m'.")
        if type < 1:
            raise ValueError("Type must be greater or equal than 1.")
        for vector in self.vectors:
            if vector.name_id == name_id:
                vector.set_name_id(new_name_id)
                vector.set_color(color)
                vector.set_type(type)
                vector.set_values(values)
        return self

    def delete_vector_index(self, index:int):
        """
        Delete a vector by index
        :param index: The index of the vector
        :return: The updated vector repository
        :raises TypeError, IndexError
        """
        if not isinstance(index, int):
            raise TypeError("Index must be of type int.")
        self.vectors.pop(index)
        return self

    def delete_vector_name_id(self, name_id:str):
        """
        Delete a vector by name_id
        :param name_id: The name or id of the vector
        :return: The updated vector repository
        :raises TypeError
        """
        if not isinstance(name_id, str):
            raise TypeError("Name or id must be of type str.")
        for vector in self.vectors:
            if vector.name_id == name_id:
                self.vectors.remove(vector)
        return self

    def plot(self):
        """
        Plot all vectors based on type and color.
        1 - circle
        2 - square
        3 - triangle
        > 3 - diamond
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        shapes = {1: "o", 2: "s", 3: "^"}
        for vector in self.vectors:
            marker = shapes.get(vector.get_type(), "D")
            ax.scatter(vector.get_values()[0], vector.get_values()[1], vector.get_values()[2], color=vector.get_color(), marker = marker)
        plt.show()

    def sum_vectors_color(self, color:str):
        """
        Get the vectors that have a minimum less than a value
        :param color: The color
        :return: The sum of elements of the vectors
        :raises: TypeError, ValueError
        """
        if not isinstance(color,str):
            raise TypeError("Color must be a string")
        if color not in ["r", "b", "g", "y", "m"]:
            raise ValueError("Color must be r, b, g, y or m")
        s = 0
        for vector in self.vectors:
            if vector.get_color() == color:
                for value in vector.get_values():
                    s += value
        return s

    def delete_all_vectors(self):
        """
        Delete all vectors
        """
        for vector in reversed(self.vectors):
            self.delete_vector_name_id(vector.get_name_id())

    def update_color_name_id(self, name_id:str, color:str):
        """
        Update a color by name or id
        :param name_id: The name or id
        :param color: The new color
        :raises: TypeError, ValueError
        """
        if not isinstance(name_id, str):
            raise TypeError("Name or id must be a string")
        if not isinstance(color, str):
            raise TypeError("Color must be a string")
        if color not in ["r", "b", "g", "y", "m"]:
            raise ValueError("Color must be r, b, g, y or m")
        for vector in self.vectors:
            if vector.get_name_id() == name_id:
                vector.set_color(color)
        return self.vectors