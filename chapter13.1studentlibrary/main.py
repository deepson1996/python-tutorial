class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("* "+ book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please return it on the due date.")
            self.books.remove(bookName)
            return True
        else:
            print(f"Sorry, {bookName} is not currently available in this library.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print(f"Thank you for returning {bookName}. Hope you enjoyed it.")

class Student:
    def __init__(self):
        self.bookList = []
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(['Algorithms', 'Data Structures', 'Operating Systems', 'Python', 'Java', 'C++'])
    student = Student()
    while(True):
        welcomeMsg = '''
        
====== Welcome to central library ======
Please choose an option: 
1. Request a book
2. Return a book
3. Exit the library
4. Display available books'''
        print(welcomeMsg)
        choice = int(input("Enter your choice: "))
        if choice == 4:
            centralLibrary.displayAvailableBooks()
        elif choice == 1:
            bookName = student.requestBook()
            centralLibrary.borrowBook(bookName)
        elif choice == 2:
            bookName = student.returnBook()
            centralLibrary.returnBook(bookName)
        elif choice == 3:
            print("Thanks for choosing central library. Hope you enjoyed your time.")
            exit()
        else:
            print("Invalid choice entered. Please try again.")

