import Base_datos_usuarios
import getpass


##Funcion para mostrar el menu luego de inicio de sesion
def mostrar_menu_usuarios():
    while True:
        print("\nOpciones:")
        print("1. Gastos")
        print("2. Ingresos")
        print("3. Inventario")
        print("4. Salir")
        opcion = input ("Seleccione una opcion: ")
        
        if opcion == "1":
            print("Se Ingresa exitosamente al menu de Gastos")
        elif opcion == "2":
            print("Se ingresa exitosamente al menu de Ingresos")
        elif opcion == "3":
            print("Se ingresa exitosamente al menu de Inventario")
        elif opcion == "4":
            break
        else:
            print("Opcion no valida, intente nuevamente")
            


##Funcion para mostrar el menu principal
def mostrar_menu_principal(usuarios):
    while True:
        print("\nOpciones:")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Consultar Usuarios")
        print("4. Salir")
        opcion = input ("Seleccione una opcion: ")

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
                mostrar_menu_usuarios()
        elif opcion == "3":
            # Consultar todos los usuarios
            for usuario in usuarios.find():
                print(usuario)
        elif opcion == "4":
            break
        else:
            print("Opcion no valida. Intente nuevamente.")

if __name__ == "__main__":
    usuarios = Base_datos_usuarios.crear_conexion_base_datos()
    mostrar_menu_principal(usuarios)
        