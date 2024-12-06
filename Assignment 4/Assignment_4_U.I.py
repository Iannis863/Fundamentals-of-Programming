from Assignment_4_Classes import *

def init():
    vector_repository = VectorRepository()
    vector_1 = MyVector("Vector 1", "r", 1, [1,2,3])
    vector_2 = MyVector("Vector 2", "g", 2, [3,4,5])
    vector_3 = MyVector("Vector 3", "b", 3, [4,5,6])
    vector_4 = MyVector("Vector 4", "y", 1, [5,6,7])
    vector_5 = MyVector("Vector 5", "m", 2, [6,7,8])
    vector_6 = MyVector("Vector 6", "r", 3, [7,8,9])
    vector_7 = MyVector("Vector 7", "g", 1, [8,9,10])
    vector_8 = MyVector("Vector 8", "b", 2, [9,10,11])
    vector_9 = MyVector("Vector 9", "y", 3, [10,11,12])
    vector_10 = MyVector("Vector 10", "m", 4, [12,13,14])
    vector_repository.add_vector(vector_1)
    vector_repository.add_vector(vector_2)
    vector_repository.add_vector(vector_3)
    vector_repository.add_vector(vector_4)
    vector_repository.add_vector(vector_5)
    vector_repository.add_vector(vector_6)
    vector_repository.add_vector(vector_7)
    vector_repository.add_vector(vector_8)
    vector_repository.add_vector(vector_9)
    vector_repository.add_vector(vector_10)
    return vector_repository

def main(vector_repository):
    print("""
    1. Create a vector
    2. Print the vector
    3. Get the name or id of the vector
    4. Get the color of the vector
    5. Get the type of the vector
    6. Get the values of the vector
    7. Set the name or id of the vector
    8. Set the color of the vector
    9. Set the type of the vector
    10. Set the values of the vector
    11. Add a scalar to the vector
    12. Add a vector to the vector
    13. Subtract a vector from the vector
    14. Multiply a vector by another vector
    15. Get the sum of the values of the vector
    16. Get the product of the values of the vector
    17. Get the average of the values of the vector
    18. Get the minimum of the values of the vector
    19. Get the maximum of the values of the vector
    20. Add a vector
    21. Get all vectors
    22. Get a vector by index
    23. Update a vector by index
    24. Update a vector by name or id
    25. Delete a vector by index
    26. Delete a vector by name or id
    27. Delete all vectors
    28. Compute the sum of all the values of all a vectors of a certain color
    29. Update a color of a vector by name or id
    30. Plot the vectors
    31. Stop (type stop)
    """)
    while True:
        user_input = input("Enter a number: ")
        if user_input == "stop":
            break
        elif user_input == "1":
            name_id = input("Enter a name or id: ")
            color = input("Enter a color: ")
            type = int(input("Enter a type: "))
            values = []
            for i in range(3):
                values.append(int(input("Enter a value: ")))
            vector = MyVector(name_id, color, type, values)
            print(vector)
        elif user_input == "2":
            print(vector)
        elif user_input == "3":
            print("Name: " + vector.get_name_id())
        elif user_input == "4":
            print("Color: " + vector.get_color())
        elif user_input == "5":
            print("Type: " + str(vector.get_type()))
        elif user_input == "6":
            print("Values: " + str(vector.get_values()))
        elif user_input == "7":
            name_id = input("Enter a name or id: ")
            vector.set_name_id(name_id)
            print(vector)
        elif user_input == "8":
            color = input("Enter a color: ")
            vector.set_color(color)
            print(vector)
        elif user_input == "9":
            type = int(input("Enter a type: "))
            vector.set_type(type)
            print(vector)
        elif user_input == "10":
            values = []
            for i in range(3):
                values.append(int(input("Enter a value: ")))
            vector.set_values(values)
            print(vector)
        elif user_input == "11":
            scalar = int(input("Enter a scalar: "))
            vector.add_scalar(scalar)
            print(vector)
        elif user_input == "12":
            values = []
            for i in range(3):
                values.append(int(input("Enter a value: ")))
            vector.add_vector(values)
            print(vector)
        elif user_input == "13":
            values = []
            for i in range(3):
                values.append(int(input("Enter a value: ")))
            vector.subtract_vector(values)
            print(vector)
        elif user_input == "14":
            values = []
            for i in range(3):
                values.append(int(input("Enter a value: ")))
            print(vector.multiplication(values))
        elif user_input == "15":
            print(vector.sum_vector())
        elif user_input == "16":
            print(vector.product_vector())
        elif user_input == "17":
            print(vector.avg_vector())
        elif user_input == "18":
            print(vector.min_vector())
        elif user_input == "19":
            print(vector.max_vector())
        elif user_input == "20":
            vector_repository.add_vector(vector)
        elif user_input == "21":
            for vector in vector_repository.get_vectors():
                print(vector)
        elif user_input == "22":
            index = int(input("Enter the index: "))
            print(vector_repository.get_vector(index))
        elif user_input == "23":
            index = int(input("Enter the index: "))
            name_id = input("Enter a name or id: ")
            color = input("Enter a color: ")
            type = int(input("Enter a type: "))
            values = []
            for i in range(3):
                values.append(int(input("Enter a value: ")))
            vector_repository.update_vector_index(index, name_id, color, type, values)
        elif user_input == "24":
            name_id = input("Enter a name or id: ")
            new_name_id = input("Enter a name or id: ")
            color = input("Enter a color: ")
            type = int(input("Enter a type: "))
            values = []
            for i in range(3):
                values.append(int(input("Enter a value: ")))
            vector_repository.update_vector_name_id(name_id, new_name_id, color, type, values)
        elif user_input == "25":
            index = int(input("Enter the index: "))
            vector_repository.delete_vector_index(index)
        elif user_input == "26":
            name_id = input("Enter a name or id: ")
            vector_repository.delete_vector_name_id(name_id)
        elif user_input == "27":
            vector_repository.delete_all_vectors()
        elif user_input == "28":
            color = input("Enter a color: ")
            print(vector_repository.sum_vectors_color(color))
        elif user_input == "29":
            name_id = input("Enter a name or id: ")
            color = input("Enter a color: ")
            vector_repository.update_color_name_id(name_id, color)
        elif user_input == "30":
            vector_repository.plot()
        else:
            print("Invalid input")

if __name__ == "__main__":
    main(init())