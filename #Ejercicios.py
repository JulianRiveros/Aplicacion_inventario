#Ejercicios

#invertir una cadena

def invertir_cadena(cadena: str) -> str:
    return cadena[::-1]

print(invertir_cadena("python"))


#Verificar si una palabra es palindromo
def  es_palindromo(palabra: str) -> bool:
    return palabra == palabra[::-1]

print(es_palindromo("radar"))
print(es_palindromo("python"))

def suma(a: int, b: int) -> int:
    return a + b

print(suma(5, 4))


#Manejo de contextos con python
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, python")
    

with open("archivo.txt", "r") as file:
    contenido = file.read()
        
print(contenido)


import logging 
logging.basicConfig(level=logging.INFO)
logging.info("Este es un mensaje de DEBUG")

def calcular_area(base: float, altura: float) -> float:
    return base * altura

print(calcular_area(5, 8))

#Usar dataclasses para manejar estructuras de datos
from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int
persona1 = Persona("Jeni",18)
print(persona1)



#Uso de excepciones especificas
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")