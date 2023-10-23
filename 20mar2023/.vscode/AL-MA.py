while True:
    print("Ingrese su verdadero nombre")
    nombre = input(str)

    if nombre in ["Arcemist", "SoraSilver"]:
        while True:
            print (nombre)
            print ("Ingrese contraseña o ingrese 1 para volver")
            contraseña = input(str)
            if contraseña in ["1"]:
                break
            elif contraseña in ["hola"]:
                print ("Acceso concedido")
                print ("Bienvenido señor",nombre)
                break
            else:
                print ("Acceso denegado")
    elif nombre in ["Gabriel","Lucas","Luka"]:
        while True:
            print ("Ingrese contraseña o ingrese 1 para volver")
            contraseña = input(str)
            if contraseña in ["1"]:
                break
            elif contraseña in ["Elgato1080p"]:
                print ("Acceso concedido")
                print ("Bienvenido",nombre)
                break
            else:
                print ("Acceso denegado")
    else:
        print ("Acceso denegado")