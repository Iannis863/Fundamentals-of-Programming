class Passenger:
    """
    A class to represent a passenger.

    Attributes:
    ----------
    passport_number : int
        The passport number of the passenger.
    first_name : str
        The first name of the passenger.
    last_name : str
        The last name of the passenger.
    """

    def __init__(self, passport_number: int, first_name: str, last_name: str):
        """
        Constructs all the necessary attributes for the passenger object.

        Parameters:
        ----------
        passport_number : int
            The passport number of the passenger.
        first_name : str
            The first name of the passenger.
        last_name : str
            The last name of the passenger.

        Raises:
        ------
        ValueError
            If passport_number is not an integer.
            If first_name is not a string.
            If last_name is not a string.
        """
        if not isinstance(passport_number, int):
            raise ValueError("Passport number must be an integer")
        if not isinstance(first_name, str):
            raise ValueError("First name must be a string")
        if not isinstance(last_name, str):
            raise ValueError("Last name must be a string")
        self.passport_number = passport_number
        self.first_name = first_name
        self.last_name = last_name

    def get_passport_number(self):
        """
        Gets the passport number of the passenger.

        Returns:
        -------
        int
            The passport number of the passenger.
        """
        return self.passport_number

    def set_passport_number(self, passport_number: int):
        """
        Sets the passport number of the passenger.

        Parameters:
        ----------
        passport_number : int
            The new passport number of the passenger.

        Raises:
        ------
        ValueError
            If passport_number is not an integer.
        """
        if not isinstance(passport_number, int):
            raise ValueError("Passport number must be an integer")
        self.passport_number = passport_number

    def get_first_name(self):
        """
        Gets the first name of the passenger.

        Returns:
        -------
        str
            The first name of the passenger.
        """
        return self.first_name

    def set_first_name(self, first_name: str):
        """
        Sets the first name of the passenger.

        Parameters:
        ----------
        first_name : str
            The new first name of the passenger.

        Raises:
        ------
        ValueError
            If first_name is not a string.
        """
        if not isinstance(first_name, str):
            raise ValueError("First name must be a string")
        self.first_name = first_name

    def get_last_name(self):
        """
        Gets the last name of the passenger.

        Returns:
        -------
        str
            The last name of the passenger.
        """
        return self.last_name

    def set_last_name(self, last_name: str):
        """
        Sets the last name of the passenger.

        Parameters:
        ----------
        last_name : str
            The new last name of the passenger.

        Raises:
        ------
        ValueError
            If last_name is not a string.
        """
        if not isinstance(last_name, str):
            raise ValueError("Last name must be a string")
        self.last_name = last_name

    def __str__(self):
        """
        Returns a string representation of the passenger.

        Returns:
        -------
        str
            A string representation of the passenger.
        """
        return f"{self.first_name} {self.last_name}, Passport number: {self.passport_number}"