print("COMPROBAR SI AL CONTRASEÑA ES CORRECTA")
print("Introduce la contraseña:")
password = input()
print("Vuelve a introducir la contraseña:")
verificar_password = input()

while  password != verificar_password:
    print("Error: Vuelve a introducir la contraseña:")
    verificar_password = input()

print("Contraseña correcta")
