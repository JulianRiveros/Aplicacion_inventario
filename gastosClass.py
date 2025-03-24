from pymongo import MongoClient
from bson.objectid import ObjectId
import Base_datos_usuarios


class Gastos():
    def _init_(self,db) -> None:
        self.db =db
        self.collection = self.db['gastos']

    def crear_conexion_base_datos(self):
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
        self.db =db
        self.collection = self.db['gastos']
        #return db

#funcion agregado de item a la base de datos
    def agregar_item_gastos(self, id, nombre, descripcion ,cantidad,costo):
        #Asigancion de atributos
        item ={
            "id":id,
            "nombre": nombre,
            "descripcion_producto": descripcion,
            "cantidad": cantidad,
            "costo": costo
        }
        self.collection.insert_one(item)
        print(f"item '{item}' agregado exitosamente.")
#funcion actualizar items de la base datos
    # def actualizar_item (self, id, cantidad=None, costo=None):
    #     update_fields ={}
    #     if cantidad is not None:
    #         update_fields["cantidad"] = cantidad
    #     if costo is not None:
    #         update_fields["costo"] = costo
        
    #     if update_fields:
    #         self.collection.update_one({"id": id}, {"$set": update_fields})
    #         print(f"Item con id '{id}' actualizado exitosamente.")
    #     else:
    #         print("No se proporcionaron campos para actualizar.")

#funcion muestra el inventario
    def mostrar_inventario_gastos (self):
        items = self.collection.find()
        for item in items:
            print(item)

#Funcion conversion a numero entero
def convertir_a_entero_gastos (s):
    try:
        valor =int(s)
        return valor
    except ValueError:
        print("Error: El string no puede convertirse a un entero.")
        return None

#Agregar items al inventario
def agregar_item_gastos():
        id= input("Ingrese id de item: ")
        nombre= input("Ingrese nombre de item: ")
        descripcion= input("Ingrese descripcion de item: ")
        cantidad = convertir_a_entero_gastos( input("Ingrese cantidad de item: "))
        costo= convertir_a_entero_gastos(input("Ingrese costo de item: "))
            
        #agregar item
        Base_datos_usuarios.coleccion_gastos().agregar_item_gastos(id,nombre,descripcion,cantidad, costo)
        #Mostrar base de datos inventario
        Base_datos_usuarios.coleccion_gastos().mostrar_inventario_gastos()

# Mostrar inventario
def mostrar_inventario_gastos():
    Base_datos_usuarios.coleccion_gastos().mostrar_inventario_gastos()