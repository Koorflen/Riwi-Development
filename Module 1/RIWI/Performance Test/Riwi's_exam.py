#######README#######
#The way I analyzed how to develop this code was: first, create an inventory, which would be a list. This list would contain all the products.
#Each product would be a dictionary. The dictionary has three keys: 'name', 'price', and 'quantity', which correspond to the name, price, and quantity, respectively.
#After this, I created an initial menu where the user decides what to do.

#Main Menu: This contains the options to add, query, update, remove, and calculate total value.

#Add: When adding products for the first time, the user must add a quantity greater than 5 products.
#The first 5 products overwrite the 5 drafts that were in the list. From then on, they are added as new dictionaries.
# However, if the user is not adding for the first time, meaning they have already added, the first 5 are not overwritten; they only add new ones.

#Consult: Since the minimum quantity is 6 products in the inventory, it is first verified if the inventory has the 5 products that were in the draft.
#If so, then it is redirected to the main menu and is told that no products have been added for consultation.
#If the inventory already has products, this function requests the name of the product to search for.
# It is searched for in the inventory and if found, its information is displayed (name, price, quantity).
# If not found, it is redirected to the main menu and displays the message that the product is not in the inventory.

#Update: This checks if the inventory has products in the same way as in the 'consult' function.
#After confirming that the inventory has products, you are asked for the name of the product you wish to update.
#This product is searched for in the inventory.
#If it is not found, you are redirected to the main menu and a message is displayed indicating that the product is not in the inventory.
#If the product is found, you are asked what information you wish to update (price/quantity).
#After selecting the product, the new information is requested, and then the product information is displayed, showing both its previous information and the updated information.

#Remove: This checks the quantity of products in the inventory. If there are 5, you are redirected to the main menu and told that no products have been added.
#If there are 6, you are redirected to the main menu and told that you cannot have fewer than 6 products.
#If products can be removed from the inventory, you will be asked for the name of the product you wish to remove.
#This will be searched for in the inventory. If it is not found, you will be redirected to the main menu and told that this product is not in the inventory.
#If the product is found, the product information will be displayed and confirmation will be requested to remove it.
#If the confirmation is affirmative, the product will be removed from the inventory and a message will be displayed indicating that the process was successful.
#If the confirmation is negative, you will be redirected to the main menu.

#Calculate total value: This will confirm whether the inventory has products.
#If it does not have products, you will be redirected to the main menu and told that no products have been entered yet.
#If the inventory has products, you will be asked what you want to calculate: the total value of a product or the total value of the inventory.
#If you want to consult the total value of a product, you ask which product you want the calculation to be done for, it looks to see if it is in the inventory,
#if it is not, you are redirected to the main menu and you are told that this product is not in the inventory,
#if it is found, the data of this product and the calculation of the total value are shown.
#If you want to consult the calculation of the total value of the inventory, you begin to go through the entire inventory and the total value of each product is saved in a variable.
#After going through the entire list, a message with the total value of the inventory is printed.




####INVENTORY####
Inventory = [
    {"name": "product", "price": 1.0, "quantity": 1},
    {"name": "product", "price": 1.0, "quantity": 1},
    {"name": "product", "price": 1.0, "quantity": 1},
    {"name": "product", "price": 1.0, "quantity": 1},
    {"name": "product", "price": 1.0, "quantity": 1}
]
###MAIN MENU###
def main_menu():
    main_menu_decision=0
    ##VALIDATION OF THE MAIN MENU DECISION##
    while main_menu_decision not in (1,2,3,4,5,6):
        try:
            print("-------->Riwi's Supermarket<--------")
            print("What do you want to do?\n"
                "1. Add products to inventory\n"
                "2. Consult products in the inventory\n"
                "3. Update product's price\n"
                "4. Remove products from inventory\n"
                "5. Calculate inventory's total value\n"
                "6. Exit")
            main_menu_decision=int(input())
            if main_menu_decision not in (1,2,3,4,5,6):
                print("Invalid Data\n")
        except ValueError:
            print("Invalid Data\n")
    ##SUB-MENUS##
    match main_menu_decision:
        case 1:
            add_products()
            main_menu()
        case 2:
            consult_products()
            main_menu()
        case 3:
            update_products()
            main_menu()
        case 4:
            remove_product()
            main_menu()
        case 5:
            calculate_total_value()
            main_menu()
        case 6:
            print("Thank you for using our services")

