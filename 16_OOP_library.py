class Book:
    def __init__(self,book_title, book_author):
        self.title = book_title
        self.author = book_author
        self.is_available = True
    def checkout_book(self):
        if self.is_available:
            print(f"📖 Success! You checked out '{self.title}'.")
            self.is_available = False
        else:
            print(f"❌ Sorry, '{self.title}' is already checked out!")
        
    def return_book(self):
        if not self.is_available:
            print(f"🔄 Success! '{self.title}' has been returned to the shelf.")
            self.is_available = True
        else:
            print(f"🤔 '{self.title}' is already sitting on the shelf.")
book_1 = Book("The Hobbit", "J.R.R. Tolkien")
book_1.checkout_book()
book_1.return_book()
        