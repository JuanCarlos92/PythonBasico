print("NUMEROS IMPARES ENTRE DOS NÚMEROS")
print("Introduce el  primer número:")
num1 = int(input())
print("Introduce el segundo número:")
num2 = int(input())

if num1 > num2:
    num1, num2 = num2, num1 

print(f"Números impares entre {num1} y {num2}:")
1

for num in range(num1, num2 + 1):
    if num % 2 != 0: 
        print(num)