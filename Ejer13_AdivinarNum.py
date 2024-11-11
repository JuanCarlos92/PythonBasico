import random


print("ADIVINAR EL NUMERO ALEATORIO ENTRE 1 Y 100")
numero_aleatorio = random.randint(1, 100)
print("Se ha generado un numero aleatorio,  intenta adivinarlo")
while True:
    adivinar = int(input())
    if adivinar == numero_aleatorio:
        print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡")
        print("¡Has adivinado el numero aleatorio!")
        break
    else:
        if adivinar < numero_aleatorio:
            print("Introduce un numero mayor")

        else:
            print("Introduce un numero menor")
