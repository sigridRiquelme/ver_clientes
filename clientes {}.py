clientes = {}

while True: 
    print("\n***GESTION DE CLIENTES***")
    print("1- registrar cliente")
    print("2- consultar cliente")
    print("3- eliminar cliente")
    print("4- salir")

    op = input("ingrese una opcion (1-4): ")

    if op == "1":
        nombre = input("ingrese el nombre completo del cliente: ").strip().lower()
        if nombre in clientes:
            print("El cliente ya se encuentra registrado")
            continue

        while True:
                correo = input("ingrese el correo electronico: ")
                if "@" in correo and "." in correo:
                    break
                else:
                    print("Correo invalido. Intente nuevamente")

        while True: 
            try: 
                edad = int(input("ingrese la edad: "))
                if edad >= 18:
                    break
                else:
                    print("el cliente debe tener 18 años o mas")

            except ValueError:
                print("ingresa un numero entero valido")

        clientes[nombre] = {"correo": correo, "edad": edad}    
        print("cliente ingresado exitosamente")

    elif op == "2":
        nombre = input("ingrese el nombre del cliente a consultar: ").strip().lower() 
        if nombre in clientes:
            cliente = clientes[nombre]
            print(f"Nombre: {nombre}")
            print(f"correo: {cliente["correo"]}")
            print(f"edad: {cliente["edad"]}")     

        else:
            print("el cliente no esta registrado") 

    elif op == "3":
        nombre = input("ingrese el nombre del cliente que desea eliminar: ").strip().lower()
        if nombre in clientes:
            del clientes[nombre]
            print("cliente eliminado exitosamente")

        else:
            print("El cliente no se encuentra registrado")

    elif op == "4":
        print("hasta pronto...")
        break

    else: 
        print("debes ingresar una opcion valida (1-4)")
                


