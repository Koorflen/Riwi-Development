Inventory = [
    {"title": "Book 1", "price": 10.0, "quantity": 100},
    {"title": "Book 2", "price": 15.0, "quantity": 50},
    {"title": "Book 3", "price": 20.0, "quantity": 30},
    {"title": "Book 4", "price": 25.0, "quantity": 10},
    {"title": "Book 5", "price": 30.0, "quantity": 5}
]

def main_menu():
    main_menu_decision=0
    while main_menu_decision not in (1,2,3,4,5,6):
        try:
            print("-------->Riwi's Bookshop<--------")
            print("What do you want to do?\n"
                  "1. Add books to inventory\n"
                  "2. Consult books in the inventory\n"
                  "3. Update book's price\n"
                  "4. Remove books from inventory\n"
                  "5. Calculate inventory's total value\n"
                  "6. Exit")
            main_menu_decision=int(input())
            if main_menu_decision not in (1,2,3,4,5,6):
                print("Invalid Data\n")
        except ValueError:
            print("Invalid Data\n")
            
    match main_menu_decision:
        case 1:
            add()
            main_menu_decision=0
            main_menu()
        case 2:
            consult()
            main_menu_decision=0
            main_menu()
        case 6:
            print("Thank you for using our services")

def add():
    add_books=0
    if len(Inventory)==5:
        while add_books<=5:
            try:
                print("---->Add books<----")
                print("How many books do you want to add?(>5)")
                add_books=int(input())
                if add_books<=5:
                    print("invalid Data\n")
            except ValueError:
                print("invalid Data\n")
                
        for i in range (5):
            
                print("Book's name: ")
                book_name=str(input())
                Inventory[i]["title"]=book_name
                
                book_price=-1
                while book_price<0:
                    try:
                        print("Book's price: ")
                        book_price=float(input())
                        if book_price<0:
                            print("Invalid Data\n")
                    except ValueError:
                        print("Invalid Data\n")
                Inventory[i]["price"]=book_price
                        
                book_quantity=-1
                while book_quantity<0:
                    try:
                        print("Book's quantity: ")
                        book_quantity=int(input())
                        if book_quantity<0:
                            print("Invalid Data\n")
                    except ValueError:
                        print("Invalid Data\n")
                Inventory[i]["quantity"]=book_quantity
            
        extra_books=add_books-5
        for i in range (extra_books):
            new_book={}
            
            print("Book's name: ")
            book_name=str(input())
            new_book["title"]=book_name
            
            book_price=-1
            while book_price<0:
                try:
                    print("Book's price: ")
                    book_price=float(input())
                    if book_price<0:
                        print("Invalid Data\n")
                except ValueError:
                    print("Invalid Data\n")
            new_book["price"]=book_price
                    
            book_quantity=-1
            while book_quantity<1:
                try:
                    print("Book's quantity: ")
                    book_quantity=int(input())
                    if book_quantity<0:
                        print("Invalid Data\n")
                except ValueError:
                    print("Invalid Data\n")
            new_book["quantity"]=book_quantity
            
            Inventory.append(new_book)
        
    else:
        while add_books<1:
            try:
                print("---->Add books<----")
                print("How many books do you want to add?(>5)")
                add_books=int(input())
                if add_books<1:
                    print("invalid Data\n")
            except ValueError:
                print("invalid Data\n")
                
        for i in range (add_books):
            new_book={}
            
            print("Book's name: ")
            book_name=str(input())
            new_book["title"]=book_name
            
            book_price=-1
            while book_price<0:
                try:
                    print("Book's price: ")
                    book_price=float(input())
                    if book_price<0:
                        print("Invalid Data\n")
                except ValueError:
                    print("Invalid Data\n")
            new_book["price"]=book_price
                    
            book_quantity=-1
            while book_quantity<1:
                try:
                    print("Book's quantity: ")
                    book_quantity=int(input())
                    if book_quantity<0:
                        print("Invalid Data\n")
                except ValueError:
                    print("Invalid Data\n")
            new_book["quantity"]=book_quantity
            
            Inventory.append(new_book)
        
def consult():
    print("---->Consult book<----")
    print("what book do you want to search for?")
    consult_book=str(input())
    for book in Inventory:
        if book["title"]==consult_book:
            find=True
            print(f"Title: {book["title"]}\n"
                  f"Price: {book["price"]}\n"
                  f"Quantity: {book["quantity"]}")
            break
        if not find:
            print("Book not found")
            
##Continue in home##
                
main_menu()

