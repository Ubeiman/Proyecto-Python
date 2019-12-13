import os
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

def registrar_mascota():
    R = ()
    print("DATOS DE LA MASCOTA")
    nombreMascota = input("Ingrese el nombre  >> ")
    identificacionM = input("Ingrese la identificacion >> ")
    edad = int(input("Ingrese la edad >> "))
    tipoMascota = input("Ingrese el tipo >> ")
    raza = input("Ingrese la raza >> ")
    observaciones = input("Ingrese las observaciones >> ")
    print("DATOS DEL PROPIETARIO")
    nombrePropietario = input("Ingrese el nombre >> ")
    identificacionP = input("Ingrese la identificacion >> ")
    telefono = input("Ingrese el telefono >> ")
    correo = input("Ingrese el correo >> ")
    direccion = input("Ingrese la direccion  >> ")
    R = (nombreMascota, identificacionM, edad, tipoMascota, raza, observaciones,
         nombrePropietario, identificacionP, telefono, correo, direccion)
    return R

def asignar_cita():
    A = ()
    print("DATOS DE LA CITA")
    dia = int(input("Dia >> "))
    mes = int(input("Mes >> "))
    anho = int(input("Año >> "))
    motivo = input("Motivo de la consulta >> ")
    veterinario = input("Nombre del veterinario >> ")
    codigoConsulta = int(input("Codigo de la cita >> "))
    identificacionMasco = input("Documento de la mascota >> ")
    hora = int(input("Hora >> "))

    A = (dia, mes, anho, motivo, veterinario,
         codigoConsulta, identificacionMasco, hora)
    return A

    # inserta datos a la base de datos
