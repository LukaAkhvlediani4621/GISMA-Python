


class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True


    def display_book_info(self):
         print(self.title, self.author, self.year, self.available)


    def borrow_book(self):
        if self.available:
            self.available = False
            print("The book is available for borrowing")
        else:
            print("The book is not available at the moment, we are sorry")