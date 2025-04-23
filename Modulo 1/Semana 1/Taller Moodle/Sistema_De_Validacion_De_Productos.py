#DECLARACION DE DICCIONARIOS Y LISTAS
nombre_y_precio={}
precio_y_cantidad={}
nombre_productos=[]
precio_productos=[]
numero_de_productos=[]

#INICIO
print("---Bienvenido a SuperRiwi---")
try:
    cantidad_productos=int(input("Cuantos productos deseas adquirir?\n"))
except:
    print("Ingresa un valor numerico")
    
#VALIDACION DE QUE INGRESE UN NUMERO NATURAL O CERO
if cantidad_productos<0:
    
    while cantidad_productos<0:
        try:
            cantidad_productos=int(input("Porfavor ingresa una cantidad mayor o igual a cero\n"))
        except:
            print("Ingresa un valor numerico")

elif cantidad_productos>0:
    
    #BUCLE PARA LEER TODOS LOS PRODUCTOS, SU PRECIO, Y LA CANTIDAD QUE DESEE LLEVAR
    for i in range(cantidad_productos):
        
        nombre=str(input("Ingresa el nombre del producto\n")).lower()
        
        try:
            precio=float(input("Ingresa el precio del producto\n"))
        except:
            print("Ingresa un valor numerico")
        
        #VALIDACION DE QUE PUSO UN PRECIO NO NEGATIVO
        if precio<0:
        
            while precio<0:
                precio=float(input("Ingresa un precio mayor o igual a cero\n"))
        
        cantidad_del_producto=int(input(f"Cuantos {nombre} deseas adquirir?\n"))
        
        #VALIDACION DE QUE PUSO UNA CANTIDAD DE PRODUCTO NO NEGATIVA
        if cantidad_del_producto<=0:
            
            while cantidad_del_producto<=0:
                cantidad_del_producto=int(input(f"Ingresa una cantidad positiva\n"))

        #SE AGREGAN LOS DATOS RECOLECTADOS A LOS DICCIONARIOS Y LAS LISTAS
        nombre_y_precio[nombre]=precio
        precio_y_cantidad[precio]=cantidad_del_producto
        nombre_productos.append(nombre)
        precio_productos.append(precio)
        numero_de_productos.append(cantidad_del_producto)
    
    descuento=str(input("Tienes algun descuento?(si/no)\n")).lower()
    
    #PROCESO SI HAY DESCUENTO
    if descuento=="si":
        
        cantidad_descuento=float(input("De cuanto es tu descuento?\n"))
        
        #VALIDACION DE QUE SE PUSO UN PORCENTAJE DE DESCUENTO ENTRE 0 Y 100
        while cantidad_descuento<0 or cantidad_del_producto>100:
            cantidad_descuento=float(input("Porfavor ingresa una cantidad entre 0 y 100\n"))
    
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
    print(f"Total Final:_____________________{(precio_total*cantidad_descuento/100):.2f}")