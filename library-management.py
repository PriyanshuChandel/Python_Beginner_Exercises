class Liberary:

    def __init__(self, list_of_books, liberary_name):
        self.list_of_books = list_of_books
        self.liberay_name = liberary_name
        self.lended_book_dict = {}

    def display_book(self):
        print(f"Below are the available books in {self.liberay_name} liberary.")
        for books in self.list_of_books:
             print(books)

    def lend_book(self, user_name, book_name):
        if book_name not in self.lended_book_dict.keys():
            self.lended_book_dict.update({book_name:user_name})
            print("Lender book database updated. you can take book now.")
        else:
            print(f"Book is already taken by {self.lended_book_dict[book_name]}.")

    def add_book(self, new_book):
        self.list_of_books.append(new_book.capitalize())
        print("Book has been added in the list")

    def return_book(self, old_book):
        self.lended_book_dict.pop(old_book)
        print("Book has been returned successfully")

if __name__ == "__main__":
    liberary1 = Liberary(['Python', 'Harry Potter', 'History', 'Math'], "Priyanshu's")
    while (True):
        print(f"Welcome to {liberary1.liberay_name} liberary, Please enter your choice below:\n1.Press 1 to display all available"
              " books.\n2.Press 2 to lend book.\n3.Press 3 to donate book.\n4.Press 4 to return book.")
        user_choice = (input(":"))
        if user_choice == "1":
            liberary1.display_book()
        elif user_choice == "2":
            book_name = input("Enter the name of book you want to lend:\n").capitalize()
            user_name = input("Enter your name:").capitalize()
            liberary1.lend_book(user_name, book_name)
        elif user_choice == "3":
            new_book = input("Enter the name of book you want to add:\n").capitalize()
            liberary1.add_book(new_book)
        elif user_choice == "4":
            old_book = input("Enter the name of book you want to return:\n").capitalize()
            liberary1.return_book(old_book)
        else:
            print("You've entered wrong input, please enter again.")
            # continue
        print("Presss Q to quit and C to continue:")
        user_choice2 = " "
        while(user_choice2 != "Q" and user_choice2 != "C"):
            user_choice2 = input().capitalize()
            if user_choice2 == "Q":
                exit()
            elif user_choice2 == "C":
                continue
            else :
                print("Please enter valid choice:")
                continue
