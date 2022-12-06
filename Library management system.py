class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
            print(f"\n {len(self.books)} AVAILABLE BOOKS ARE.")
            for book in self.books:
                print("♦--" + book)
            print("\n")

    def borrowBook(self, name, bookname):
        if bookname not in self.books:
                print(f"{bookname} BOOK IS NOT AVAILABLE EITHER TAKEN BY SOMEONE ELSE, WAIT UNTIL HE RETURNED . \n")
        else:
                track.append({name: bookname})
                print("BOOK ISSUED : THANK YOU KEEP IT WITH CARE AND RETURN IT ON TIME")
                self.books.remove(bookname)

    def returnbook(self, bookname):
            print("BOOK RETURNED : THANK YOU \n")
            self.books.append(bookname)

    def donateBook(self, bookname):
        print("BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD.\n")
        self.books.append(bookname)



class Student():
    def requestBook(self):
        print("So, you want to borrow book!")
        self.book = input("Enter te name of the book you want to borrow:")
        return self.book

    def returnBook(self):
        print("So, you want to return book!")
        name = input("Enter your name:")
        self.book  = input("Enter the name of the book you want to return:")
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book

    def donateBook(self):
        print("Okay, You want to donate book")
        self.book = input("Enter the name of the book you want to donate")
        return self.book


if __name__ == "__main__":
    PersonalLibrary = Library(["We were liars", "Mindset", "Sapiens", "I too had a love story", "Can love happen twice?"])

    student = Student()
    track = []

    print("\t\t\t\t\t\t\t♦♦♦♦♦♦♦ WELCOME TO MY PERSONAL LIBRARY ♦♦♦♦♦♦♦\n")
    print("""
                CHOOSE WHAT YOU WANT TO DO:-\n
                1. List of all books\n
                2. Borrow books\n
                3. Return books\n
                4. Donate books\n
                5. Track books\n
                6. exit the library\n
        """)

    while(True):
        # Print(track)
        try:
            usr_response = int(input("Enter your choice:"))

            if usr_response == 1: # listing
                PersonalLibrary.displayAvailableBooks()
            elif usr_response == 2: # borrow
                PersonalLibrary.borrowBook(
                    input("Enter your name:"), student.requestBook()
                )

            elif usr_response == 3: # return
                PersonalLibrary.returnbook(
                    student.returnBook()
                )

            elif usr_response == 4: #donate
                PersonalLibrary.donateBook(
                    student.donateBook()
                )

            elif usr_response == 5: #track book
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} book is taken/ issued by {holder}.")
                    print("\n")
                    if len(track) == 0:
                        print("NO BOOKS ARE ISSUED. \n")

            elif usr_response == 6: # exit
                print("THANK YOU! \n")
                exit()
            else:
                print("INVALID INPUT! \n")

        except Exception as e: # catch error
            print(f"{e}-----> INVALID INPUT! \n")







