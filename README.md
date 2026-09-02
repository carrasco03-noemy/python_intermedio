# CONTROL DE FLUJO

## CONDICIONALES
### La sentencia if
esta sentencia al igual que en otros lenguajes de programacion en su escritura debemos añadir una `exprecion de comparacion`,terminada en dos puntos`:`

```python
temperatura:float=40.0
if temperatura > 20:
    print("alta temperatura")
```

en este caso solo se ejecutara el blooque `if` si la condicion es `verdadera` ,para controlar si la condicion es `falsa` debemos usar la sentencia `else`

# segundo ejemplo

```python
temp:int=20
if temp > 35:
    print("temperatura alta")
else:
    print("temperatura normal")
```
podriamos tener muchas condicionales, lo que se llamaria tecnicamente *condiciones anidadas*:

```python
temp: int=20
if temp < 30:
   if temp < 10
   print ("nivel azul mucho frio")
   else: 
   print ("nivel verde normal")
else:
if temp < 30:
print ("nivel naranja")
else:
    print (" nivel rojo")
``` 

python ofrece una mejora en la escritura de condiciones anidadas, para ello debemos usar 

```python
temp: int=20
if temp < 30:
   if temp < 10
   print ("nivel azul mucho frio")
   else: 
   print ("nivel verde normal")
elif temp < 30:
print ("nivel naranja")
else:
    print (" nivel rojo")
```

### SENTENCIA 
Esta es una nueva sentencia condicional ,similar a los if anidados:

```python
vocal:str="a"
match vocal:
    case "a":
        print("es una vocal")
    case "e":
        print("es una vocal")
    case "i":
        print("es una vocal")
    case "0":
        print("es una vocal")
    case "u":
        print("es una vocal")
```

una manera de hacer el codigo mas corto es :

```python
vocal:str=input("ingrese una letra: ")
match vocal:
    case "a"| "e"|"i"|"0"|"u":
        print("es una vocal")
    case _:
        print("es una consonante")
```

## BUCLES

### La sentencia WHILE

Es el primer mecanismo que existe en python para repetir instrucciones.
La semantica tras esta sentencia es :`Mientras se cumpla la condicion has algo`.
EJEMPLO:

```python
salir:str="N"
while salir=="N":
     print("Hola que tal")
    salir=input("deseas salir (S/N): ")
        print("Adios")
```

se puede cortar la ejecucion de un `while`haciendoel uso `break`:

```python

intentos = 0
while intentos < 3:
    respuesta = input("¿Cuánto es 5 + 5? ")
    if respuesta == "10":
        print("Correcto")
        break
    else:
        print("Incorrecto")
        intentos += 1
```
