from Plane import Plane

class Airport:
    """
    A class to represent an airport.

    Attributes:
    ----------
    planes : list
        The list of planes at the airport.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the airport object.
        """
        self.planes = []

    def get_planes(self):
        """
        Gets the list of planes at the airport.

        Returns:
        -------
        list
            The list of planes at the airport.
        """
        return self.planes

    def add_plane(self, plane: Plane):
        """
        Adds a plane to the airport.

        Parameters:
        ----------
        plane : Plane
            The plane to add to the airport.

        Raises:
        ------
        ValueError
            If plane is not an instance of Plane.
        """
        if not isinstance(plane, Plane):
            raise ValueError("Plane must be an instance of Plane")
        self.planes.append(plane)

    def sort_passengers(self, plane_name_or_number: str | int):
        """
        Sorts the passengers on a specific plane by last name.

        Parameters:
        ----------
        plane_name_or_number : str | int
            The name or number of the plane whose passengers to sort.

        Raises:
        ------
        ValueError
            If plane_name_or_number is not a string or an integer.
        Exception
            If the plane is not found.
        """
        if not isinstance(plane_name_or_number, str) and not isinstance(plane_name_or_number, int):
            raise ValueError("Plane name or number must be a string or an integer")
        for plane in self.planes:
            if plane.get_name_or_number() == plane_name_or_number:
                plane.sort_passengers()
                return
        raise Exception("Plane not found")

    def sort_planes(self):
        """
        Sorts the planes at the airport by the number of passengers.
        """
        self.planes.sort(key=lambda p: len(p.get_passengers()))

    def sort_planes_passengers_name_start(self, string: str):
        """
        Sorts the planes at the airport by the number of passengers whose first name starts with a given string.

        Parameters:
        ----------
        string : str
            The string to search for in the passengers' first names.

        Raises:
        ------
        ValueError
            If string is not a string.
        """
        if not isinstance(string, str):
            raise ValueError("String must be a string")
        self.planes.sort(key=lambda p: len([passenger for passenger in p.get_passengers() if passenger.get_first_name().startswith(string)]))

    def sort_planes_nr_passengers_destination(self):
        """
        Sorts the planes at the airport by the string obtained by concatenating the number of passengers and destination.
        """
        self.planes.sort(key=lambda p: (str(len(p.get_passengers())) + p.get_destination()))

    def search_plane_passenger_passport_nr_starts_with(self):
        """
        Searches for planes with passengers whose passport numbers start with the same three digits.

        Returns:
        -------
        list
            A list of planes with passengers whose passport numbers start with the same three digits.
        """
        return [plane for plane in self.planes if any(str(p1.get_passport_number()).startswith(str(p2.get_passport_number())[:3]) for p1 in plane.get_passengers() for p2 in plane.get_passengers() if p1 != p2)]

    def search_passenger_name_contains(self, plane_name_or_number:str | int, string: str):
        """
        Searches for passengers on a specific plane whose first or last name contains a given string.

        Parameters:
        ----------
        plane_name_or_number : str | int
            The plane to search for passengers on.
        string : str
            The string to search for in the passengers' names.

        Returns:
        -------
        list
            A list of passengers on the plane whose names contain the given string.

        Raises:
        ------
        ValueError
            If plane_name_or_number is not a string or an integer.
            If string is not a string.
        """
        if not isinstance(plane_name_or_number, str):
            raise ValueError("Plane name or number must be a string")
        if not isinstance(string, str):
            raise ValueError("String must be a string")
        for plane in self.planes:
            if plane.get_name_or_number() == plane_name_or_number:
                return plane.search_passengers_name_contains(string)

    def search_passenger_name(self, first_name: str, last_name: str):
        """
        Searches for a passenger by first and last name across all planes at the airport.

        Parameters:
        ----------
        first_name : str
            The first name of the passenger to search for.
        last_name : str
            The last name of the passenger to search for.

        Returns:
        -------
        list
            A list of planes with the passenger found.

        Raises:
        ------
        ValueError
            If first_name is not a string.
            If last_name is not a string.
        """
        if not isinstance(first_name, str):
            raise ValueError("First name must be a string")
        if not isinstance(last_name, str):
            raise ValueError("Last name must be a string")
        return [plane for plane in self.planes if plane.search_passengers_name(first_name, last_name)]