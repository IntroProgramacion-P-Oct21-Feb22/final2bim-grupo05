/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package tallerfinaljava;

import java.util.Locale;
import java.util.Scanner;

/**
 *
 * @author Usuario
 */
public class TallerfinalJava {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        entrada.useLocale(Locale.US);

        String salida;
        int numero;
        int contador = 0;

        do {
            contador = contador + 1;
            System.out.println("Ingrese 1 para crear una cuenta en Facebook\n"
                    + "Ingrese 2 para crear una cuenta en Twitter\n"
                    + "Ingrese 3 para crear una cuenta en Whatsapp\n"
                    + "Ingrese 4 para crear una cuenta en Telegram\n"
                    + "Ingrese 5 para crear una cuenta en Signal\n"
                    + "Ingrese 6 para crear una cuenta en Instagram\n"
                    + "Ingrese 7 para crear una cuenta en Flickr\n");
            numero = entrada.nextInt();
            entrada.nextLine();
            if (numero == 1) {
                System.out.println(crearFacebook());
            } else {
                if (numero == 2) {
                    crearTwitter();
                } else {
                    if (numero == 3) {
                        System.out.println(crearWhatsapp());
                    } else {
                        if (numero == 4) {
                            crearTelegram();
                        } else {
                            if (numero == 5) {
                                System.out.println(crearSignal());
                            } else {
                                if (numero == 6) {
                                    crearInstagram();
                                } else {
                                    if (numero == 7) {
                                        System.out.println(crearFlickr());
                                    } else {
                                        System.out.println("El numero ingresado"
                                                + " es incorrecto");
                                    }
                                }
                            }
                        }
                    }
                }
            }

            System.out.println("Ingrese (si) o cualquier otra palabra para salir "
                    + " del proceso, caso contrario ingrese (no) para"
                    + " continuar");
            salida = entrada.nextLine();
        } while (salida.equals("no"));

