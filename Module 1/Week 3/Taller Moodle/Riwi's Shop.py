#### INVENTARIO DE LA TIENDA ####
Inventario={}

### MENU INICIAL ###
def main_menu():
    decision_main_menu=0
    while decision_main_menu not in (1,2,3,4,5,6):
        try:
            print("-------->Riwi's Shop<--------")
            print("Que deseas hacer?\n"
                "1. Añadir productos\n"
                "2. Consultar productos\n"
                "3. Actualizar precios\n"
                "4. Eliminar productos\n"
                "5. Calcular el valor total del inventario\n"
                "6. Salir")
            decision_main_menu=int(input())
            if decision_main_menu not in (1,2,3,4,5,6):
                print("Dato no valido")
        except ValueError:
            print("Dato no valido")
    match decision_main_menu:
        case 1:
            add()
            decision_main_menu=0
            main_menu()
        case 2:
            consult()
            decision_main_menu=0
            main_menu()
        case 3:
            update()
            decision_main_menu=0
            main_menu()
        case 4:
            deleted()
            decision_main_menu=0
            main_menu()
        case 5:
            calculate_total()
            decision_main_menu=0
            main_menu()
        case 6:
            print("Muchas gracias por usar nuestros servicios")


## AÑADIR PRODUCTOS ##
def add():
    products_add=0
    while products_add<1:
        try:
            print("---->Añadir<----")
            print("Cuantos productos deseas añadir?")
            products_add=int(input())
            if products_add<1:
                print("Ingresa una cantidad positiva")
        except ValueError:
            print("Dato no valido")
    
    for product in range(products_add):
        price=0
        quantity=0
        price_quantity=[]
        print("Ingrese el nombre del producto: ")
        name=str(input())
        while price<1:
            try:
                print("Ingrese el precio del producto: ")
                price=float(input())
                if price<1:
                    print("Ingresa un valor positivo")
            except ValueError:
                print("Dato no valido")
        price_quantity.append(price)
        while quantity<1:
            try:
                print("Ingrese la cantidad de unidades del producto: ")
                quantity=int(input())
                if quantity<1:
                    print("Ingresa un valor positivo")
            except ValueError:
                print("Dato no valido")
        price_quantity.append(quantity)
        Inventario[name]=price_quantity


## BUSCAR PRODUCTO ESPECIFICO ##
def consult():
    find=False
    print("---->Consultar<----")
    print("Que producto deseas buscar?")
    consult_product=str(input())
    for product in Inventario:
        if consult_product==product:
            find=True
            print(f"Nombre: {product}\n"
                  f"Precio: {Inventario[product][0]}\n"
                  f"Unidades: {Inventario[product][1]}")
            break
    if not find:
        print("El producto no esta en el inventario")


## ACTUALIZAR DATOS SOBRE UN PRODUCTO ##
def update():
    find=False
    print("---->Actualizar<----")
    print("Que producto deseas actualizar?")
    update_product=str(input())
    for product in Inventario:
        if update_product==product:
            find=True
            decision_update=0
            while decision_update not in (1,2):
                try:
                    print("Que dato deseas cambiar?\n"
                        "1. Precio\n"
                        "2. Unidades")
                    decision_update=int(input())
                    if decision_update not in (1,2):
                        print("Dato invalido")
                except ValueError:
                    print("Dato invalido")
            break
    if not find:
        print("El producto no esta en el inventario")
        main_menu()
    
    # MENU SEGUN QUE DATO DESEA ACTUALIZAR #
    match decision_update:
        case 1:
            new_price=0
            while new_price<1:
                try:
                    print("Ingresa el nuevo precio: ")
                    new_price=float(input())
                    if new_price<1:
                        print("ingresa un valor positivo")
                except ValueError:
                    print("Dato invalido")
            for product in Inventario:
                if update_product==product:
                    print(f"Nombre: {update_product}\n"
                          f"Anterior precio: {Inventario[update_product][0]}")
                    Inventario[update_product][0]=new_price
                    print(f"Nuevo precio: {Inventario[update_product][0]}\n"
                          f"Unidades: {Inventario[update_product][1]}")
                    break
        case 2:
            new_quantity=0
            while new_quantity<1:
                try:
                    print("Ingresa la nueva cantidad de unidades: ")
                    new_quantity=int(input())
                    if new_quantity<1:
                        print("Ingresa una cantidad positiva")
                except ValueError:
                    print("Dato invalido")
            for producto in Inventario:
                if update_product==product:
                    print(f"Nombre: {update_product}\n"
                          f"Precio: {Inventario[update_product]}\n"
                          f"Unidades anteriores: {Inventario[update_product][0]}")
                    Inventario[update_product][1]=new_quantity
                    print(f"Unidades actualizadas: {Inventario[update_product][1]}")
                    break


## ELIMINAR UN PRODUCTO ##
def deleted():
    find=False
    while not find:
        print("---->Eliminar<----")
        print("Que producto deseas eliminar?")
        deleted_product=str(input())
        for product in Inventario:
            if deleted_product==product:
                find=True
                confirm_deleted=0
                while confirm_deleted not in (1,2):
                    try:
                        print("Estas seguro que deseas eliminar el producto: "
                            f"Nombre: {product}\n"
                            f"Precio: {Inventario[product][0]}\n"
                            f"Unidades: {Inventario[product][1]}\n"
                            "1. Si\n"
                            "2. No")
                        confirm_deleted=int(input())
                        if confirm_deleted not in (1,2):
                            print("Dato invalido")
                    except ValueError:
                        print("Dato invalido")
                if confirm_deleted==1:
                    del Inventario[deleted_product]
                    print("Producto eliminado exitosamente")
                break
        if not find:
            print("El producto no esta en el inventario")


## CALCULAR VALOR DEL INVENTARIO ##
def calculate_total():
    print("---->Valor Total del Inventario<----")
    if not Inventario:
        print("El inventario está vacío.")
        return
    calcular_valor = lambda precio, cantidad: precio * cantidad
    total = 0
    for producto in Inventario:
        precio, cantidad = Inventario[producto]
        total += calcular_valor(precio, cantidad)
    print(f"El valor total del inventario es: ${total:.2f}")    
    
    
main_menu()