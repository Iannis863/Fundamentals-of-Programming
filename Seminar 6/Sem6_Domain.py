class Book:
    def __init__(self, code:int, title:str, author:str, year:int, price:float):
        """
        Initialize a book instance.
        :param code: The code of the book.
        :param title: The title of the book.
        :param author: The author of the book.
        :param year: The year of the book.
        :param price: The price of the book.
        :raises: TypeError, ValueError
        """
        if not isinstance(code, int):
            raise TypeError("code must be an integer")
        if not isinstance(title, str):
            raise TypeError("title must be an string")
        if not isinstance(author, str):
            raise TypeError("author must be an string")
        if not isinstance(year, int):
            raise TypeError("year must be an integer")
        if not isinstance(price, float):
            raise TypeError("price must be an float")
        if year < 0 or year > 2024:
            raise ValueError("invalid year")
        self.__code = code
        self.__title = title
        self.__author = author
        self.__year = year
        self.__price = price

    def __str__(self):
        """
        Return a string representation of the book.
        :return: The string representation of the book.
        """
        return str(self.__code) + self.__title + self.__author + str(self.__year) + str(self.__price)

    def __eq__(self, other):
        """
        Check if two books are equal
        :param other: The other book to compare.
        :return: True if the two books are equal, False otherwise.
        :raises: TypeError
        """
        if not isinstance(other, Book):
            raise TypeError("other must be an instance of Book")
        return self.__code == other.__code and self.__title == other.__title and self.__author == other.__author and self.__year == other.__year and self.__price == other.__price

    def get_code(self):
        """
        Return the code of the book.
        :return: The code of the book.
        """
        return self.__code

    def get_title(self):
        """
        Return the title of the book.
        :return: The title of the book.
        """
        return self.__title

    def get_author(self):
        """
        Return the author of the book.
        :return: The author of the book.
        """
        return self.__author

    def get_year(self):
        """
        Return the year of the book.
        :return: The year of the book.
        """
        return self.__year

    def get_price(self):
        """
        Return the price of the book.
        :return: The price of the book.
        """
        return self.__price

    def set_code(self, code:int):
        """
        Set the code of the book.
        :param code: The new code of the book.
        :return: The book
        :raises: TypeError
        """
        if not isinstance(code, int):
            raise TypeError("code must be an integer")
        self.__code = code
        return self

    def set_title(self, title:str):
        """
        Set the title of the book.
        :param title: The new title of the book.
        :return: The book
        :raises: TypeError
        """
        if not isinstance(title, str):
            raise TypeError("title must be an string")
        self.__title = title
        return self

    def set_author(self, author:str):
        """
        Set the author of the book.
        :param author: The new author of the book.
        :return: The book
        :raises: TypeError
        """
        if not isinstance(author, str):
            raise TypeError("author must be an string")
        self.__author = author
        return self

    def set_year(self, year:int):
        """
        Set the year of the book.
        :param year: The new year of the book.
        :return: The book
        :raises: TypeError, ValueError
        """
        if not isinstance(year, int):
            raise TypeError("year must be an integer")
        if year < 0 or year > 2024:
            raise ValueError("invalid year")
        self.__year = year
        return self

    def update_book(self, code:int, title:str, author:str, year:int, price:float):
        """
        Update the book with the given parameters.
        :param code: The new code of the book.
        :param title: The new title of the book.
        :param author: The new author of the book.
        :param year: The new year of the book.
        :param price: The new price of the book.
        :return: The book
        :raises: TypeError, ValueError
        """
        if not isinstance(code, int):
            raise TypeError("code must be an integer")
        if not isinstance(title, str):
            raise TypeError("title must be an string")
        if not isinstance(author, str):
            raise TypeError("author must be an string")
        if not isinstance(year, int):
            raise TypeError("year must be an integer")
        if not isinstance(price, float):
            raise TypeError("price must be an float")
        if year < 0 or year > 2024:
            raise ValueError("invalid year")
        self.__code = code
        self.__title = title
        self.__author = author
        self.__year = year
        self.__price = price
        return self