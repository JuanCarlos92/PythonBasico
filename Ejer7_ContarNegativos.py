print("CONTAR NUMEROS NEGATIVOS")
print("Introduce numeros o escriba 0 para finalizar")

contador =0

while True:
    num = float(input())

    if num == 0:
        break
    
    if num <0:
        contador += 1

print("Hay", contador, "numeros negativos")

    