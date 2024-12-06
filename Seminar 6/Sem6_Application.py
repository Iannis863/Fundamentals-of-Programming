from Sem6_Domain import Book
from Sem6_Infrastructure import BookRepository

class BookController:
    def __init__(self, book_repository: BookRepository):
        """
        Initialize the controller
        :param book_repository: BookRepository object\
        :raises: TypeError
        """
        if not isinstance(book_repository, BookRepository):
            raise TypeError("BookRepository must be of type BookRepository")
        self.__book_repository = book_repository

    def add(self, book: Book):
        """
        Add a book to the repository
        :param book: The book to add
        :raises: TypeError
        """
        if not isinstance(book, Book):
            raise TypeError("Book must be of type Book")
        self.__book_repository.add_book(book)

    def delete_book(self, book: Book):
        """
        Delete a book from the repository
        :param book: The book to delete
        :raises: TypeError
        """
        if not isinstance(book, Book):
            raise TypeError("Book must be of type Book")
        self.__book_repository.delete_book(book)



