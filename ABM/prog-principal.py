#coding=UTF-8


#Importando librerías
import sys
import pickle

sys.path.append("modulos")

from tools.validate.validate import *
from tools.view.view import *


#Validando la existencia de los archivos
validating_existence_file("clientes.dat")


#Declaración de propósitos
"""
Breve descripción de las funcionalidades del software a desarrollar.
"""


#Descripción y definición de estructuras
"""
Estructura: clientes
Descripción: diccionario que contiene los datos de todos los clientes.
Tipos de datos de cada índice: Clave = string y Valor = lista.
Tipos de datos que contiene el atributo valor : [string, string, string, string, string, string, string, string]
Dato del atributo clave: dni_cliente
Datos del atributo valor: [apellido, nombre, dirección, codigo_postal, localidad, tel_fijo, tel_movil, email]
"""

clientes = {}


#Definición de funciones
def menu_principal():
    cleaning()
    print "\nSistema de GESTIÓN COMERCIAL.\n\nMenú Principal.\n\n"
    print "\n\t1. Clientes."
    print "\n\t2. Productos."
    print "\n\t3. Proveedores."
    print "\n\t4. Ventas."
    print "\n\t5. Salir."
    opcion = raw_input("\n\n\t\tIngrese una opción: ")
    opcion = validate_integer(opcion)
    opcion = validate_range(opcion, 1, 5)
    return opcion

def menu_clientes():
    cleaning()
    print "\nMenú de GESTIÓN de CLIENTES.\n\n"
    print "\n\t1. Ingresar."
    print "\n\t2. Modificar."  
    print "\n\t3. Buscar."
    print "\n\t4. Eliminar."  
    print "\n\t5. Retornar al Menú Principal."
    opcion = raw_input("\n\n\t\tIngrese una opción: ")
    opcion = validate_integer(opcion)
    opcion = validate_range(opcion, 1, 5)
    return opcion

