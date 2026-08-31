"""
# 1. escriba un programa que acepte 1 opcion de dos jugadores en piedra_papel
- entrada:persona1=piedra,persona2=papel 
- salida:gana persona2,papel envuelve Piedra
"""

persona1 = input("Persona 1: ")
persona2 = input("Persona 2: ")
if persona1 == "piedra" and persona2 == "tijera":
    print("Gana persona 1")
if persona1 == "papel" and persona2 == "piedra":
    print("Gana persona 1")
if persona1 == "tijera" and persona2 == "papel":
    print("Gana persona 1")
if persona1 == persona2:
    print("Empate")
if persona2 == "piedra" and persona1 == "tijera":
    print("Gana persona 2")
if persona2 == "papel" and persona1 == "piedra":
    print("Gana persona 2")
if persona2 == "tijera" and persona1 == "papel":
    print("Gana persona 2")


"""
2. escribe un programa que acpte 3 numeros y calcule el minimo 
- entrada: 7,4,8
- salida: 4
"""

a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))

menor = a

if b < menor:
    menor = b
if c < menor:
    menor = c

print("El mínimo es:", menor)