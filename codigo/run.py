
def crearfacebook():
    print("----Se va a crear una cuenta en Facebook ---")
    nombreUsuario = str(input("Ingrese el nombre del usuario:"))
    edad = int(input("Ingrese la edad del usuario:"))
    ciudad = str(input("Ingrese la ciudad del usuario:"))
    pais = str(input("Ingrese el país del usuario:"))
    correo = str(input("Ingrese el correo electrónico del usuario:"))
    mensaje = ("El nombre del usuario es %s su edad es %d "
               "reside en la ciudad de %s en el país %s, y "
               "su correo electrónico es %s" % (nombreUsuario, edad, ciudad, pais, correo))
    return mensaje

def crearTwitter():
    print("----Se va a crear una cuenta en Twitter ---")
    nombreUsuario = str(input("Ingrese el nombre del usuario:"))
    nombre = str(input("Ingrese sus nombres:"))
    apellidos = str(input("Ingrese sus apellidos:"))
    edad = int(input("Ingrese la edad del usuario:"))
    ciudad = str(input("Ingrese la ciudad del usuario:"))
    pais = str(input("Ingrese el país del usuario:"))
    idioma = str(input("Ingrese el idioma de preferencia:"))
    correo = str(input("Ingrese el correo electrónico del usuario:"))
    mensaje = ("El nickname del Usuario es %s, sus nombres son %s, con apellidos %s, su edad es %d, reside en la "
                  "ciudad de %s en el país %s\n, el lenguaje seleccionado es %s y "
               "el correo electrónico del usuario es: %s"
                  % (nombreUsuario, nombre, apellidos, edad, ciudad, pais, idioma, correo))

    print(mensaje)

def crearWhatsapp():
    print("----Se va a crear una cuenta en Whatsapp ---")
    nombreUsuario = str(input("Ingrese el nombre del usuario:"))
    telefono = int(input("Ingrese el numero de telefono:"))
    edad = int(input("Ingrese la edad del usuario:"))
    ciudad = str(input("Ingrese la ciudad del usuario:"))
    pais = str(input("Ingrese el país del usuario:"))
    mensaje = ("El nombre del usuario es %s, el número de telefono del usuario es %d, la edad del usuario es %d "
               "reside en la ciudad de %s en el país %s  " % (nombreUsuario, telefono, edad, ciudad, pais))
    return mensaje

def crearTelegram():
    print("----Se va a crear una cuenta en Telegram ---")
    nombreUsuario = str(input("Ingrese el nombre del usuario:"))
    telefono = int(input("Ingrese el numero de telefono:"))
    ciudad = str(input("Ingrese la ciudad del usuario:"))
    pais = str(input("Ingrese el país del usuario:"))
    area = str(input("Ingrese el area de interes del usuario:"))
    mensaje = ("El nombre del usuario es %s, el número del usuario es %d, reside en la ciudad de %s en el país de %s y "
               "el área de interes del usuario es %s  " % (nombreUsuario, telefono, ciudad, pais, area))
    print(mensaje)

def crearSignal():
    print("----Se va a crear una cuenta en Signal ---")
    nombreUsuario = str(input("Ingrese el nombre del usuario:"))
    telefono = int(input("Ingrese el numero de telefono:"))
    ciudad = str(input("Ingrese la ciudad del usuario:"))
    pais = str(input("Ingrese el país del usuario:"))
    hobby = str(input("Ingrese su hobby principal:"))
    mensaje = ("El nombre del usuario es %s, su número de telefono es %d, reside en la ciudad de %s, en el país de %s y"
               "su hobby principal es %s  " % (nombreUsuario, telefono, ciudad, pais, hobby))
    return mensaje

def crearInstagram():
    print("----Se va a crear una cuenta en Instagram ---")
    nombreUsuario = str(input("Ingrese el nombre del usuario:"))
    ciudad = str(input("Ingrese la ciudad del usuario:"))
    edad = int(input("Ingrese la edad del usuario:"))
    correo = str(input("Ingrese el correo electrónico del usuario:"))
    mensaje = ("El nombre del usuario es %s reside en la ciudad de %s y tiene una edad de %d, su correo electronico "
               "es: %s " % (nombreUsuario, ciudad, edad, correo))
    print(mensaje)

def crearFlickr():
    print("----Se va a crear una cuenta en Flickr ---")
    nombreUsuario = str(input("Ingrese el nombre del usuario:"))
    correo = str(input("Ingrese el correo electrónico del usuario:"))
    mensaje = ("El nombre del usuario es %s y su correo electronico es %s " % (nombreUsuario, correo))
    return mensaje

def obtenerMensaje(contador):
     mensajeFinal = ["Campaña con poca afluencia",
            "Campaña moderada siga adelante", "Excelente campaña"]
     if contador >= 1 and contador <= 5:
         print(mensajeFinal[0])
     else:
         if contador >= 6 and contador <= 15:
             print(mensajeFinal[1])
         else:
             if contador >= 16:
                 print(mensajeFinal[2])



condicion = True
contador = 0



while (condicion):
    contador = contador + 1

    numero = int(input("Ingrese 1 para crear una cuenta en Facebook\n"
                       "Ingrese 2 para crear una cuenta en Twitter\n"
                       "Ingrese 3 para crear una cuenta en Whatsapp\n"
                       "Ingrese 4 para crear una cuenta en Telegram\n"
                       "Ingrese 5 para crear una cuenta en Signal\n"
                       "Ingrese 6 para crear una cuenta en Instagram\n"
                       "Ingrese 7 para crear una cuenta en Flickr\n"))
    if numero == 1:
        print(crearfacebook())
    else:
        if numero == 2:
            crearTwitter()
        else:
            if numero == 3:
                print(crearWhatsapp())
            else:
                if numero == 4:
                    crearTelegram()
                else:
                    if numero == 5:
                        print(crearSignal())
                    else:
                        if numero == 6:
                            crearInstagram()
                        else:
                            if numero == 7:
                                print(crearFlickr())
                            else:
                                print("El numero ingresado es incorrecto")


    salida = input("Escribir (si) para salir del proceso o Escriba (no) para seguir con la entrada de datos\n")
    if salida == "si":
        condicion = False

obtenerMensaje(contador)