# inserta datos a la base de datos
def registrart_mascota():
    datos = registrar_mascota()
    # conexion a la base de datos
    con_bd = sqlite3.connect('mybase.db')
    # cursor a la db
    cursor_agenda = con_bd.cursor()
    # consultas
    cursor_agenda.execute("INSERT INTO mascotas(nombreMascota,identificacionM,edad,tipoMascota,raza,observaciones,nombrePropietario,identificacionP,telefono,correo,direccion) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (datos))
    # se ejecutan los cambios
    con_bd.commit()
    # cierre del cursor
    cursor_agenda.close()
    # cierre de la conexion
    con_bd.close()

def asignacion_cita():
    cita = asignar_cita()
    # conexion a la base de datos
    con_bd = sqlite3.connect('mybase.db')
    # cursor a la db
    cursor_agenda = con_bd.cursor()
    # consultas
    cursor_agenda.execute("INSERT INTO asignar(dia,mes,anho,motivo,veterinario,codigoConsulta,identificacionMasco,hora) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (cita))
    # se ejecutan los cambios
    con_bd.commit()
    # cierre del cursor
    cursor_agenda.close()
    # cierre de la conexion
    con_bd.close()

def consultar_todo():
    # conexion a la base de datos
    con_bd = sqlite3.connect('mybase.db')
    # cursor a la db
    cursor_agenda = con_bd.cursor()
    # consultas
    # email=input("Ingrese el documento sobre el cual desea investigar")
    identificacionM = input("Ingrese la identificacion")
    consulta = cursor_agenda.execute(
        "SELECT nombreMascota FROM mascotas WHERE identificacionM=?", (identificacionM,))
    # impresion de todos los campos
    for fila in consulta:
        print("fila: {0}".format(fila))
        for campo in fila:
            print("Campo de la fila: {0}".format(campo))
    con_bd.commit()
    # cierre del cursor
    cursor_agenda.close()
    # cierre de la conexion
    con_bd.close()

def actualizar():
    # conexion a la base de datos
    con_bd = sqlite3.connect('mybase.db')
    # cursor a la db
    cursor_agenda = con_bd.cursor()
    # consultas
    # email=input("Ingrese el documento sobre el cual desea investigar")
    identificacion = input("Ingrese la identificacion del propietario: ")
    consulta = cursor_agenda.execute("UPDATE mascotas  SET observaciones=?,telefono=?,direccion=? WHERE identificacionP=?", (input("ingrese las nuevas observaciones: "), input("ingrese el nuevo telefono: "), input("ingrese la nueva direccion: "), identificacion,))
    # impresion de todos los campos
    for fila in consulta:
        print("fila: {0}".format(fila))
        for campo in fila:
            print("Campo de la fila: {0}".format(campo))
    con_bd.commit()
    # cierre del cursor
    cursor_agenda.close()
    # cierre de la conexion
    con_bd.close()

def borrar():
    # conexion a la base de datos
    con_bd = sqlite3.connect('mybase.db')
    # cursor a la db
    cursor_agenda = con_bd.cursor()
    # consultas
    # email=input("Ingrese el documento sobre el cual desea investigar")
    id = input("Ingrese la identificacion de la mascota")
    consulta = cursor_agenda.execute("DELETE nombreMascota FROM mascotas WHERE identificacionM=?", (id,))
    # impresion de todos los campos
    for fila in consulta:
        print("fila: {0}".format(fila))
        for campo in fila:
            print("Campo de la fila: {0}".format(campo))
    con_bd.commit()
    # cierre del cursor
    cursor_agenda.close()
    # cierre de la conexion
    con_bd.close()

def menu_principal():    
    while True:
        print("\t¡BIENVENIDOS!")
        print("\t1 - Registrar mascota")
        print("\t2 - Asignar citas")
        print("\t3 - Consultar citas")
        print("\t4 - Actualizar")
        print("\t5 - Borrar")
        print("\t6 - Enviar promociones")
        print("\t7 - salir")

        opcionMenu = input("\tInsertar la opcion que deseas realizar >> ")
        if opcionMenu == "1":
            print("")
            print("Bienvenido a registro de mascotas.")
            print("")
            registrart_mascota()

        elif opcionMenu == "2":
            print("")
            input("Bienvenido a asignacion de citas.")
            print("")
            asignacion_cita()

        elif opcionMenu == "3":
            print("")
            input("¿Bienvenido que cita quieres consultar?")
            consultar_todo()

        elif opcionMenu == "4":
            print("")
            input("Bienvenido por favor actualiza tus datos.")
            actualizar()

        elif opcionMenu=="5":
            print ("")
            input("¡Bienvenido a borrar datos!")  
            print ("")
            borrar()

        elif opcionMenu=="6":
            print ("")
            input("¡Bienvenido a envio de promociones!")  
            print ("")
            enviar_correo()

        elif opcionMenu=="7":
            print ("Gracias por usar nuestro sistema")
            False
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        os.system('cls')  # NOTA para windows tienes que cambiar clear por cls

def enviar_correo():
    # conexion a la base de datos
    con_bd = sqlite3.connect('mybase.db')
    # cursor a la db
    cursor_agenda = con_bd.cursor()
    # envios
    consulta = cursor_agenda.execute("SELECT correo FROM mascotas")
    proveedor_correo = 'smtp.gmail.com: 587'
    # print(proveedor_correo)
    remitente ="samy12paez12@gmail.com"
    password="12062001maicol"
    # conexion a servidor
    servidor = smtplib.SMTP(proveedor_correo)
    servidor.starttls()
    servidor.ehlo()
    # autenticacion
    servidor.login(remitente, password)
    
    # impresion de todos los campos
    for fila in consulta:
        print("fila: {0}".format(fila))
        for campo in fila:
            print("Campo de la fila: {0}".format(campo))
            # mensaje 
            mensaje ="Hola estimado cliente fiel a nuestros servicios tendra una promocion en todos los productos o servicios como peluqueria,jugueteria, por favor aserquese a nuestros lugares"
            msg = MIMEMultipart()
            msg.attach(MIMEText(mensaje, 'html'))
            msg['From'] = remitente
            msg['To'] = campo
            msg['Subject'] =("CLIENTE DESTACADO DIRTY LEGS¡¡")

            servidor.sendmail(msg['From'] , msg['To'], msg.as_string())
    # cierre del cursor
    cursor_agenda.close()
    # cierre de la conexion
    con_bd.close()

menu_principal()


