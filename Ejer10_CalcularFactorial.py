print("CALCULAR FACTORIAL")
print("Introduce un numero entero positivo:")
num  = int(input())
if num < 0:
    print("Error, el numero no es positivo")
else:
    factorial =1
    
    for i in range(1, num + 1):
        factorial = factorial * i
        
    print(f"El factorial de {num} es {factorial}")