def ingresar_cliente(base):
    cleaning()
    print "\nIngresar CLIENTE.\n\n"
    id_cliente = raw_input("\n\t\tIngrese el DNI del CLIENTE: ")
    if id_cliente not in base.keys():
        print "\n\tRellene los campos con la información correspondiente al CLIENTE.\n"
        temporal = []
        dato = raw_input("\n\t\t1. Apellido(s): ")
        temporal.append(dato)
        dato = raw_input("\n\t\t2. Nombre(s): ")
        temporal.append(dato)
        dato = raw_input("\n\t\t3. Dirección: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t4. Código Postal: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t5. Localidad: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t6. Teléfono Fijo: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t7. Teléfono Celular: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t8. eMail: ")
        temporal.append(dato)
        base[id_cliente] = temporal
        cleaning()
        print "\n\t\tEl CLIENTE ha sido ingresado al SISTEMA exitosamente."
    else:
        print "\n\t\tEl CLIENTE que desea ingresar ya existe."
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def modificar_cliente(base):
    cleaning()
    print "\nModificar CLIENTE.\n\n"
    id_cliente = raw_input("\n\t\tIngrese el DNI del CLIENTE que desea modificar: ")
    cleaning()
    if id_cliente in base.keys():
        temporal = base[id_cliente]
        print "\nLos datos del CLIENTE N°", id_cliente, "a modificar son:\n"
        print "\n\t\t1. Apellido(s):", temporal[0]
        print "\n\t\t2. Nombre(s):", temporal[1]
        print "\n\t\t3. Direccion:", temporal[2] 
        print "\n\t\t4. Código Postal:", temporal[3] 
        print "\n\t\t5. Localidad:", temporal[4] 
        print "\n\t\t6. Teléfono Fijo:", temporal[5] 
        print "\n\t\t7. Teléfono Celular:", temporal[6]
        print "\n\t\t8. eMail:", temporal[7]
        print "\n\n\n\t\t9. Salir SIN MODIFICAR DATOS del CLIENTE."
        atributo = raw_input("\n\n\t\tIngrese una opción: ")
        atributo = validate_integer(atributo)
        atributo = validate_range(atributo, 1, 9)
        cleaning()
        if atributo <> 9:
            msje = "Ingrese "
            etiquetas = ["Apellido(s): ", "Nombre(s): ", "Dirección: ", "Código Postal: ", "Localidad: ", "Teléfono Fijo: ", "Teléfono Celular: ", "eMail: "]
            msje = msje + etiquetas[atributo - 1]
            dato = raw_input(msje)
            temporal[atributo - 1] = dato
            base[id_cliente] = temporal
            cleaning()
            print "\n\t\tEl CLIENTE ha sido modificado en el SISTEMA exitosamente."
        else:
            print "\n\t\tNO ha sido modificado ningún atributo del CLIENTE en el SISTEMA."    
    else:
        print "\nEl CLIENTE N°", id_cliente, "que desea modificar, NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def buscar_cliente(base):
    cleaning()
    print "\nBuscar CLIENTE.\n\n"
    id_cliente = raw_input("\n\t\tIngrese el DNI del CLIENTE que desea buscar: ")
    cleaning()
    if id_cliente in base.keys():
        temporal = base[id_cliente]
        print "\nLos datos del CLIENTE buscado son:\n"
        print "\n\t\tCliente N°:", id_cliente
        print "\n\t\tApellido(s):", temporal[0]
        print "\n\t\tNombre(s):", temporal[1]
        print "\n\t\tDireccion:", temporal[2] 
        print "\n\t\tCódigo Postal:", temporal[3] 
        print "\n\t\tLocalidad:", temporal[4] 
        print "\n\t\tTeléfono Fijo:", temporal[5] 
        print "\n\t\tTeléfono Celular:", temporal[6]
        print "\n\t\teMail:", temporal[7]  
    else:
        print "\nEl CLIENTE N°", id_cliente, "que desea buscar, NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def eliminar_cliente(base):
    cleaning()
    print "\nEliminar CLIENTE.\n\n"
    id_cliente = raw_input("\n\t\tIngrese el DNI del CLIENTE que desea eliminar: ")
    cleaning()
    if id_cliente in base.keys():
        del base[id_cliente]
        cleaning()
        print "\n\t\tEl CLIENTE ha sido eliminado del SISTEMA exitosamente."
    else:
        print "\nEl CLIENTE N°", id_cliente, "que desea eliminar, NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")


#Programa principal
seleccion = menu_principal()
while seleccion <> 5:
    if seleccion == 1:
        #Cargando los datos del archivo "clientes.dat" al diccionario clientes
        clientes = loading_file_into_memory("clientes.dat")
        seleccion = menu_clientes()
        while seleccion <> 5:
            if seleccion == 1:
                ingresar_cliente(clientes)
            elif seleccion == 2:
                modificar_cliente(clientes)
            elif seleccion == 3:
                buscar_cliente(clientes)
            else:
                eliminar_cliente(clientes)
            seleccion = menu_clientes()
        #Guardando los cambios del diccionario clientes al archivo "clientes.dat"
        saving_changes_to_the_file("clientes.dat", clientes)
    elif seleccion == 2:
        cleaning()
        raw_input("\n\tEl sector de gestión de Productos SE ENCUENTRA ACTUALMENTE EN DESARROLLO.\n\n\t\t\tPresione la tecla ENTER para continuar operando.")        
    elif seleccion == 3:
        cleaning()
        raw_input("\n\tEl sector de gestión de Proveedores SE ENCUENTRA ACTUALMENTE EN DESARROLLO.\n\n\t\t\tPresione la tecla ENTER para continuar operando.")        
    else:
        cleaning()
        raw_input("\n\tEl sector de gestión de Ventas SE ENCUENTRA ACTUALMENTE EN DESARROLLO.\n\n\t\t\tPresione la tecla ENTER para continuar operando.")        
    seleccion = menu_principal()
cleaning()
raw_input("\n\tUsted ha salido exitosamente del SISTEMA.\n\n\t\t\tPresione la tecla ENTER para terminar de salir.")
cleaning()
