def crearfacebook():  # Devuelve valor,return
    print("----Se va a crear una cuenta en Facebook ---")  # Se especifica de que se va a crear la cuenta
    # Se van a pedir los datos
    nombreUsuario = str(input("Ingrese el nombre del usuario:"))
    edad = int(input("Ingrese la edad del usuario:"))
    ciudad = str(input("Ingrese la ciudad del usuario:"))
    pais = str(input("Ingrese el país del usuario:"))
    correo = str(input("Ingrese el correo electrónico del usuario:"))
    # Se almacenan los datos en una cadena
    mensaje = ("El nombre del usuario es %s su edad es %d "
               "reside en la ciudad de %s en el país %s, y "
               "su correo electrónico es %s" % (nombreUsuario, edad, ciudad, pais, correo))
    # Retorna la cadena que formamos
    return mensaje


def crearTwitter():  # No devuelve valor
    print("----Se va a crear una cuenta en Twitter ---")  # Se especifica de que se va a crear la cuenta
    # Se van a pedir los datos
    nombreUsuario = str(input("Ingrese el nombre del usuario:"))
    nombre = str(input("Ingrese sus nombres:"))
    apellidos = str(input("Ingrese sus apellidos:"))
    edad = int(input("Ingrese la edad del usuario:"))
    ciudad = str(input("Ingrese la ciudad del usuario:"))
    pais = str(input("Ingrese el país del usuario:"))
    idioma = str(input("Ingrese el idioma de preferencia:"))
    correo = str(input("Ingrese el correo electrónico del usuario:"))
    # Se almacenan los datos en una cadena
    mensaje = ("El nickname del Usuario es %s, sus nombres son %s, con apellidos %s, su edad es %d, reside en la "
               "ciudad de %s en el país %s\n, el lenguaje seleccionado es %s y "
               "el correo electrónico del usuario es: %s"
               % (nombreUsuario, nombre, apellidos, edad, ciudad, pais, idioma, correo))
    # Mostramos en pantalla la cadena que formamos
    print(mensaje)


def crearWhatsapp():  # Devuelve valor,return
    print("----Se va a crear una cuenta en Whatsapp ---")  # Se especifica de que se va a crear la cuenta
    # Se van a pedir los datos
    nombreUsuario = str(input("Ingrese el nombre del usuario:"))
    telefono = int(input("Ingrese el numero de telefono:"))
    edad = int(input("Ingrese la edad del usuario:"))
    ciudad = str(input("Ingrese la ciudad del usuario:"))
    pais = str(input("Ingrese el país del usuario:"))
    # Se almacenan los datos en una cadena
    mensaje = ("El nombre del usuario es %s, el número de telefono del usuario es %d, la edad del usuario es %d "
               "reside en la ciudad de %s en el país %s  " % (nombreUsuario, telefono, edad, ciudad, pais))
    # Retorna la cadena que formamos
    return mensaje


def crearTelegram():  # No devuelve valor
    print("----Se va a crear una cuenta en Telegram ---")  # Se especifica de que se va a crear la cuenta
    # Se van a pedir los datos
    nombreUsuario = str(input("Ingrese el nombre del usuario:"))
    telefono = int(input("Ingrese el numero de telefono:"))
    ciudad = str(input("Ingrese la ciudad del usuario:"))
    pais = str(input("Ingrese el país del usuario:"))
    area = str(input("Ingrese el area de interes del usuario:"))
    # Se almacenan los datos en una cadena
    mensaje = ("El nombre del usuario es %s, el número del usuario es %d, reside en la ciudad de %s en el país de %s y "
               "el área de interes del usuario es %s  " % (nombreUsuario, telefono, ciudad, pais, area))
    # Mostramos en pantalla la cadena que formamos
    print(mensaje)


