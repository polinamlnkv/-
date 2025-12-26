# library_system.py

class Book:
    def __init__(self, book_id, title, price, library_id):
        self.book_id = book_id
        self.title = title
        self.price = price
        self.library_id = library_id


class Library:
    def __init__(self, lib_id, name):
        self.lib_id = lib_id
        self.name = name


class LibraryBook:
    def __init__(self, lib_id, book_id):
        self.lib_id = lib_id
        self.book_id = book_id


def get_one_to_many(libraries, books):

    return [
        (b.title, b.price, l.name)
        for l in libraries
        for b in books
        if b.library_id == l.lib_id
    ]


def get_library_total_prices(libraries, books):

    result = []
    for l in libraries:
        prices = [b.price for b in books if b.library_id == l.lib_id]
        if prices:
            result.append((l.name, sum(prices)))
    return result


def get_many_to_many_with_keyword(libraries, books, library_books, keyword):

    temp = [
        (l.name, b.title)
        for l in libraries
        for lb in library_books
        for b in books
        if l.lib_id == lb.lib_id and b.book_id == lb.book_id
    ]

    result = {}
    for lib_name, book_title in temp:
        if keyword.lower() in lib_name.lower():
            result.setdefault(lib_name, []).append(book_title)

    return result
