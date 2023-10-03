library_books = []


def add_book(title, author):
    book = {"title": title, "author": author, "availability": True}
    library_books.append(book)
    print(f"'{title}' by {author} has been added to the library.")


def borrow_book(title):
    for book in library_books:
        if book["title"] == title:
            if book["availability"]:
                book["availability"] = False
                print(f"'{title}' has been borrowed.")
            else:
                print(f"'{title}' is not available.")
            return
    print(f"'{title}' is not found in the library.")


def return_book(title):
    for book in library_books:
        if book["title"] == title:
            if not book["availability"]:
                book["availability"] = True
                print(f"'{title}' has been returned.")
            else:
                print(f"'{title}' is already available in the library.")
            return
    print(f"'{title}' is not found in the library.")


def find_book(title):
    for book in library_books:
        if book["title"] == title:
            return book
    return None
