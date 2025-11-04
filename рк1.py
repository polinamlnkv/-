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



libraries = [
    Library(1, "Центральная библиотека"),
    Library(2, "Детский отдел библиотеки"),
    Library(3, "Городской книжный центр"),
]

books = [
    Book(1, "Война и мир", 1200, 1),
    Book(2, "Преступление и наказание", 900, 1),
    Book(3, "Маленький принц", 700, 2),
    Book(4, "Гарри Поттер и философский камень", 1100, 2),
    Book(5, "1984", 1000, 3),
]

library_books = [
    LibraryBook(1, 1),
    LibraryBook(1, 2),
    LibraryBook(2, 3),
    LibraryBook(2, 4),
    LibraryBook(3, 5),
    LibraryBook(1, 4),  # книга есть и в центральной библиотеке
]


print("=" * 60)
print("ИСХОДНЫЕ ДАННЫЕ\n")

print("Библиотеки:")
for l in libraries:
    print(f"ID={l.lib_id}, Название='{l.name}'")

print("\nКниги:")
for b in books:
    print(f"ID={b.book_id}, Название='{b.title}', Цена={b.price}, ID библиотеки={b.library_id}")

print("\nСвязи (многие-ко-многим):")
for lb in library_books:
    print(f"ID библиотеки={lb.lib_id}, ID книги={lb.book_id}")

print("=" * 60)



print("\n1. Список всех связанных книг и библиотек (один-ко-многим):")

one_to_many = [(b.title, b.price, l.name)
               for l in libraries
               for b in books
               if b.library_id == l.lib_id]

one_to_many_sorted = sorted(one_to_many, key=lambda x: x[2])

for title, price, lib_name in one_to_many_sorted:
    print(f"{lib_name:30} | {title:35} | {price:>5} руб.")

print("=" * 60)



print("\n2. Список библиотек с суммарной стоимостью книг (один-ко-многим):")

lib_sums = []
for l in libraries:
    prices = [b.price for b in books if b.library_id == l.lib_id]
    if prices:
        total = sum(prices)
        lib_sums.append((l.name, total))

lib_sums_sorted = sorted(lib_sums, key=lambda x: x[1], reverse=True)

for lib_name, total in lib_sums_sorted:
    print(f"{lib_name:30} | Суммарная стоимость книг: {total} руб.")

print("=" * 60)



print("\n3. Библиотеки (в названии есть 'отдел') и их книги (многие-ко-многим):")


many_to_many_temp = [(l.name, b.title)
                     for l in libraries
                     for lb in library_books
                     for b in books
                     if l.lib_id == lb.lib_id and b.book_id == lb.book_id]

many_to_many_result = {}
for lib_name, book_title in many_to_many_temp:
    if "отдел" in lib_name.lower():
        many_to_many_result.setdefault(lib_name, []).append(book_title)


if many_to_many_result:
    for lib_name, titles in many_to_many_result.items():
        print(f"{lib_name}:")
        for t in titles:
            print(f"   - {t}")
else:
    print("Нет библиотек, содержащих слово 'отдел'.")

print("=" * 60)
