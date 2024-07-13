

##import sys
##print(sys.path)


from pymongo import MongoClient

# Conectarse a MongoDB
#client = MongoClient('localhost', 27017)

# Seleccionar o crear una base de datos
#db = client['Credenciales_Admins']

# Verificar la creación de la base de datos
#

# Conectar a MongoDB
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client.Admins  # Reemplaza 'mydatabase' con tu nombre de base de datos
    print("Conexión exitosa a MongoDB")
except Exception as e:
    print(f"No se pudo conectar a MongoDB: {e}")

# Definir la colección
usuarios = db['usuarios']

# Crear documentos de ejemplo e insertarlos en la colección
usuario1 = {
    'id_usuario': 1,
    'username': 'usuario1',
    'password': 'password1'
}

usuarios.insert_one(usuario1)


# Consultar todos los usuarios
for usuario in usuarios.find():
    print(usuario)

# Consultar un usuario específico por username
usuario = usuarios.find_one({'username': 'usuario1'})
print(usuario)

#print(client.list_database_names())


