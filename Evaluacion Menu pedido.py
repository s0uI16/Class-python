#La empresa de chocolate ha creado una promoción de huevitos de chocolate. 
#Cuando el cliente compra más de una caja de 25 unidades de huevos grandes tiene 10% de descuento y 5% las cajas de huevos pequeños.
#Al comprar más de 4 cajas tiene 25% de descuento y 15% en los huevos pequeños.
#Los huevos comprados por unidad no tienen descuento y su precio es $150 los grandes y $100 los pequeños
#Se solicita ingresar la cantidad de cajas o unidades a comprar junto a su tamaño, considerando los siguientes precios:
#Caja de 25 huevos grandes $3000, huevos pequeños $2000 . Entregar el monto a pagar con descuento y sin descuento.

#Cristobal Gomez Moya - Evaluacion

#Total de variables creadas para el trabajo
menu = 1
seleccion = 0
pedido = 0
can_cjaGr = 0
can_cjPe = 0
can_huvPe = 0
can_huvGr = 0
cja_grande = 3000
cja_pequeña = 2000
huv_grande = 150
huv_pequeño = 100
cta_desc = 0
totalCompra = 0
totalCompradesc = 0
totalDesc = 0
desc = 0

#Menu de Bienvenida
print(" B I E N V E N D O")
print("Solo por hoy recuerde que tenemos descuentos en las cajas de huevos de 10% las grandes y 5% las pequeñas")
while menu == 1:

    ## Menu seleccion de pedido cajas o unidades
    print("Que desea comprar Cajas (1) o Unidades (2)")
    pedido = int(input("Elija una opcion: "))
    
    #Diferenciador de seleccion de cajas, para la suma de la cuenta
    if pedido == 1:
        print("Tenemos dos cajas: 1)Grande $3000 o 2)Pequeña $2000")
        seleccion = int(input("Elija una opcion: "))
    
        #Seleccion de Caja Grande
        if seleccion == 1:
            print("Ha seleccionado la caja grande ")
            can_cjaGr = int(input("¿Cuantas cajas desea?: ")) 
            cuenta = can_cjaGr*cja_grande
            desc = (cuenta*10)/100
            cta_desc = (cuenta-desc)
            print("El total de su compra es: ", cuenta, "Con descuento queda en: ", cta_desc)

        #Seleccion de Caja Pequeña
        else:
            print("Ha seleccionado la caja pequeña ")
            can_cjaPe = int(input("¿Cuantas cajas desea?: "))
            cuenta = cja_pequeña * can_cjaPe
            desc = (cuenta*5)/100
            cta_desc = (cuenta-desc)
            print("El total de su compra es: ", cuenta, "Con descuento queda en: ", cta_desc)

    #Diferenciador de seleccion de unidades, para la suma de la cuenta
    else:
        print("Tenemos dos tipos de huevos: 1)Grande $150 o 2)Pequeña $100")
        seleccion = int(input("Elija una opcion: "))

        #Seleccion Unidades Grandes
        if seleccion == 1:
            print("Ha seleccionado los huevos grandes")
            can_huvGr = int(input("¿Cuantos huevos desea?: ")) 
            cuenta = can_huvGr*huv_grande
            print("El total de su compra es: ", cuenta)

        #Seleccion Unidades Pequeñas
        else:
            print("Ha seleccionado la caja pequeña ")
            can_huvPe = int(input("¿Cuantas cajas desea?: "))
            cuenta = can_huvPe*huv_pequeño
            print("El total de su compra es: ", cuenta)
    
    #Suma del total de descuentos, total de compra sin descuento y total de compra con el descuento aplicado
    totalDesc = totalDesc + desc
    totalCompra = cuenta + totalCompra
    totalCompradesc = totalCompra - totalDesc

    #Seleccionador de continuacion de menu para el while, si sigue o no comprando
    print("Desea agregar otra orden: 1)Si 2) No")
    menu=int(input("ingrese opcion: "))             

#Impresion de los datos para el cliente
print("El total de la compra sin descuento es: ", totalCompra, "Los descuentos fueron de: ", totalDesc, "Su cuenta a pagar es de: ", totalCompradesc)
print("Gracias por su compra")