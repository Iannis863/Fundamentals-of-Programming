from Passenger import Passenger
from Plane import Plane
from Airport import Airport

def set_Up():
    passenger1 = Passenger(123456789, "John", "Doe")
    passenger2 = Passenger(987654321, "Jane", "Smith")
    passenger3 = Passenger(123, "John", "Smith")
    passenger4 = Passenger(456, "Jane", "Doe")
    passenger5 = Passenger(789, "Alex", "Pop")
    passenger6 = Passenger(125, "Iannis", "Alb")
    passenger7 = Passenger(126, "Felix", "Crisan")
    passenger8 = Passenger(127, "Alex", "Crisan")
    passenger9 = Passenger(128, "Vlad", "Potra")
    plane1 = Plane("A123", "Delta", 100, "New York")
    plane2 = Plane("B456", "American Airlines", 200, "Los Angeles")
    plane3 = Plane("C789", "United Airlines", 300, "Chicago")
    plane1.add_passenger(passenger1)
    plane1.add_passenger(passenger2)
    plane1.add_passenger(passenger3)
    plane2.add_passenger(passenger4)
    plane2.add_passenger(passenger5)
    plane2.add_passenger(passenger6)
    plane3.add_passenger(passenger7)
    plane3.add_passenger(passenger8)
    plane3.add_passenger(passenger9)
    airport = Airport()
    airport.add_plane(plane1)
    airport.add_plane(plane2)
    airport.add_plane(plane3)
    return airport

def read_passenger_info():
    try:
        passport_number = int(input("Enter the passenger's passport number: "))
    except ValueError:
        print("Passport number must be an integer.")
        return
    first_name = input("Enter the passenger's first name: ")
    last_name = input("Enter the passenger's last name: ")
    return Passenger(passport_number, first_name, last_name)

def read_plane_info():
    name_or_number = input("Enter the plane's name or number: ")
    airline = input("Enter the plane's airline: ")
    try:
        capacity = int(input("Enter the plane's capacity: "))
    except ValueError:
        print("Capacity must be an integer.")
        return
    destination = input("Enter the plane's destination: ")
    return Plane(name_or_number, airline, capacity, destination)

