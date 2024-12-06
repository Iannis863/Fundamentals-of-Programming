from Sem6_Domain import Book


class BookRepository:
    def __init__(self):
        """
        Initialize a repository for books
        """
        self.__books = []

    def __str__(self):
        """
        Print all the books
        """
        for book in self.__books:
            print(book)

    def get_books(self):
        """
        Get all the books
        :return: The books
        """
        return self.__books

    def add_book(self, book:Book):
        """
        Add a book to the repository
        :param book: A book
        :return: The repository
        :raises: TypeError
        """
        if not isinstance(book, Book):
            raise TypeError
        self.__books.append(book)

    def delete_book(self, book_to_delete:Book):
        """
        Delete a book from the repository
        :param book_to_delete: The book to delete
        :raises: TypeError
        """
        if not isinstance(book_to_delete, Book):
            raise TypeError("Book must be of type 'Book'")
        for book in self.__books:
            if book == book_to_delete:
                self.__books.remove(book)