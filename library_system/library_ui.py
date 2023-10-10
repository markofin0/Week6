import tkinter as tk
from tkinter import messagebox, simpledialog
import main  # Assuming main.py contains the functions for the library operations
import books as b
import members as m


def register_member():
    # Call the function to register a member
    member = simpledialog.askstring("Input", "Enter the new member's name: ")
    if member:
        m.register_member(member)
        messagebox.showinfo("Success", "Member added successfully!")
    else:
        messagebox.showwarning("Warning", "Member addition cancelled. Name was not provided.")


def borrow_book():
    # Call the function to borrow a book
    book = simpledialog.askstring("Input", "Enter the book's name: ")
    if book:
        if b.borrow_book(book):
            messagebox.showinfo("Success", "Book successfully borrowed!")
        else:
            messagebox.showwarning("Warning", "Book is not available!")
    else:
        messagebox.showwarning("Warning", "Book request cancelled. Title was not provided.")


def return_book():
    # Call the function to return a book
    book = simpledialog.askstring("Input", "Enter the book's name: ")
    if book:
        if b.return_book(book):
            messagebox.showinfo("Success", "Book successfully returned!")
        else:
            messagebox.showwarning("Warning", "Book either does not exist or is already returned!")
    else:
        messagebox.showwarning("Warning", "Return cancelled. Title was not provided.")


def display_books():
    # Call the function to display all books
    messagebox.showinfo("Books",b.display_books())


def display_members():
    # Call the function to display all members
    messagebox.showinfo("Info", "Display members functionality here")


def add_book():
    """Capture details and add a book to the library."""
    title = simpledialog.askstring("Input", "Enter the book's title:")
    if title:  # Check if the user provided a title (didn't press cancel)
        author = simpledialog.askstring("Input", "Enter the book's author:")
        if author:  # Check if the user provided an author
            b.add_book(title, author)  # Using the function from books.py
            messagebox.showinfo("Success", "Book added successfully!")
        else:
            messagebox.showwarning("Warning", "Book addition cancelled. Author was not provided.")
    else:
        messagebox.showwarning("Warning", "Book addition cancelled. Title was not provided.")


root = tk.Tk()
root.title("Library Management System")

# Menu buttons
add_book_btn = tk.Button(root, text="Add a new book", command=add_book)
add_book_btn.pack(pady=10)

register_member_btn = tk.Button(root, text="Register a new member", command=register_member)
register_member_btn.pack(pady=10)

borrow_book_btn = tk.Button(root, text="Borrow a book", command=borrow_book)
borrow_book_btn.pack(pady=10)

return_book_btn = tk.Button(root, text="Return a book", command=return_book)
return_book_btn.pack(pady=10)

display_books_btn = tk.Button(root, text="Display all books", command=display_books)
display_books_btn.pack(pady=10)

display_members_btn = tk.Button(root, text="Display all members", command=display_members)
display_members_btn.pack(pady=10)

root.mainloop()