def crearSignal():  # Devuelve valor,return
    print("----Se va a crear una cuenta en Signal ---")  # Se especifica de que se va a crear la cuenta
    # Se van a pedir los datos
    nombreUsuario = str(input("Ingrese el nombre del usuario:"))
    telefono = int(input("Ingrese el numero de telefono:"))
    ciudad = str(input("Ingrese la ciudad del usuario:"))
    pais = str(input("Ingrese el país del usuario:"))
    hobby = str(input("Ingrese su hobby principal:"))
    # Se almacenan los datos en una cadena
    mensaje = ("El nombre del usuario es %s, su número de telefono es %d, reside en la ciudad de %s, en el país de %s y"
               "su hobby principal es %s  " % (nombreUsuario, telefono, ciudad, pais, hobby))
    # Retorna la cadena que formamos
    return mensaje


def crearInstagram():  # No devuelve valor
    print("----Se va a crear una cuenta en Instagram ---")  # Se especifica de que se va a crear la cuenta
    # Se van a pedir los datos
    nombreUsuario = str(input("Ingrese el nombre del usuario:"))
    ciudad = str(input("Ingrese la ciudad del usuario:"))
    edad = int(input("Ingrese la edad del usuario:"))
    correo = str(input("Ingrese el correo electrónico del usuario:"))
    # Se almacenan los datos en una cadena
    mensaje = ("El nombre del usuario es %s reside en la ciudad de %s y tiene una edad de %d, su correo electronico "
               "es: %s " % (nombreUsuario, ciudad, edad, correo))
    # Mostramos en pantalla la cadena que formamos
    print(mensaje)


def crearFlickr():  # Devuelve valor,return
    print("----Se va a crear una cuenta en Flickr ---")  # Se especifica de que se va a crear la cuenta
    # Se van a pedir los datos
    nombreUsuario = str(input("Ingrese el nombre del usuario:"))
    correo = str(input("Ingrese el correo electrónico del usuario:"))
    # Se almacenan los datos en una cadena
    mensaje = ("El nombre del usuario es %s y su correo electronico es %s " % (nombreUsuario, correo))
    # Retorna la cadena que formamos
    return mensaje


def obtenerMensaje(contador):  # Devuelve valor como return
    mensajeFinal = ["Campaña con poca afluencia",
                    "Campaña moderada siga adelante", "Excelente campaña"]  # Nos dan un arreglo unidimensional
    if contador >= 1 and contador <= 5:  # Si esta entre el 1 y el 5 regresa campaña con poca afluencia
        return (mensajeFinal[0])
    else:
        if contador >= 6 and contador <= 15:  # Si esta entre el 6 y el 15 regresa Campaña moderada siga adelante
            return (mensajeFinal[1])
        else:
            if contador >= 16:  # Si es mayor a 16 regresa  Excelente campaña
                return (mensajeFinal[2])


# Se asignan valores a los datos
condicion = True
contador = 0

while (condicion):  # Comienza un ciclo While
    contador = contador + 1  # El contador aumenta en uno, pero... (Linea 155)

    numero = int(input("Ingrese 1 para crear una cuenta en Facebook\n"  # Se elige la cuenta 
                       "Ingrese 2 para crear una cuenta en Twitter\n"
                       "Ingrese 3 para crear una cuenta en Whatsapp\n"
                       "Ingrese 4 para crear una cuenta en Telegram\n"
                       "Ingrese 5 para crear una cuenta en Signal\n"
                       "Ingrese 6 para crear una cuenta en Instagram\n"
                       "Ingrese 7 para crear una cuenta en Flickr\n"))
    if numero == 1:
        print(crearfacebook())  # Se presenta en pantalla la cadena
    else:
        if numero == 2:
            crearTwitter()
        else:
            if numero == 3:
                print(crearWhatsapp())  # Se presenta en pantalla la cadena
            else:
                if numero == 4:
                    crearTelegram()
                else:
                    if numero == 5:
                        print(crearSignal())  # Se presenta en pantalla la cadena
                    else:
                        if numero == 6:
                            crearInstagram()
                        else:
                            if numero == 7:
                                print(crearFlickr())  # Se presenta en pantalla la cadena
                            else:
                                contador = contador - 1  # Si el numero es distinto, el contador disminuye en 1
                                print("El numero ingresado es incorrecto")

    salida = input("Escribir (si) para salir del proceso o Escriba (no) para seguir con la entrada de datos\n")
    if salida == "si":
        condicion = False  # Fin ciclo While

print(obtenerMensaje(contador))  # Se presenta en pantalla la una cadena