def main(airport):
    print("""
Welcome to the Airport Management System
Please select an option from the menu below:
1. Create a new passenger
2. Get the current passenger's passport number
3. Get the current passenger's first name
4. Get the current passenger's last name
5. Set the current passenger's passport number
6. Set the current passenger's first name
7. Set the current passenger's last name 
8. Print the current passenger's information
9. Create a new plane
10. Add the current passenger to the current plane
11. Get the current plane's name or number 
12. Get the current plane's airline
13. Get the current plane's capacity
14. Get the current plane's destination
15. Get a plane's passengers # ask for plane
16. Set the current plane's name or number 
17. Set the current plane's airline
18. Set the current plane's capacity
19. Set the current plane's destination
20. Create and add a new passenger to a plane # ask for a plane
21. Remove a passenger from a plane # ask for a plane
22. Update a passenger's information # breaks when trying to update a passenger that does not exist
23. Print a planes information # Ask for a plane name or number
24. Add the current plane to the airport
25. Create and add a new plane to the airport
26. Get the airport's planes
27. Update a plane's information # ask for a plane
27. Sort the passengers of a plane by last name
28. Sort the airport's planes by capacity # Not working
29. Sort the planes by the number of passengers starting with a given string
30. Sort the planes by the number of passengers concatenated with the plane's destination
31. Search for planes with passengers whose passport numbers start with the same three digits.
32. Search for passengers on a specific plane whose first or last name contains a given string.
33. Search for a passenger by first and last name across all planes at the airport.
34. Stop the program (type 'exit')
""")
    while True:
        user_input = (input("Enter the number of the option you would like to select: "))
        if user_input.isnumeric():
            user_input = int(user_input)
        match user_input:
            case 1:
                print("You have selected to create a new passenger.")
                passenger = read_passenger_info()
            case 2:
                print("You have selected to get the current passenger's passport number.")
                try:
                    print(passenger.get_passport_number())
                except AttributeError:
                    print("There is no current passenger.")
            case 3:
                print("You have selected to get the current passenger's first name.")
                try:
                    print(passenger.get_first_name())
                except AttributeError:
                    print("There is no current passenger.")
            case 4:
                print("You have selected to get the current passenger's last name.")
                try:
                    print(passenger.get_last_name())
                except AttributeError:
                    print("There is no current passenger.")
            case 5:
                print("You have selected to set the current passenger's passport number.")
                try:
                    passport_number = int(input("Enter the passenger's new passport number: "))
                    passenger.set_passport_number(passport_number)
                except ValueError:
                    print("Passport number must be an integer.")
                except AttributeError:
                    print("There is no current passenger.")
            case 6:
                print("You have selected to set the current passenger's first name.")
                first_name = input("Enter the passenger's new first name: ")
                try:
                    passenger.set_first_name(first_name)
                except AttributeError:
                    print("There is no current passenger.")
            case 7:
                print("You have selected to set the current passenger's last name.")
                last_name = input("Enter the passenger's new last name: ")
                try:
                    passenger.set_last_name(last_name)
                except AttributeError:
                    print("There is no current passenger.")
            case 8:
                print("You have selected to print the current passenger's information.")
                try:
                    print(passenger)
                except AttributeError:
                    print("There is no current passenger.")
            case 9:
                print("You have selected to create a new plane.")
                plane = read_plane_info()
            case 10:
                print("You have selected to add the current passenger to the current plane.")
                try:
                    plane.add_passenger(passenger)
                except AttributeError:
                    print("There is no current passenger or current plane.")
            case 11:
                print("You have selected to get the current plane's name or number.")
                try:
                    print(plane.get_name_or_number())
                except AttributeError:
                    print("There is no current plane.")
            case 12:
                print("You have selected to get the current plane's airline.")
                try:
                    print(plane.get_airline_company())
                except AttributeError:
                    print("There is no current plane.")
            case 13:
                print("You have selected to get the current plane's capacity.")
                try:
                    print(plane.get_number_of_seats())
                except AttributeError:
                    print("There is no current plane.")
            case 14:
                print("You have selected to get the current plane's destination.")
                try:
                    print(plane.get_destination())
                except AttributeError:
                    print("There is no current plane.")
            case 15:
                print("You have selected to get a plane's passengers.")
                try:
                    for passenger in plane.get_passengers():
                        print(passenger)
                except AttributeError:
                    print("There is no current plane.")
            case 16:
                print("You have selected to set the current plane's name or number.")
                name_or_number = input("Enter the plane's new name or number: ")
                try:
                    plane.set_name_or_number(name_or_number)
                except AttributeError:
                    print("There is no current plane.")
            case 17:
                print("You have selected to set the current plane's airline.")
                airline = input("Enter the plane's new airline: ")
                try:
                    plane.set_airline_company(airline)
                except AttributeError:
                    print("There is no current plane.")
            case 18:
                print("You have selected to set the current plane's capacity.")
                try:
                    capacity = int(input("Enter the plane's new capacity: "))
                    plane.set_number_of_seats(capacity)
                except ValueError:
                    print("Capacity must be an integer.")
                except AttributeError:
                    print("There is no current plane.")
            case 19:
                print("You have selected to set the current plane's destination.")
                destination = input("Enter the plane's new destination: ")
                try:
                    plane.set_destination(destination)
                except AttributeError:
                    print("There is no current plane.")
            case 20:
                print("You have selected to create and add a new passenger to a plane.")
                passenger = read_passenger_info()
                if passenger is not None:
                    try:
                        plane.add_passenger(passenger)
                    except AttributeError:
                        print("There is no current plane.")
            case 21:
                print("You have selected to remove a passenger from the plane.")
                try:
                    passport_number = int(input("Enter the passenger's passport number: "))
                    plane.remove_passenger(passport_number)
                except ValueError:
                    print("Passport number must be an integer.")
                except AttributeError:
                    print("There is no current plane.")
            case 22:
                print("You have selected to update a passenger's information.")
                try:
                    passport_number = int(input("Enter the passenger's passport number: "))
                    first_name = input("Enter the passenger's new first name: ")
                    last_name = input("Enter the passenger's new last name: ")
                    plane.update_passenger(passport_number, first_name, last_name)
                except ValueError:
                    print("Passport number must be an integer.")
                except AttributeError:
                    print("There is no current plane.")
            case 23:
                print("You have selected to print the planes information.")
                try:
                    print(plane)
                except AttributeError:
                    print("There is no current plane.")
            case 24:
                print("You have selected to add the current plane to the airport.")
                try:
                    airport.add_plane(plane)
                except AttributeError:
                    print("There is no current plane.")
            case 25:
                print("You have selected to create and add a new plane to the airport.")
                plane = read_plane_info()
                if plane is not None:
                    airport.add_plane(plane)
            case 26:
                print("You have selected to get the airport's planes.")
                for plane in airport.get_planes():
                    print(plane)
            case 27:
                print("You have selected to update a plane's information.")
                name_or_number = input("Enter the plane's name or number: ")
                found = False
                for plane in airport.get_planes():
                    if plane.get_name_or_number() == name_or_number:
                        print("Plane found.")
                        found = True
                        print("Please enter the new information for the plane.")
                        info = read_plane_info()
                        if info is not None:
                            plane.update_plane(info.get_name_or_number(), info.get_airline_company(), info.get_number_of_seats(), info.get_destination())
                        break
                if not found:
                    print("Plane not found.")
            case 28:
                print("You have selected to sort the passengers of a plane by last name.")
                plane_name = input("Enter the plane's name or number: ")
                airport.sort_passengers(plane_name)
            case 29:
                print("You have selected to sort the airport's planes by capacity.")
                airport.sort_planes()
            case 30:
                print("You have selected to sort the planes by the number of passengers starting with a given string.")
                string = input("Enter the string: ")
                airport.sort_planes_passengers_name_start(string)
            case 32:
                print("You have selected to sort the planes by the number of passengers concatenated with the plane's destination.")
                airport.sort_planes_nr_passengers_destination()
            case 33:
                print("You have selected to search for planes with passengers whose passport numbers start with the same three digits.")
                result = airport.search_plane_passenger_passport_nr_starts_with()
                for passenger in result:
                    print(passenger)
            case 34:
                print("You have selected to search for passengers on a specific plane whose first or last name contains a given string.")
                plane_name = input("Enter the plane's name or number: ")
                string = input("Enter the string: ")
                result = airport.search_passenger_name_contains(plane_name ,string)
                for passenger in result:
                    print(passenger)
            case 35:
                print("You have selected to search for a passenger by first and last name across all planes at the airport.")
                first_name = input("Enter the passenger's first name: ")
                last_name = input("Enter the passenger's last name: ")
                result = airport.search_passenger_name(first_name, last_name)
                for passenger in result:
                    print(passenger)
            case "exit":
                print("Exiting the program.")
                break
            case _:
                print("Invalid input. Please try again.")

if __name__ == '__main__':
    airport = set_Up()
    main(airport)