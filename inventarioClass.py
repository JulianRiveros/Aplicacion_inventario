from pymongo import MongoClient
from bson.objectid import ObjectId


class Inventario:
    def __init__(self,db) -> None:
        self.db =db
        self.collection = self.db['inventario']

    def agregar_item(self, id, nombre, cantidad,precio):
        item ={
            "id":id,
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }
        self.collection.insert_one(item)
        print(f"item '{item}' agregado exitosamente.")
    
    def actualizar_item (self, id, cantidad=None, precio=None):
        update_fields ={}
        if cantidad is not None:
            update_fields["cantidad"] = cantidad
        if precio is not None:
            update_fields["precio"] = precio
        
        if update_fields:
            self.collection.update_one({"id": id}, {"$set": update_fields})
            print(f"Item con id '{id}' actualizado exitosamente.")
        else:
            print("No se proporcionaron campos para actualizar.")

    def deducir_items_vendidos(self, items_vendidos):
        for item in items_vendidos:
            self.collection.update_one(
                {"id": item['id']},
                {"$inc": {"cantidad": -item['cantidad']}}
            )
            print(f"Cantidad de '{item['id']}' dedicida en {item['cantidad']} unidades")

    def mostrar_inventario (self):
        items = self.collection.find()
        for item in items:
            print(item)

#Crear conexion base datos

def crear_conexion_base_datos():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        client.admin.command('ping')
        print("Conexión a MongoDB exitosa")   
        db = client['GestorLaGrieta'] # Reemplaza 'mydatabase' con tu nombre de base de datos
        print("Conexión exitosa a GestorLaGrieta")     
    except Exception as e:
        print(f"No se pudo conectar a MongoDB: {e}")

    # Crear una instancia de la clase Inventario
    inventario = Inventario(db)
    
    #Agregar items al inventario
     
    
    id= input("Ingrese id de item: ")
    nombre= input("Ingrese nombre de item: ")
    try:
        s= input("Ingrese cantidad de item: ")
        cantidad = int(s)
    except ValueError:
        print("Error: El string no puede convertirse a un entero.")
        return None
    
    precio= input("Ingrese precio de item: ")
            
    #agregar item
    inventario.agregar_item(id,nombre,cantidad, precio)
    
    #Actualizar items del inventario
    
    id= input("Ingrese id de item a actualizar: ")
    try:
        s = input("Ingrese cantidad actualizada: ")
        cantidadActualizar = int(s)
    except ValueError:
        print("Error: El string no puede convertirse a un entero.")
        return None
    inventario.actualizar_item(id, cantidadActualizar)
    
    
    # Deducir items vendidos
    
    
    id= input("Ingrese id de item a deducir: ")
    try:
        s = input("Ingrese cantidad vendida: ")
        cantidadVendida = int(s)
    except ValueError:
        print("Error: El string no puede convertirse a un entero.")
        return None
    items_vendidos = [
    {"id": id, "cantidad": cantidadVendida}
    ]
    inventario.deducir_items_vendidos(items_vendidos)
    
    

    # Mostrar inventario
    inventario.mostrar_inventario()

crear_conexion_base_datos()