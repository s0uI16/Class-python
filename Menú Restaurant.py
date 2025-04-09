## Un restaurante ofrece a sus clientes diferentes menús, cada uno con un precio y un conteo de calorías.
## Se solicita un programa que, al seleccionar uno o más platos del menú, indique el conteo de calorías y el monto a pagar.
## El programa también debe indicar el promedio de calorías por plato y el promedio de precio por plato.
## Además, el programa debe indicar el total de calorías y el monto total a pagar.

opcion = 0
precio = 0
calorias = 0
continuar = 1
precio_total = 0
calorias_total = 0 
print ( " M E N U " )
print("1.- Bebida individual")
print("2.- Cerveza")
print("3.- Empanada de pino")
print("4.- Arroz con pollo")
print("5.- Arroz con carne")

while continuar == 1:
    opcion= int(input("Seleccione una opción del menú: "))
    if opcion == 1:
        precio = 1000
        calorias = 200
        print("Bebida individual seleccionada")
    elif opcion == 2:
        precio = 1500
        calorias = 300
        print("Cerveza seleccionada")
    elif opcion == 3:
        precio = 2000
        calorias = 400
        print("Empanada de pino seleccionada")
    elif opcion == 4:
        precio = 2500
        calorias = 500
        print("Arroz con pollo seleccionado")
    elif opcion == 5:
        precio = 3000
        calorias = 600
        print("Arroz con carne seleccionado")
    else:
        print("Opción no válida")
    
    print ("Su menu seleccionado es: ", opcion)
    precio_total = precio_total + precio
    calorias_total = calorias_total + calorias
    continuar = int(input("Desea seleccionar otro plato? (1: Si, 0: No)"))
print("El precio total es: ", precio_total)
print("El total de calorias es: ", calorias_total)
