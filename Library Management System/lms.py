import datetime

class LMS:
    """ This class is used to keep a record of the library.
    It has four main functions: "Display Books", "Issue Books", "Return Books", "Add Books" """

    def __init__(self, list_of_books, Library_name):
        self.list_of_books = list_of_books
        self.library_name = Library_name
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
            for line in content:
                self.books_dict.update({str(Id): {"books_title": line.replace("\n", ""),
                                                 "lender_name": "",
                                                 "Issue_date": "",
                                                 "Status": "Available"}})
                Id = Id + 1

    def display_books(self):
        print("--------------------List of Books -----------------")
        print("Book ID", "\t", "Title")
        print("------------------------------")
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"), "-", value.get("Status"))

    def issue_book(self):
        books_id = input("Enter book ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Available":
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} "
                      f"on {self.books_dict[books_id]['Issue_date']}")
            else:
                your_name = input("Enter your name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['Issue_date'] = current_date
                self.books_dict[books_id]['Status'] = "Already Issued"
                print("Book Issued Successfully !!!")
        else:
            print("Book ID not found !!!")

    def add_books(self):
        new_books = input("Enter book title: ")
        if not new_books:
            print("Title cannot be empty.")
        elif len(new_books) > 25:
            print("Book title length is too long. Title length should be 25 characters or less.")
        else:
            with open(self.list_of_books, "a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict)) + 1): {'books_title': new_books,
                                                                             "lender_name": "",
                                                                             "Issue_date": "",
                                                                             "Status": "Available"}})
                print(f"This book '{new_books}' has been added successfully !!!")

    def return_books(self):
        book_id = input("Enter book ID: ")
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]["Status"] == "Available":
                print("This book is already available in the library. Please check your book ID.")
            else:
                self.books_dict[book_id]["lender_name"] = ""
                self.books_dict[book_id]["Issue_date"] = ""
                self.books_dict[book_id]["Status"] = "Available"
                print("Successfully Updated !!!")
        else:
            print("Book ID is not found")

try:
    myLMS = LMS("List_of_books.txt", "Python's Library")
    press_key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books", "R": "Return Books", "Q": "Quit"}
    key_press = None

    while key_press != "q":
        print(f"\n----------- Welcome To {myLMS.library_name} Library Management System -----------\n")
        for key, value in press_key_list.items():
            print(f"Press {key} To {value}")
        key_press = input("Press key: ").lower()
        if key_press == "i":
            print("\nCurrent Selection: Issue Books\n")
            myLMS.issue_book()
        elif key_press == "a":
            print("\nCurrent Selection: Add Book\n")
            myLMS.add_books()
        elif key_press == "d":
            print("\nCurrent Selection: Display Books\n")
            myLMS.display_books()
        elif key_press == "r":
            print("\nCurrent Selection: Return Books\n")
            myLMS.return_books()

except Exception as e:
    print("Something went wrong. Please check your input !!!")
