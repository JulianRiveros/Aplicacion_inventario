
from pymongo import MongoClient
import bcrypt
import json
##import inventarioClass

class Usuario:
    def __init__(self, nombreUsuario, contraseña):
        self.nombreUsuario = nombreUsuario
        self.contraseña = contraseña
    def __str__(self):
        return f"Usuario: {self.nombreUsuario}"

    def verificar_contraseña(self, contraseña):
        return self.contraseña == contraseña


# Verificar conexion a MongoDB
def crear_conexion_base_datos():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        client.admin.command('ping')
        print("Conexión a MongoDB exitosa")   
        db = client['GestorLaGrieta'] # Reemplaza 'mydatabase' con tu nombre de base de datos
        print("Conexión exitosa a GestorLaGrieta")    
        client.admin.command('ping')
        print("Conexión exitosa a MongoDB")
        #print(db.list_collection_names())
    except Exception as e:
        print(f"No se pudo conectar a MongoDB: {e}") 
    return db
    
# Definir la colección Usuarios
def coleccion_usuarios():
    usuarios = crear_conexion_base_datos()['usuarios']
    print("Conexion exitosa a coleccion usuarios")
    return usuarios

def coleccion_inventario():
    inventario = inventarioClass.Inventario(crear_conexion_base_datos())
    print("Conexion exitosa a coleccion inventario")
    return inventario

def registrar_usuario(nombre_usuario, contrasenia, usuarios):
    #Verificar si el usuario ya existe
    if usuarios.find_one ({"nombre_usuario": nombre_usuario}):
        print("El usuario ya existe. ")
        return False
    #Hash de la contraseña
    contrasenia_hash = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())
    usuario_json = {
        "nombre_usuario": nombre_usuario,
        "contraseña": contrasenia_hash  # Asegúrate de hash la contraseña
    }
    usuarios.insert_one(usuario_json)
    admin = Usuario(nombre_usuario, contrasenia_hash)
    #Insertar el nuevo usuario en la base de datos
    #usuarios.insert_one({'nombre_usuario': nombre_usuario,
    #                   'contraseña': contrasenia_hash})

    print("Usuario Registrado Exitosamente.")
    return True

def iniciar_sesion(nombre_usuario, contrasenia,usuarios):
    #Buscar el usuario en la base de datos 
    usuario = usuarios.find_one({"nombre_usuario": nombre_usuario})

    if usuario:
        #verificar la contraseña
        if bcrypt.checkpw(contrasenia.encode('utf-8'), usuario['contraseña']):
            print("Inicio de Sesion exitoso.")
            admin = Usuario(nombre_usuario, contrasenia)
            return admin
        else:
            print("Contraseña Incorrecta.")
            return False
    else:
        print("El usuario no existe.")
        return False


def buscar_usuario(nombreUsuario,usuarios):
    usuario = usuarios.find_one({"nombre_usuario": nombreUsuario})

    if usuario:
        print("Usuario Existente")
        return True
    else:
        print("Usuario No existente")
        return False

##Funcion para modificar la contraseña del usuario existente
def modificar_usuario(nombreUsuario, nuevaContrasenia,usuarios):
    query = {'nombre_usuario': nombreUsuario}
    ##print
    
    usuario = usuarios.find_one({"nombre_usuario": nombreUsuario})
    if usuario:
        contrasenia_hash = bcrypt.hashpw(nuevaContrasenia.encode('utf-8'), bcrypt.gensalt())
        newValue = {'$set': {'contraseña': contrasenia_hash}}
        result = usuarios.update_one(query, newValue)
        print(f'{result.modified_count} usuario {nombreUsuario}  actualizado exitosamente')
    else:
        print("Usuario no encontrado")
    return True

def eliminar_usuario(usuarios):
    nombreUsuario= input("Ingrese nombre de usuario a eliminar: ")
    usuario = usuarios.find_one({"nombre_usuario": nombreUsuario})
    if usuario:
        query = {'nombre_usuario': nombreUsuario}
        result = usuarios.delete_one(query)
        ##print(f'{result.deleted_count} documento(s) eliminado(s)')
        print(f'{result.deleted_count} usuario {nombreUsuario} Eliminado exitosamente')
    else:
        print(f'Usuario no existente')