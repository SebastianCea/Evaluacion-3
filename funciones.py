import config , random , csv

def menu():
    num_opcion = 1
    for opc in config.lista_menu:
        print(f"{num_opcion}. {opc}")
        num_opcion += 1
        while True:
            try:
                seleccion = int(input("Opción: "))
                break
            except:
                print("Debe ingresar un número válido")
        return seleccion   
                        
                
def registrar_pedido (lista):
    while True:
        id_cliente = codigo_cliente()
        cliente = input("Ingresa tu nombre y apellido: ")
        direccion = input("Ingresa tu dirección: ")
        sector = input("Ciudad/Comuna: ")
        disp_6lts = int(input("Cantidad de 6 litros: "))
        disp_10lts = int(input("Cantidad 10 litros: "))
        disp_20lts = int(input("Cantidad 20 litros: "))
        
        lista.append ([id_cliente , cliente, direccion , sector , disp_6lts , disp_10lts , disp_20lts])
        break

def codigo_cliente ():
    numero = random.randint (100000 , 999999)
    return numero

def listar_pedidos (lista):
    print("ID cliente\tCliente\tDirección\tSector\tDisp.6\tDisp.10\tDisp.20")
    for opc in lista:
        print(f"{opc[0]}\t{opc[1]}\t{opc[2]}\t{opc[3]}\t{opc[4]}\t{opc[5]}\t{opc[6]}")

def hoja_ruta (lista, opc):
    try:
        with open("dato.csv", "w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["ID cliente", "Cliente", "Dirección", "Sector", "Disp.6", "Disp.10", "Disp.20"])
            for opc in lista:
                if opc[3] == "Concepción":
                    escritor.writerow(opc)
                    
                if opc[3] == "Chiguayante":
                    escritor.writerow(opc)
                    
                if opc[3] == "Talcahuano":
                    escritor.writerow(opc)

                if opc[3] == "Hualpen":
                    escritor.writerow(opc)

                if opc[3] == "San Pedro":
                    escritor.writerow(opc)
                    
                if opc[3] == "Todos":
                    escritor.writerows(opc)
    except:
        print("Opción inválida, intente de nuevo")    

def buscar_id (lista , id_cliente):
    print("ID cliente\tCliente\tDirección\tSector\tDisp.6\tDisp.10\tDisp.20")
    for opc in lista:
        if id_cliente == opc[0]:
            print(f"{opc[0]}\t{opc[1]}\t{opc[2]}\t{opc[3]}\t{opc[4]}\t{opc[5]}\t{opc[6]}")

           

