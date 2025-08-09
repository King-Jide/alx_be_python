class Book:
    def __init__(self, title, author):
        """ Represents a book in the library."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Return true if the book is available."""
        return not self._is_checked_out

class Library:
    """Manages a collection of books."""
    def __init__(self):
        self._books = []

    def add_book(self,book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self,title):
        """Check out a book if its available"""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False
    
    def return_book(self, title):
        """Return a book to the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False
    
    def list_available_books(self):
        """Print all available books"""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}") 
