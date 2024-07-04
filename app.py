import funciones

lista=[]

while True:
    opcion = funciones.menu()

    if opcion == 1:
        funciones.registrar_pedido(lista)
    
    elif opcion == 2:
        funciones.listar_pedidos(lista)
       

    elif opcion == 3:
        opc = input("Ingrese ciudad o comuna: ")
        funciones.hoja_ruta(lista,opc)


    elif opcion == 4:
        id_cliente = input("Ingresa tu ID: ")
        funciones.buscar_id(lista , id_cliente)

    elif opcion == 5:
        break

    else:
        print("Opción no válida")