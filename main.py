
temperatura:float=40.0
if temperatura > 20:
    print("alta temperatura")


temp:int=20
if temp > 35:
    print("temperatura alta")
else:
    print("temperatura normal")


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



a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))

menor = a

if b < menor:
    menor = b
if c < menor:
    menor = c

print("El mínimo es:", menor)



## usando  WHILE crea un programa que me de una pregunta para responder 
# y que solo tenga 3 oportubidades para dar con la respuesta correcta

intentos = 0
while intentos < 3:
    respuesta = input("¿Cuánto es 5 + 5? ")
    if respuesta == "10":
        print("Correcto")
        break
    else:
        print("Incorrecto")
        intentos += 1