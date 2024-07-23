
from pymongo import MongoClient
import bcrypt
import json


# Conexion y verificacion a MongoDB
def crear_conexion_base_datos():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        client.admin.command('ping')
        print("Conexión a MongoDB exitosa")   
        db = client['GestorLaGrieta'] # Reemplaza 'mydatabase' con tu nombre de base de datos
        print("Conexión exitosa a GestorLaGrieta")     
    except Exception as e:
        print(f"No se pudo conectar a MongoDB: {e}")


    # Definir la colección
    usuarios = db['usuarios']
    return usuarios

def registrar_usuario(nombre_usuario, contrasenia, usuarios):
    #Verificar si el usuario ya existe
    if usuarios.find_one ({"nombre_usuario": nombre_usuario}):
        print("El usuario ya existe. ")
        return False
    #Hash de la contraseña
    contrasenia_hash = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())
    #Insertar el nuevo usuario en la base de datos
    usuarios.insert_one({'nombre_usuario': nombre_usuario,
                        'contraseña': contrasenia_hash})

    print("Usuario Registrado Exitosamente.")
    return True

def iniciar_sesion(nombre_usuario, contrasenia,usuarios):
    #Buscar el usuario en la base de datos 
    usuario = usuarios.find_one({"nombre_usuario": nombre_usuario})

    if usuario:
        #verificar la contraseña
        if bcrypt.checkpw(contrasenia.encode('utf-8'), usuario['contraseña']):
            print("Inicio de Sesion exitoso.")
            return True
        else:
            print("Contraseña Incorrecta.")
            return False
    else:
        print("El usuario no existe.")
        return False


