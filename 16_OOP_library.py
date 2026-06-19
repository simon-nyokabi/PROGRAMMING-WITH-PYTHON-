class Book:
    def __init__(self,book_title, book_author):
        self.title = book_title
        self.author = book_author
        self.is_available = True
    def checkout_book(self):
        if self.is_available:
            print(f"Success! You checked out '{self.title}'.")
            self.is_available = False
        else:
            print(f"Sorry, '{self.title}' is already checked out!")
        
    def return_book(self):
        if not self.is_available:
            print(f"Success! '{self.title}' has been returned to the shelf.")
            self.is_available = True
        else:
            print(f"'{self.title}' is already sitting on the shelf.")
book_1 = Book("The Hobbit", "J.R.R. Tolkien")
book_1.checkout_book()
book_1.return_book()
# NOW WE SAVE THE BOOKS USING FILES
my_book = Book("The Fellowship of the Ring", "J.R.R. Tolkien")
#using normal method
'''with open("current_book.txt", "w") as file:
    file.write(my_book.title)
with open("current_book.txt", "r") as file:
    books = file.read()
    print(books)'''
#USING JSON FILES TO MAKE THE FILE MORE ORGANISED AND STRUCTURED
import json
book_data = {
    "title": my_book.title,
    "author": my_book.author,
    "is_available" : my_book.is_available
}

with open("book_storage.json", "w") as file:
    json.dump(book_data, file, indent=4 )
with open("book_storage.json", "r") as file:
    loaded_data = json.load(file)
reloaded_data = Book(loaded_data["title"], loaded_data["author"])
print(reloaded_data.author)
