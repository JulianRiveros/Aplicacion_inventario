from pymongo import MongoClient
from bson.objectid import ObjectId
import Base_datos_usuarios


class Inventario:
    def __init__(self,db) -> None:
        self.db =db
        self.collection = self.db['inventario']

#funcion agregado de item a la base de datos
    def agregar_item(self, id, nombre, cantidad,precio):
        #Asigancion de atributos
        item ={
            "id":id,
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }
        self.collection.insert_one(item)
        print(f"item '{item}' agregado exitosamente.")
#funcion actualizar items de la base datos
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
#Funcion para restar la cantidad de items vendidos
    def deducir_items_vendidos(self, items_vendidos):
        for item in items_vendidos:
            self.collection.update_one(
                {"id": item['id']},
                {"$inc": {"cantidad": -item['cantidad']}}
            )
            print(f"Cantidad de '{item['id']}' dedicida en {item['cantidad']} unidades")
#funcion muestra el inventario
    def mostrar_inventario (self):
        items = self.collection.find()
        for item in items:
            print(item)

#Funcion conversion a numero entero
def convertir_a_entero (s):
    try:
        valor =int(s)
        return valor
    except ValueError:
        print("Error: El string no puede convertirse a un entero.")
        return None

#Agregar items al inventario
def agregar_item():
        id= input("Ingrese id de item: ")
        nombre= input("Ingrese nombre de item: ")
        cantidad = convertir_a_entero( input("Ingrese cantidad de item: "))
        precio= convertir_a_entero(input("Ingrese precio de item: "))
            
        #agregar item
        Base_datos_usuarios.coleccion_inventario().agregar_item(id,nombre,cantidad, precio)
        #Mostrar base de datos inventario
        Base_datos_usuarios.coleccion_inventario().mostrar_inventario()

#Actualizar items del inventario
def actualizar_item():
    id= input("Ingrese id de item a actualizar: ")
    cantidadActualizar= convertir_a_entero( input("Ingrese cantidad actualizada: "))
    Base_datos_usuarios.coleccion_inventario().actualizar_item(id, cantidadActualizar)
    
#Deducir cantidad en un item
def deducir_item():
    id= input("Ingrese id de item a deducir: ")
    cantidadVendida = convertir_a_entero(input("Ingrese cantidad vendida: "))
    items_vendidos = [
    {"id": id, "cantidad": cantidadVendida}
    ]
    Base_datos_usuarios.coleccion_inventario().deducir_items_vendidos(items_vendidos)
# Mostrar inventario
def mostrar_inventario():
    Base_datos_usuarios.coleccion_inventario().mostrar_inventario()
