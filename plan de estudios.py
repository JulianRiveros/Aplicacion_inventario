entero = 10
flotante = 10.5
cadena = "Hola Python"
booleano = True

print(type(entero), type(flotante), type(cadena), type(booleano))

suma = 5 + 3
comparacion = 5 > 3
print(suma, comparacion)

# Estructuras de control

edad = 20
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

for i in range(5):
    print(i)

contador = 0
while contador < 5:
    print(contador)
    contador += 1


# Funciones y modulos
def suma_fun(a, b):
    return a + b


print(suma_fun(3, 4))

import math

print(math.sqrt(16))

# Diferencia entre is y == , is compara si dos variables apuntan
# al mismo objeto en memoria, mientras que == compara los valores
arreglo = [1, 2, 3]
b_arreglo = arreglo
print(arreglo is b_arreglo)
print(arreglo == b_arreglo)

# Duck typing es un concepto en el que el tipo de una variable se determina
# por su comportamiento en lugar de su declaracion explicita


# POO
# CLASE: Plantilla para crear objetos
# OBJETO: Instancia de una clase
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


persona_1 = Persona("Jeni")

print(persona_1.nombre)

# Manejo de APIs y peticiones HTTP
import requests

try:
    ##response = requests.get("https://api.example.com/datos")
    ##response.raise_for_status()
    print("CONEXION")
except requests.exceptions.HTTPError as err:
    # print(f"Error HTTP: {err}")
    print("ERROR")

# Aprovisionamiento y Automatizacion
import paramiko

cliente = paramiko.SSHClient()
cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
cliente.connect("192.168.1.100", username="usuario", password="clave")
stdin, stdout, stderr = cliente.exec_command("ls -l")
print(stdout.read().decode())
cliente.close()

# Infraestructura como codigo
# - hosts: servidores
#  become: yes
#  tasks:
#   - name: Instalar Nginx
#     apt:
#       name: nginx
#       state: present

# Seguridad y ciberseguridad
import socket

#for port in range(20, 1025):
#    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    sock.settimeout(1)
#    result = sock.connect_ex(("192.168.1.1", port))
#    if result == 0:
#        print(f"Puerto {port} abierto")
#    sock.close()

#Capturar trafico de red con scapy
from scapy.all import sniff
def capturar_paquetes(packet):
    print(packet.summary)
sniff(prn=capturar_paquetes, count=10)

