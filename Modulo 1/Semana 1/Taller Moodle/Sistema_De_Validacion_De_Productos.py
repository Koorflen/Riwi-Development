#DECLARACION DE DICCIONARIOS Y LISTAS
nombre_y_precio={}
precio_y_cantidad={}
nombre_productos=[]
precio_productos=[]
numero_de_productos=[]

#INICIO
print("---Bienvenido a SuperRiwi---")

#LECTURA DE CUANTOS PRODUCTOS LLEVARA
while True:    
    try:
        cantidad_productos = int(input("¿Cuántos productos deseas adquirir?\n"))
        if cantidad_productos < 0:
            print("Por favor, ingresa una cantidad mayor o igual a cero.")
        else:
            break
    except ValueError:
        print("Por favor, ingresa un valor numérico válido.")


if cantidad_productos>0:
    
    #BUCLE PARA LEER TODOS LOS PRODUCTOS, SU PRECIO, Y LA CANTIDAD QUE DESEE LLEVAR
    for i in range(cantidad_productos):
        
        nombre=str(input("Ingresa el nombre del producto\n")).lower()
        print("Ingresa el precio del producto:")
        
        while True:
            try:
                precio = float(input())
                if precio < 0:
                    print("Ingresa un precio mayor o igual a cero.")
                else:
                    break  
            except ValueError:
                print("Ingresa un valor numérico válido.")

        print(f"Cuantos {nombre} deseas adquirir?")
        
        while True:
            try:
                cantidad_del_producto=int(input())
                if cantidad_del_producto<=0:
                    print("Ingresa una cantidad positiva\n")
                else:
                    break
            except ValueError:
                print("Ingresa un valor numérico válido.")

        #SE AGREGAN LOS DATOS RECOLECTADOS A LOS DICCIONARIOS Y LAS LISTAS
        nombre_y_precio[nombre]=precio
        precio_y_cantidad[precio]=cantidad_del_producto
        nombre_productos.append(nombre)
        precio_productos.append(precio)
        numero_de_productos.append(cantidad_del_producto)
    
    descuento=str(input("Tienes algun descuento?(si/no)\n")).lower()
    
    #PROCESO SI HAY DESCUENTO
    if descuento=="si":
        print("De cuanto es tu descuento?")
        while True:
            try:
                cantidad_descuento=float(input())
                if cantidad_descuento<0 or cantidad_del_producto>100:
                    print("Porfavor ingresa una cantidad entre 0 y 100")
                else:
                    break
            except ValueError:
                print("Ingresa un valor numérico válido.")
precio_total=0
print("-----LISTA DE PRODUCTOS-----")

#BUCLE QUE ME ESCRIBE PRODUCTO, PRECIO, CANTIDAD, Y CANTIDAD TOTAL POR PRODUCTO
for i in range (cantidad_productos):
    print(f"{nombre_productos[i]}____${precio_productos[i]:.2f}____x{numero_de_productos[i]}____${(precio_productos[i])*(numero_de_productos[i]):.2f}")
    precio_total+=(precio_productos[i])*(numero_de_productos[i])

print(f"Total:_____________________{precio_total:.2f}")

#APLICADOR DE DESCUENTO
if descuento=="si":
    print(f"Porcentaje de Descuento:____{cantidad_descuento}%")
    print(f"Total Final:_____________________{(precio_total)-(precio_total*cantidad_descuento/100):.2f}")