class Library:
    def __init__(self):
        self.book_Lists=[]

    def add_book(self,book):
        self.book_Lists.append(book)

    def display_books(self):
        for book in self.book_Lists:
            print(f"Book_Name:{book.name}\nAuthor:{book.author}\nAvailability: {"Available" if book.availability else "Not Available"}\n")

    def borrow(self,name):
        for b in self.book_Lists:
            if b.name==name:
                if not b.availability:
                    print("Book Already Borrowed")
                else:
                    print(f"{name} Borrowed")
                    b.availability=False
                break
        else:
            print("Book Not available")
                    
class Book:
    def __init__(self,name,author):
        self.name=name
        self.author=author
        self.availability=True

book1 = Book("Python", "John")
book2 = Book("Java", "James")
book3 = Book("c", "abc")
book4 = Book("c++", "cba")

library1 = Library()

library1.add_book(book1)
library1.add_book(book2)
library1.borrow('Python')
library1.borrow('Python')
library1.borrow('c#')

library2=Library()

library2.add_book(book3)
library2.add_book(book4)
library2.borrow('Python')
library2.borrow('c++')
library2.borrow('c#')

library1.display_books()
print()
library2.display_books()
