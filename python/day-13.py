#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.author = author
        self.title = title
        self.price = price
        
    def display(self):
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Price: " + str(self.price))