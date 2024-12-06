from Assignment_3_Classes import *

def init_point_repository():
    point_repo = PointRepository()
    point_1 = MyPoint((1, 2), "red")
    point_2 = MyPoint((3, 4), "blue")
    point_3 = MyPoint((5, 6), "green")
    point_4 = MyPoint((7, 8), "yellow")
    point_5 = MyPoint((9, 10), "magenta")
    point_6 = MyPoint((-1, -2), "red")
    point_7 = MyPoint((-3, -4), "blue")
    point_8 = MyPoint((-5, -6), "green")
    point_9 = MyPoint((-7, -8), "yellow")
    point_10 = MyPoint((-9, -10), "magenta")
    point_repo.add_point(point_1)
    point_repo.add_point(point_2)
    point_repo.add_point(point_3)
    point_repo.add_point(point_4)
    point_repo.add_point(point_5)
    point_repo.add_point(point_6)
    point_repo.add_point(point_7)
    point_repo.add_point(point_8)
    point_repo.add_point(point_9)
    point_repo.add_point(point_10)
    return point_repo

def menu(points):
    print(
    """
Possible operations:
1. Initialize a point
2. Get the x coordinate of the point
3. Get the y coordinate of the point
4. Get the color of the point   
5. Set the x coordinate of the point
6. Set the y coordinate of the point
7. Set the color of the point
8. Update the point
9. Print the point
10. Add the point
11. Print all the points
12. Get a point by index
13. Get all the points of a color
14. Get the number of points of a color
15. Update the color of a point given its coordinates
16. Get all the points in a square
17. Get all points in a circle
18. Get all points in a rectangle
19. Get the minimum distance between 2 points
20. Get the maximum distance between 2 points
21. Update a point
22. Delete a point by index
23. Delete a point by coordinates
24. Delete all the points in a square
25. Delete all the points in a circle
26. Delete all the points within a certain distance from a given point
27. Shift points on x axis
28. Shift points on y axis
29. Plot the points
30. Stop (type "stop")
    """)
    while True:
        user_input = input("Enter your choice: ")
        if user_input == "stop":
            break
        elif user_input == "1":
            print("Enter the x coordinate of the point")
            x = int(input())
            print("Enter the y coordinate of the point")
            y = int(input())
            print("Enter the color of the point")
            color = input()
            coordinates = (x, y)
            point = MyPoint(coordinates,color)
            print(point.__str__())
        elif user_input == "2":
            print(f"The x coordinate of the point is {point.get_x()}")
        elif user_input == "3":
            print(f"The y coordinate of the point is {point.get_y()}")
        elif user_input == "4":
            print(f"The color of the point is {point.get_color()}")
        elif user_input == "5":
            print("Enter the new x coordinate of the point")
            x = int(input())
            point.set_x(x)
            print(point.__str__())
        elif user_input == "6":
            print("Enter the new y coordinate of the point")
            y = int(input())
            point.set_y(y)
            print(point.__str__())
        elif user_input == "7":
            print("Enter the new color of the point")
            color = input()
            point.set_color(color)
            print(point.__str__())
        elif user_input == "8":
            print("Enter the new x coordinate of the point")
            x = int(input())
            print("Enter the new y coordinate of the point")
            y = int(input())
            print("Enter the new color of the point")
            color = input()
            coordinates = (x, y)
            point.update(coordinates, color)
            print(point.__str__())
        elif user_input == "9":
            print(point.__str__())
        elif user_input == "10":
            points.add_point(point)
            print(points.__str__())
        elif user_input == "11":
            print(points.get_points())
        elif user_input == "12":
            print("Enter the index of the point")
            index = int(input())
            print(points.get_point(index))
        elif user_input == "13":
            print("Enter a color")
            color = input()
            print(points.get_points_color(color))
        elif user_input == "14":
            print("Enter a color")
            color = input()
            print(points.nr_points_color(color))
        elif user_input == "15":
            print("Enter the x coordinate of the point")
            x = int(input())
            print("Enter the y coordinate of the point")
            y = int(input())
            print("Enter the new color of the point")
            color = input()
            coordinates = (x, y)
            print(points.update_color(coordinates, color))
        elif user_input == "16":
            print("Enter the x coordinate of the upper left corner of the square")
            x = int(input())
            print("Enter the y coordinate of the upper left corner of the square")
            y = int(input())
            print("Enter the length of the square")
            length = int(input())
            print(points.get_points_square((x,y),length))
        elif user_input == "17":
            print("Enter the x coordinate of the center of the circle")
            x = int(input())
            print("Enter the y coordinate of the center of the circle")
            y = int(input())
            print("Enter the radius of the circle")
            radius = int(input())
            print(points.get_points_circle((x,y),radius))
        elif user_input == "18":
            print("Enter the x coordinate of the upper left corner of the rectangle")
            x = int(input())
            print("Enter the y coordinate of the upper left corner of the rectangle")
            y = int(input())
            print("Enter the length of the rectangle")
            length = int(input())
            print("Enter the width of the rectangle")
            width = int(input())
            print(points.get_points_rectangle((x,y),length,width))
        elif user_input == "19":
            print(points.get_min_distance())
        elif user_input == "20":
            print(points.get_max_distance())
        elif user_input == "21":
            print("Enter the index of the point")
            index = int(input())
            print("Enter the new x coordinate")
            x = int(input())
            print("Enter the new y coordinate")
            y = int(input())
            print("Enter the new color")
            color = input()
            coordinates = (x, y)
            points.update(index,coordinates, color)
            print(points.__str__())
        elif user_input == "22":
            print("Enter the index of the point")
            index = int(input())
            points.delete_point(index)
            print(points.__str__())
        elif user_input == "23":
            print("Enter the x coordinate of the point")
            x = int(input())
            print("Enter the y coordinate of the point")
            y = int(input())
            points.delete_coords((x,y))
            print(points.__str__())
        elif user_input == "24":
            print("Enter the x coordinate of the upper left corner of the square")
            x = int(input())
            print("Enter the y coordinate of the upper left corner of the square")
            y = int(input())
            print("Enter the length of the square")
            length = int(input())
            points.delete_points_square((x,y),length)
            print(points.__str__())
        elif user_input == "25":
            print("Enter the x coordinate of the center of the circle")
            x = int(input())
            print("Enter the y coordinate of the center of the circle")
            y = int(input())
            print("Enter the radius of the circle")
            radius = int(input())
            points.delete_points_circle((x, y), radius)
            print(points.__str__())
        elif user_input == "26":
            print("Enter the index of the point")
            index = int(input())
            print("Enter the distance from the point")
            distance = int(input())
            point = points.get_point_object(index)
            points.delete_distance(point, distance)
            print(points.__str__())
        elif user_input == "27":
            print("Enter distance to shift")
            distance = int(input())
            points.shift_x_axis(distance)
            print(points.__str__())
        elif user_input == "28":
            print("Enter distance to shift")
            distance = int(input())
            points.shift_y_axis(distance)
            print(points.__str__())
        elif user_input == "29":
            points.plot_points()
        else: print("Invalid input")


if __name__ == "__main__":
    point_repository = init_point_repository()
    menu(point_repository)
