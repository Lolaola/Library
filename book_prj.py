list_of_books = []


def add_book():
    book_name = str(input("Enter book name to add: "))
    list_of_books.append(book_name)
    print("Book is successfully added: "+ book_name)


def del_book():
    book_name = str(input("Enter book name to delete: "))
    is_book_exist = list_of_books.__contains__(book_name)
    if is_book_exist:
        list_of_books.remove(book_name)
        print("Book is successfully deleted: "+ book_name)
    else:
        print("There's no such book: "+ book_name)


def count_book():
    print("Book count: " + str(len(list_of_books)))
    print(list_of_books)

def sort_book():
    print("Book is sorted: "+ str(sorted(list_of_books)))


print("This is a library.You can add the book name, delete it or count book amount.")
while True:
    print("What action would you like to do?")
    print("Enter 'a' to add the book")
    print("Enter 'd' to delete the book")
    print("Enter 'c' to count total book amount")
    print("Enter 's' to sort the book")
    print("Enter 'q' to quit the program")

    action = str(input("Make your choice: "))
    if action == 'a':
        add_book()
    elif action == 'd':
        del_book()
    elif action =='c':
        count_book()
    elif action == 's':
        sort_book()
    elif action =='q':
        break
    else:
        print("You entered wrong value: " + action)
    print("")
print("The program is successfully finished!")