###SUB-MENU FOR ADD PRODUCTS###
def add_products():
    products_to_add=0
    ##IF TEH INVENTORY HAS FIVE PRODUCTS, THE USER WILL BE PROMPTED TO ADD MORE THAN FIVE PRODUCTS, OVERWRITING THE FIRST FIVE AND ADDING THE REST##
    if len(Inventory)==5:
        #VALIDATE HOW MANY YOU WANT TO ADD#
        while products_to_add<=5:
            try:
                print("---->Add products<----")
                print("How many products do you want to add?(>5)")
                products_to_add=int(input())
                if products_to_add<=5:
                    print("Invalid Data\n")
            except ValueError:
                print("Invalid Data\n")
        #OVERWRITING THE FIRST FIVE#
        for first_five_products in range (5):
            print(f"Product {first_five_products+1}:\n"
                  "Product's name: ")
            product_name=str(input())
            Inventory[first_five_products]["name"]=product_name
            product_price=-1
            while product_price<0:
                try:
                    print("Product's price: ")
                    product_price=float(input("$"))
                    if product_price<0:
                        print("Invalid Data\n")
                except ValueError:
                    print("Invalid Data\n")
            Inventory[first_five_products]["price"]=product_price
            product_quantity=-1
            while product_quantity<0:
                try:
                    print("Product's quantity: ")
                    product_quantity=int(input())
                    if product_quantity<0:
                        print("Invalid Data\n")
                except ValueError:
                    print("Invalid Data\n")
            Inventory[first_five_products]["quantity"]=product_quantity
        #ADD THE REST#
        extra_products=products_to_add-5
        for other_products in range (extra_products):
            new_product={}
            print(f"Product {other_products+6}:\n"
                  "Product's name: ")
            product_name=str(input())
            new_product["name"]=product_name
            product_price=-1
            while product_price<0:
                try:
                    print("Product's price: ")
                    product_price=float(input("$"))
                    if product_price<0:
                        print("Invalid Data\n")
                except ValueError:
                    print("Invalid Data\n")
            new_product["price"]=product_price
            product_quantity=-1
            while product_quantity<1:
                try:
                    print("Product's quantity: ")
                    product_quantity=int(input())
                    if product_quantity<0:
                        print("Invalid Data\n")
                except ValueError:
                    print("Invalid Data\n")
            new_product["quantity"]=product_quantity
            Inventory.append(new_product)
    ##IF THE INVENTORY HAS MORE THAN 5 PRODUCTS, THAT IS, HE HAD PREVIOUSLY ADDED PRODUCTS FOR THE FIRST TIME, THEREFORE THE FIRST FIVE HAVE ALREADY BEEN OVERWRITTEN##
    else:
        while products_to_add<1:
            try:
                print("---->Add products<----")
                print("How many products do you want to add?")
                products_to_add=int(input())
            except ValueError:
                print("Invalid Data\n")
        #ADD THE NEW PRODUCTS#
        for product in range (products_to_add):
            new_product={}
            print(f"Product {product+1}\n"
                  "Product's name: ")
            product_name=str(input())
            new_product["title"]=product_name
            product_price=-1
            while product_price<0:
                try:
                    print("Product's price: ")
                    product_price=float(input("$"))
                    if product_price<0:
                        print("Invalid Data\n")
                except ValueError:
                    print("Invalid Data\n")
            new_product["price"]=product_price
            product_quantity=-1
            while product_quantity<1:
                try:
                    print("Product's quantity: ")
                    product_quantity=int(input())
                    if product_quantity<0:
                        print("Invalid Data\n")
                except ValueError:
                    print("Invalid Data\n")
            new_product["quantity"]=product_quantity
            Inventory.append(new_product)
            
###SUB-MENU FOR CONSULT###
def consult_products():
    ##IF THE INVENTORY HAS 5 PRODUCTS, YOU MEAN THAT THE FIRST 5 HAVE NOT BEEN OVERWRITTEN, THEREFORE NO PRODUCTS HAVE BEEN ADDED##
    if len(Inventory)==5:
        print("You haven't added any products to your inventory\n")
    ##IF THERE ARE MORE THAN 5 PRODUCTS, PRODUCTS HAVE ALREADY BEEN ADDED##
    else:
        find=False
        print("---->Consult product<----")
        print("what product do you want to search for?")
        consult_product=str(input())
        for product in Inventory:
            if product["name"]==consult_product:
                find=True
                print(f"Name: {product["name"]}\n"
                      f"Price: ${product["price"]:.2f}\n"
                      f"Quantity: {product["quantity"]}\n")
                break
        if not find:
            print("Product not found\n")
        
