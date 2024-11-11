print("TRIANGULO DE NUMEROS")
print("Introduce un número entero positivo: ")
num = int(input())

if num <= 0:
    print("Por favor, introduce un número entero positivo.")
else:
    
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end="")
            
        print()