        obtenerMensaje(contador);
    }

    public static String crearFacebook() { // devuelve valor
        Scanner entrada = new Scanner(System.in);
        entrada.useLocale(Locale.US);

        String nombreUsuario;
        int edad;
        String ciudad;
        String pais;
        String correo;
        String mensaje;

        System.out.println("----Se va a crear una cuenta en Facebook----");

        System.out.println("Ingrese el nombre del usuario");
        nombreUsuario = entrada.nextLine();
        System.out.println("Ingrese la edad del usuario");
        edad = entrada.nextInt();
        entrada.nextLine();
        System.out.println("Ingrese la ciudad del usuario");
        ciudad = entrada.nextLine();
        System.out.println("Ingrese el país del usuario");
        pais = entrada.nextLine();
        System.out.println("Ingrese el correo electrónico del usuario");
        correo = entrada.nextLine();

        mensaje = String.format("El nombre del usuario es %s su edad es %d"
                + " reside en la ciudad de %s en el país %s, y su correo"
                + " electrónico es %s",
                nombreUsuario, edad, ciudad, pais, correo);

        return mensaje;
    }

    public static void crearTwitter() { // no devuelve valor
        Scanner entrada = new Scanner(System.in);
        entrada.useLocale(Locale.US);

        String nombreUsuario;
        String nombre;
        String apellidos;
        int edad;
        String ciudad;
        String pais;
        String idioma;
        String correo;
        String mensaje;

        System.out.println("----Se va a crear una cuenta en Twitter----");

        System.out.println("Ingrese el nombre del usuario");
        nombreUsuario = entrada.nextLine();
        System.out.println("Ingrese sus nombres");
        nombre = entrada.nextLine();
        System.out.println("Ingrese sus apellidos");
        apellidos = entrada.nextLine();
        System.out.println("Ingrese la edad del usuario");
        edad = entrada.nextInt();
        entrada.nextLine();
        System.out.println("Ingrese la ciudad del usuario");
        ciudad = entrada.nextLine();
        System.out.println("Ingrese el país del usuario");
        pais = entrada.nextLine();
        System.out.println("Ingrese el idioma a preferencia");
        idioma = entrada.nextLine();
        System.out.println("Ingrese el correo electrónico del usuario");
        correo = entrada.nextLine();

        mensaje = String.format("El nickname del Usuario es %s, sus nombres son"
                + " %s, con apellidos %s, su edad es %d, reside en la ciudad de"
                + " %s en el país %s\n, el lenguaje seleccionado es %s y el correo"
                + " electrónico del usuario es:",
                nombreUsuario, nombre, apellidos, edad, ciudad, pais, idioma,
                correo);

        System.out.printf(mensaje + " %s\n",correo);
    }

    public static String crearWhatsapp() { // devuelve valor
        Scanner entrada = new Scanner(System.in);
        entrada.useLocale(Locale.US);

        String nombreUsuario;
        int telefono;
        int edad;
        String ciudad;
        String pais;
        String mensaje;

        System.out.println("----Se va a crear una cuenta en Whatsapp----");

        System.out.println("Ingrese el nombre del usuario");
        nombreUsuario = entrada.nextLine();
        System.out.println("Ingrese el numero de telefono");
        telefono = entrada.nextInt();
        System.out.println("Ingrese la edad del usuario");
        edad = entrada.nextInt();
        entrada.nextLine();
        System.out.println("Ingrese la ciudad del usuario");
        ciudad = entrada.nextLine();
        System.out.println("Ingrese el país del usuario");
        pais = entrada.nextLine();

        mensaje = String.format("El nombre del usuario es %s, el número de "
                + " telefono del usuario es %d, la edad del usuario es %d reside"
                + " en la ciudad de %s en el país %s",
                nombreUsuario, telefono, edad, ciudad, pais);

        return mensaje;
    }

    public static void crearTelegram() { // no devuelve valor
        Scanner entrada = new Scanner(System.in);
        entrada.useLocale(Locale.US);

        String nombreUsuario;
        int telefono;
        String ciudad;
        String pais;
        String area;
        String mensaje;

        System.out.println("----Se va a crear una cuenta en Telegram----");

        System.out.println("Ingrese el nombre del usuario");
        nombreUsuario = entrada.nextLine();
        System.out.println("Ingrese el numero de telefono");
        telefono = entrada.nextInt();
        entrada.nextLine();
        System.out.println("Ingrese la ciudad del usuario");
        ciudad = entrada.nextLine();
        System.out.println("Ingrese el país del usuario");
        pais = entrada.nextLine();
        System.out.println("Ingrese el área de interés del usuario");
        area = entrada.nextLine();

        mensaje = String.format("El nombre del usuario es %s, el número del"
                + " usuario es %d, reside en la ciudad de %s en el país de %s"
                + " y el área de interes del usuario es %s",
                nombreUsuario, telefono, ciudad, pais, area);

        System.out.println(mensaje);

    }

    public static String crearSignal() { // devuelve valor
        Scanner entrada = new Scanner(System.in);
        entrada.useLocale(Locale.US);

        String nombreUsuario;
        int telefono;
        String ciudad;
        String pais;
        String hobby;
        String mensaje;

        System.out.println("----Se va a crear una cuenta en Signal----");

        System.out.println("Ingrese el nombre del usuario");
        nombreUsuario = entrada.nextLine();
        System.out.println("Ingrese el numero de telefono");
        telefono = entrada.nextInt();
        entrada.nextLine();
        System.out.println("Ingrese la ciudad del usuario");
        ciudad = entrada.nextLine();
        System.out.println("Ingrese el país del usuario");
        pais = entrada.nextLine();
        System.out.println("Ingrese su hobby principal");
        hobby = entrada.nextLine();

        mensaje = String.format("El nombre del usuario es %s, su número de "
                + " telefono es %d, reside en la ciudad de %s, en el país de %s"
                + " y su hobby principal es %s",
                nombreUsuario, telefono, ciudad, pais, hobby);

        return mensaje;
    }

    public static void crearInstagram() { // no devuelve valor
        Scanner entrada = new Scanner(System.in);
        entrada.useLocale(Locale.US);

        String nombreUsuario;
        String ciudad;
        int edad;
        String correo;
        String mensaje;

        System.out.println("----Se va a crear una cuenta en Instagram----");

        System.out.println("Ingrese el nombre del usuario");
        nombreUsuario = entrada.nextLine();
        System.out.println("Ingrese la ciudad del usuario");
        ciudad = entrada.nextLine();
        System.out.println("Ingrese la edad del usuario");
        edad = entrada.nextInt();
        entrada.nextLine();
        System.out.println("Ingrese el correo electrónico del usuario");
        correo = entrada.nextLine();

        mensaje = String.format("El nombre del usuario es %s reside en la ciudad"
                + " de %s y tiene una edad de %d, su correo electronico es; %s",
                nombreUsuario, ciudad, edad, correo);

        System.out.println(mensaje);
    }

    public static String crearFlickr() { // devuelve valor
        Scanner entrada = new Scanner(System.in);
        entrada.useLocale(Locale.US);

        String nombreUsuario;
        String correo;
        String mensaje;

        System.out.println("----Se va a crear una cuenta en Flickr----");

        System.out.println("Ingrese el nombre del usuario");
        nombreUsuario = entrada.nextLine();
        System.out.println("Ingrese el correo electrónico del usuario");
        correo = entrada.nextLine();

        mensaje = String.format("El nombre del usuario es &s y su correo "
                + "electronico es %s",
                nombreUsuario, correo);

        return mensaje;
    }

    public static void obtenerMensaje(int contador) {

        String[] mensajeFinal = {"Campaña con poca afluencia",
            "Campaña moderada siga adelante", "Excelente campaña"};

        if (contador >= 1 && contador <= 5) {
            System.out.println(mensajeFinal[0]);
        } else {
            if (contador >= 6 && contador <= 15) {
                System.out.println(mensajeFinal[1]);
            } else {
                if (contador >= 16) {
                    System.out.println(mensajeFinal[2]);
                }
            }
        }
    }

}
