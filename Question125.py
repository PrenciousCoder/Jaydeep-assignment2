#Question9 section2
class Library:
    def __init__(self):
        self.book_number=input("Enter the book number: ")
        self.book_name=input("Enter the book name: ")
        self.author=input("Enter the author: ")
        self.publisher=input("name of publisher: ")
        self.num_copies_made=int(input("Enter the number of copies:  "))
        self.price=input("Enter the price")
        self.num_available=int(input("Enter the nu mber of available copies: "))
    def issue(self):
        if self.num_available>0:
            self.num_available=self.num_available-1
            return "Book Issued"
    def return_book(self):
        temp=input("Return Book?(y/n) ")
        if temp=="y":
            self.num_available=self.num_available+1
        else:
            pass
    def print_book(self):
        print(self.book_number)
        print(self.book_name)
        print(self.author)
        print(self.publisher)
        print(self.num_copies_made)
        print(self.price)
        print(self.num_available)

inst=Library()
print(inst.issue())
print(inst.return_book())
print(inst.print_book())        