###SUB-MENU FOR UPDATE PRODUCTS###
def update_products():
    ##CONFIRM IF PRODUCTS HAVE BEEN ADDED##
    if len(Inventory)==5:
        print("You haven't added any products to your inventory\n")
    ##SEARCH FOR THE PRODUCT YOU WANT TO UPDATE##
    else:
        find=False
        print("---->Update product<----")
        print("Which product do you want to update?")
        update_product=str(input())
        for product in Inventory:
            if update_product==product["name"]:
                find=True
                decision_update=0
                #VALIDATE THAT YOU WANT TO UPDATE#
                while decision_update not in (1,2):
                    try:
                        print("What information do you want to change?\n"
                              "1. Price\n"
                              "2. Quantity")
                        decision_update=int(input())
                        if decision_update not in (1,2):
                            print("Invalid Data\n")
                    except ValueError:
                        print("Invalid Data\n")
                break
        if not find:
            print("Product not found\n")
            main_menu()
        ##SUB-SUB-MENU FOR WHAT YOU WANT TO UPDATE##
        match decision_update:
            #FOR UPDATE PRICE#
            case 1:
                new_price=0
                while new_price<1:
                
                    try:
                        print("Enter the new product's price: ")
                        new_price=float(input())
                        if new_price<1:
                            print("Enter a positive value\n")
                    except ValueError:
                        print("Invalid Data\”")
                for product in Inventory:
                    if update_product==product["name"]:
                        print(f"Name: {update_product}\n"
                              f"Previous price: {product["price"]:.2f}")
                        product["price"]=new_price
                        print(f"New price: {product["price"]:.2f}\n"
                              f"quantity: {product["quantity"]}\n")
                        break
            #FOR UPDATE QUANTITY#
            case 2:
                new_quantity=0
                while new_quantity<1:
                    try:
                        print("Enter de new product's quantity: ")
                        new_quantity=int(input())
                        if new_quantity<1:
                            print("Enter positive value\”")
                    except ValueError:
                        print("Invalid Data\n")
                for producto in Inventory:
                    if update_product==product["name"]:
                        print(f"Name: {update_product}\n"
                              f"Price: {product["price"]:.2f}\n"
                              f"Previuos quantity: {product["quantity"]}")
                        product["quantity"]=new_quantity
                        print(f"New quantity: {product["quantity"]}\n")
                        break
                
###SUB-MENU FOR REMOVE PRODUCTS###
def remove_product():
    ##IT IS NOT ALLOWED TO HAVE LESS THAN 6 PRODUCTS##
    if len(Inventory)==6:
        print("You can't have less than 6 products in inventory\n")
    ##CONFIRM IF PRODUCTS HAVE BEEN ADDED##
    elif len(Inventory)==5:
        print("You haven't added any products to your inventory\n")
    else:
        #VALIDATE AND CONFIRM IF THE PRODUCT YOU WANT TO DELETE EXISTS#
        find=False
        print("---->Remove product<----")
        print("Which product do you want to delete?")
        deleted_product=str(input())
        count=0
        for product in Inventory:
            if deleted_product==product["name"]:
                find=True
                confirmed_deleted=0
                #CONFIRMATION TO DELETE#
                while confirmed_deleted not in (1,2):
                    try:
                        print("Are you sure you want to delete this product?")
                        print(f"Name: {product["name"]}\n"
                            f"Price: ${product["price"]:.2f}\n"
                            f"Quantity: {product["quantity"]}\n"
                            "1. Yes\n"
                            "2. No")
                        confirmed_deleted=int(input())
                        if confirmed_deleted not in (1,2):
                            print("Invalid Data\n")
                    except ValueError:
                        print("Invalid Data\n")
                if confirmed_deleted==1:
                    del Inventory[count]
                    print("product successfully removed\n")
                break
            count+=1
        if not find:
            print("Product not found\n")

###SUB-MENU FOR CALCULATE THE TOTAL VALUE OF THE INVENTORY###
def calculate_total_value():
    ##CONFIRM IF PRODUCTS HAVE BEEN ADDED##
    if len(Inventory)==5:
        print("You haven't added any products to your inventory\n")
    else:
        decision_calculate=0
        while decision_calculate not in (1,2):
            try:
                print("---->Inventory's Total Value<----")
                print("what do you want to calculate?\n"
                    "1. Total value of a product\n"
                    "2. Total inventory value")
                decision_calculate=int(input())
                if decision_calculate not in (1,2):
                    print("Invalid Data\n")
            except ValueError:
                print("Invalid Data\n")
        match decision_calculate:
            case 1:
                find=False
                print("Which product do you want to calculate the total price for?")
                product_calculate=str(input())
                for product in Inventory:
                    if product["name"]==product_calculate:
                        find=True
                        price=product["price"]
                        quantity=product["quantity"]
                        product_total_value=price*quantity
                        print(f"Name: {product["name"]}\n"
                              f"Price: ${product["price"]:.2f}\n"
                              f"Quantity: {product["quantity"]}\n"
                              f"Product's total value:________${product_total_value:.2f}")
                        break
                if not find:
                    print("Product not found")
            case 2:
                total_value=0
                for product in Inventory:
                    price=product["price"]
                    quantity=product["quantity"]
                    total_value+=(price*quantity)
                    print(f"Name:__________{product["name"]}\n"
                          f"Price:_________${product["price"]:.2f}\n"
                          f"Quantity:______{product["quantity"]}")
                print(f"Inventory's Total Value :________${total_value:.2f}\n")
        
        
main_menu()