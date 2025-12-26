

import unittest
from library_system import (
    Book, Library, LibraryBook,
    get_one_to_many,
    get_library_total_prices,
    get_many_to_many_with_keyword
)


class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        self.libraries = [
            Library(1, "Центральная библиотека"),
            Library(2, "Детский отдел библиотеки"),
            Library(3, "Городской книжный центр"),
        ]

        self.books = [
            Book(1, "Война и мир", 1200, 1),
            Book(2, "Преступление и наказание", 900, 1),
            Book(3, "Маленький принц", 700, 2),
            Book(4, "Гарри Поттер", 1100, 2),
            Book(5, "1984", 1000, 3),
        ]

        self.library_books = [
            LibraryBook(1, 1),
            LibraryBook(1, 2),
            LibraryBook(2, 3),
            LibraryBook(2, 4),
            LibraryBook(3, 5),
            LibraryBook(1, 4),
        ]

    def test_one_to_many(self):
        result = get_one_to_many(self.libraries, self.books)
        self.assertIn(("Война и мир", 1200, "Центральная библиотека"), result)

    def test_library_total_prices(self):
        result = get_library_total_prices(self.libraries, self.books)
        expected = ("Центральная библиотека", 2100)
        self.assertIn(expected, result)

    def test_many_to_many_with_keyword(self):
        result = get_many_to_many_with_keyword(
            self.libraries,
            self.books,
            self.library_books,
            "отдел"
        )
        self.assertIn("Детский отдел библиотеки", result)
        self.assertIn("Маленький принц", result["Детский отдел библиотеки"])


if __name__ == "__main__":
    unittest.main()