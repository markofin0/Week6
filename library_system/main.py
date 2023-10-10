import books as b
import members as m


def display_menu():
    print("\nLibrary Management System")
    print("----------------------------")
    print("1. Add a new book to the library.")
    print("2. Register a new library member.")
    print("3. Borrow a book.")
    print("4. Return a book.")
    print("5. Display all books.")
    print("6. Display all members.")
    print("7. Exit.")
    print("----------------------------")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            b.add_book(input('What is the title of the book? '), input('Who is the author? '))
            pass
        elif choice == "2":
            m.register_member(input('What is your name ? '))
            pass
        elif choice == "3":
            b.borrow_book(input('Which book would you like to borrow? '))
            pass
        elif choice == "4":
            b.return_book(input('Which book would you like to return? '))
            pass
        elif choice == "5":
            print(b.library_books)
            pass
        elif choice == "6":
            print(m.library_members)
            pass
        elif choice == "7":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
