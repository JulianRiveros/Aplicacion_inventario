import Base_datos_usuarios
import inventarioClass
import getpass
from colorama import init, Fore, Back, Style


##Funcion para modificar la contraseña del usuario que inicio sesion
#def modificar_contraseña_usuario():

##Funcion para mostrar el menu luego de inicio de sesion
def mostrar_menu_usuarios(inicio_sesion, usuarios):
    while True:
        print("\nOpciones:")
        print("1. Gastos")
        print("2. Ingresos")
        print("3. Inventario")
        print("4. Modificar contraseña Usuario")
        print("5. Eliminar Usuario")
        print("6. Cerrar Sesion")
        opcion = input ("Seleccione una opcion: ")
        
        if opcion == "1":
            print("Se Ingresa exitosamente al menu de Gastos")
        elif opcion == "2":
            print("Se ingresa exitosamente al menu de Ingresos")
        elif opcion == "3":
            menu_inventario()
            print("Se ingresa exitosamente al menu de Inventario")
        elif opcion == "4":
            while True:
                nuevaContrasenia = getpass.getpass(prompt="Ingrese la nueva contraseña: ") ## Se oculta la contraseña mientras se ingresa
                validacionContrasenia = getpass.getpass(prompt="Ingrese de nuevo la contraseña: ") ## Se oculta la contraseña mientras se ingresa
                if(nuevaContrasenia == validacionContrasenia):
                    Base_datos_usuarios.modificar_usuario(inicio_sesion.nombreUsuario, nuevaContrasenia,usuarios)
                    break
                else:
                    print(Fore.RED + "Las contraseñas no coinciden")
        elif opcion == "5":
            if inicio_sesion:
                Base_datos_usuarios.eliminar_usuario(usuarios)
            else:
                print(Fore.RED + "No ha iniciado sesion")    
        elif opcion == "6":
            break
        else:
            print(Fore.RED + "Opcion no valida, intente nuevamente")
            


##Funcion para mostrar el menu principal
def mostrar_menu_principal(usuarios):
    while True:
        print("\nOpciones:")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Consultar Usuarios")
        print(Fore.RED + "4. Salir")
        print(Style.RESET_ALL)
        opcion = input (Back.CYAN + Fore.BLACK + "Seleccione una opcion: ")
        print(Style.RESET_ALL)
        if opcion == "1":
            nombre_usuario= input("Ingrese nombre de usuario: ")
            #contrasenia = input("Ingrese contraseña: ")
            contrasenia = getpass.getpass(prompt="Ingresa tu contraseña: ") ## Se oculta la contraseña mientras se ingresa
            Base_datos_usuarios.registrar_usuario(nombre_usuario, contrasenia, usuarios)
        elif opcion == "2":
            nombre_usuario= input("Ingrese nombre de usuario: ")
            #contrasenia = input("Ingrese contraseña: ")
            contrasenia = getpass.getpass(prompt="Ingresa tu contraseña: ")  ## Se oculta la contraseña mientras se ingresa
            inicio_sesion = Base_datos_usuarios.iniciar_sesion(nombre_usuario, contrasenia, usuarios)
            if inicio_sesion:
                mostrar_menu_usuarios(inicio_sesion,usuarios)
        elif opcion == "3":
            # Consultar todos los usuarios
            for usuario in usuarios.find():
                print(usuario)
        elif opcion == "4":
            break
        else:
            print(Fore.RED + "Opcion no valida. Intente nuevamente.")


def menu_inventario():
    while True:
        print("\nOpciones:")
        print("1. Agregar item al inventario")
        print("2. Actualizar inventario")
        print("3. Deducir items vendidos")
        print("4. Mostrar inventario")
        print("5. Volver atras")
        opcion = input ("Seleccione una opcion: ")
        if opcion =="1":
            inventarioClass.agregar_item()
        elif opcion == "2":
            inventarioClass.actualizar_item()
        elif opcion == "3":
            inventarioClass.deducir_item()
        elif opcion =="4":
            inventarioClass.mostrar_inventario()
        elif opcion =="5":
            break
        else:
            print(Fore.RED + "Opcion no valida. Intente nuevamente.")   

if __name__ == "__main__":
    usuarios = Base_datos_usuarios.coleccion_usuarios()
    mostrar_menu_principal(usuarios)




        