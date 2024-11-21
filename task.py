# library management 

import time
class library:
    def __init__(self):
        self.book=[]
        self.borrow=[]
        
    def addbook(self,title):
        self.book.append(title)
    def removebook(self,bookname):
        if bookname in self.book:
            self.book.remove(bookname)
        else:
            print('book is not in the library')
    
    def borrowbook(self,borrow):
        if borrow in self.book:
            self.book.remove(borrow)
            self.borrow.append(borrow)
            print(f'you have sucessfully borrowed {borrow} in {time.ctime()}')  #imported time 
        else:
            print('book is not in the library')
    

    def returnbook(self,returnbook):
        if returnbook in self.borrow:
            self.book.append(returnbook)
            self.borrow.remove(returnbook)
            print(f'you have returned {returnbook} in {time.ctime()}')
    

def displaybook():
    print(f' Available books are {c1.book}')


# c1=library()
# c1.addbook('book of thow')
# c1.addbook('book of calf')
# c1.addbook('book of moon')
# c1.addbook('book of thiller')
# c1.addbook('book of mankind')
# # c1.removebook('book of thow')
# c1.borrowbook('book of calf')
# # c1.returnbook('book of calf')

# displaybook()

if __name__ == "__main__":
     c1=library()

while True:
        print("\nLibrary Management System")
        print("1. View Available Books")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            displaybook()
        elif choice == "2":
            book_name = input("Enter the book name: ")
            c1.addbook(book_name)
        elif choice == "3":
            book_name = input("Enter the book name you want to borrow: ")
            c1.borrowbook(book_name)
        # elif choice == "4":
        #     book_name = input("Enter the book name you want to return: ")
        #     library.return_book(book_name)
        # elif choice == "5":
        #     print("Thank you for using the Library Management System. Goodbye!")
        #     break
        else:
            print("Invalid choice! Please try again.")