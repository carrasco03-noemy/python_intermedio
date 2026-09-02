## crear un programa de login que mientras que la persona no ponga el usuario/contraseña correcto le siga pidiendo esa informacion,si el usuario/contraseña son correctos entonces darle un mensaje de bienvenida y salir del programa
usur_correcto:str="Admin"
pass_correcto:str|int = "1234"

while True:
    usur:str=input("Ingrese Usuario: ")
    password:str = input("Ingrese la Contraseña: ")
    if usur==usur_correcto and password==pass_correcto:
     print("Bienvenido a mi sistema")
    break
else:
     print("usuario/contraseña incorrectos sigue intentando")