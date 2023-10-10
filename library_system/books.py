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
                return True
            else:
                return False


def return_book(title):
    for book in library_books:
        if book["title"] == title:
            if not book["availability"]:
                book["availability"] = True
                return True
            else:
                return False


def find_book(title):
    for book in library_books:
        if book["title"] == title:
            return book
    return None

def display_books():
    titles = []
    for book in library_books:
        titles.append(library_books[book][0])
    return titles