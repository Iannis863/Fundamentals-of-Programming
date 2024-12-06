from Passenger import Passenger

class Plane:
    """
    A class to represent a plane.

    Attributes:
    ----------
    name_or_number : str | int
        The name or number of the plane.
    airline_company : str
        The airline company of the plane.
    number_of_seats : int
        The number of seats in the plane.
    destination : str
        The destination of the plane.
    passengers : list
        The list of passengers on the plane.
    """

    def __init__(self, name_or_number: str | int, airline_company: str, number_of_seats: int, destination: str):
        """
        Constructs all the necessary attributes for the plane object.

        Parameters:
        ----------
        name_or_number : str | int
            The name or number of the plane.
        airline_company : str
            The airline company of the plane.
        number_of_seats : int
            The number of seats in the plane.
        destination : str
            The destination of the plane.

        Raises:
        ------
        ValueError
            If name_or_number is not a string or an integer.
            If airline_company is not a string.
            If number_of_seats is not an integer.
            If destination is not a string.
        """
        if not isinstance(name_or_number, str) and not isinstance(name_or_number, int):
            raise ValueError("Name or number must be a string or an integer")
        if not isinstance(airline_company, str):
            raise ValueError("Airline company must be a string")
        if not isinstance(number_of_seats, int):
            raise ValueError("Number of seats must be an integer")
        if not isinstance(destination, str):
            raise ValueError("Destination must be a string")
        self.name_or_number = name_or_number
        self.airline_company = airline_company
        self.number_of_seats = number_of_seats
        self.destination = destination
        self.passengers = []

    def get_name_or_number(self):
        """
        Gets the name or number of the plane.

        Returns:
        -------
        str | int
            The name or number of the plane.
        """
        return self.name_or_number

    def set_name_or_number(self, name_or_number: str | int):
        """
        Sets the name or number of the plane.

        Parameters:
        ----------
        name_or_number : str | int
            The new name or number of the plane.

        Raises:
        ------
        ValueError
            If name_or_number is not a string or an integer.
        """
        if not isinstance(name_or_number, str) and not isinstance(name_or_number, int):
            raise ValueError("Name or number must be a string or an integer")
        self.name_or_number = name_or_number

    def get_airline_company(self):
        """
        Gets the airline company of the plane.

        Returns:
        -------
        str
            The airline company of the plane.
        """
        return self.airline_company

    def set_airline_company(self, airline_company: str):
        """
        Sets the airline company of the plane.

        Parameters:
        ----------
        airline_company : str
            The new airline company of the plane.

        Raises:
        ------
        ValueError
            If airline_company is not a string.
        """
        if not isinstance(airline_company, str):
            raise ValueError("Airline company must be a string")
        self.airline_company = airline_company

    def get_number_of_seats(self):
        """
        Gets the number of seats in the plane.

        Returns:
        -------
        int
            The number of seats in the plane.
        """
        return self.number_of_seats

    def set_number_of_seats(self, number_of_seats: int):
        """
        Sets the number of seats in the plane.

        Parameters:
        ----------
        number_of_seats : int
            The new number of seats in the plane.

        Raises:
        ------
        ValueError
            If number_of_seats is not an integer.
        """
        if not isinstance(number_of_seats, int):
            raise ValueError("Number of seats must be an integer")
        self.number_of_seats = number_of_seats

    def get_destination(self):
        """
        Gets the destination of the plane.

        Returns:
        -------
        str
            The destination of the plane.
        """
        return self.destination

    def set_destination(self, destination: str):
        """
        Sets the destination of the plane.

        Parameters:
        ----------
        destination : str
            The new destination of the plane.

        Raises:
        ------
        ValueError
            If destination is not a string.
        """
        if not isinstance(destination, str):
            raise ValueError("Destination must be a string")
        self.destination = destination

    def get_passengers(self):
        """
        Gets the list of passengers on the plane.

        Returns:
        -------
        list
            The list of passengers on the plane.
        """
        return self.passengers

    def add_passenger(self, passenger: Passenger):
        """
        Adds a passenger to the plane.

        Parameters:
        ----------
        passenger : Passenger
            The passenger to add to the plane.

        Raises:
        ------
        ValueError
            If passenger is not an instance of Passenger.
        Exception
            If there are no available seats.
        """
        if not isinstance(passenger, Passenger):
            raise ValueError("Passenger must be an instance of Passenger")
        if len(self.passengers) < self.number_of_seats:
            self.passengers.append(passenger)
        else:
            raise Exception("No available seats")

    def remove_passenger(self, passport_number: int):
        """
        Removes a passenger from the plane by passport number.

        Parameters:
        ----------
        passport_number : int
            The passport number of the passenger to remove.

        Raises:
        ------
        ValueError
            If passport_number is not an integer.
        """
        if not isinstance(passport_number, int):
            raise ValueError("Passport number must be an integer")
        self.passengers = [p for p in self.passengers if p.get_passport_number() != passport_number]

    def update_passenger(self, passport_number: int, first_name: str, last_name: str):
        """
        Updates the details of a passenger on the plane.

        Parameters:
        ----------
        passport_number : int
            The passport number of the passenger to update.
        first_name : str
            The new first name of the passenger.
        last_name : str
            The new last name of the passenger.

        Raises:
        ------
        ValueError
            If passport_number is not an integer.
            If first_name is not a string.
            If last_name is not a string.
        Exception
            If the passenger is not found.
        """
        if not isinstance(passport_number, int):
            raise ValueError("Passport number must be an integer")
        if not isinstance(first_name, str):
            raise ValueError("First name must be a string")
        if not isinstance(last_name, str):
            raise ValueError("Last name must be a string")
        for passenger in self.passengers:
            if passenger.get_passport_number() == passport_number:
                passenger.set_first_name(first_name)
                passenger.set_last_name(last_name)
                return
        raise Exception("Passenger not found")

    def sort_passengers(self):
        """
        Sorts the passengers on the plane by last name.
        """
        self.passengers.sort(key=lambda p: p.get_last_name())

    def search_passengers_name_contains(self, string: str):
        """
        Searches for passengers whose first or last name contains a given string.

        Parameters:
        ----------
        string : str
            The string to search for in the passengers' names.

        Returns:
        -------
        list
            A list of passengers whose names contain the given string.
        """
        return [passenger for passenger in self.passengers if string in passenger.get_first_name() or string in passenger.get_last_name()]

    def search_passengers_name(self, first_name: str, last_name: str):
        """
        Searches for a passenger by first and last name.

        Parameters:
        ----------
        first_name : str
            The first name of the passenger to search for.
        last_name : str
            The last name of the passenger to search for.

        Returns:
        -------
        bool
            True if a passenger with the given first and last name is found, False otherwise.
        """
        return any(p.get_first_name() == first_name and p.get_last_name() == last_name for p in self.passengers)

    def update_plane(self, name_or_number: str | int, airline_company: str, number_of_seats: int, destination: str):
        """
        Updates the details of the plane.

        Parameters:
        ----------
        name_or_number : str | int
            The new name or number of the plane.
        airline_company : str
            The new airline company of the plane.
        number_of_seats : int
            The new number of seats in the plane.
        destination : str
            The new destination of the plane.

        Raises:
        ------
        ValueError
            If name_or_number is not a string or an integer.
            If airline_company is not a string.
            If number_of_seats is not an integer.
            If destination is not a string.
        """
        if not isinstance(name_or_number, str) and not isinstance(name_or_number, int):
            raise ValueError("Name or number must be a string or an integer")
        if not isinstance(airline_company, str):
            raise ValueError("Airline company must be a string")
        if not isinstance(number_of_seats, int):
            raise ValueError("Number of seats must be an integer")
        if not isinstance(destination, str):
            raise ValueError("Destination must be a string")
        self.name_or_number = name_or_number
        self.airline_company = airline_company
        self.number_of_seats = number_of_seats
        self.destination = destination

    def __str__(self):
        """
        Returns a string representation of the plane.

        Returns:
        -------
        str
            A string representation of the plane.
        """
        return f"{self.name_or_number} ({self.airline_company}) - {self.destination} ({len(self.passengers)}/{self.number_of_seats})"