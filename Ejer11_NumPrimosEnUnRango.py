print("NUMEROS PRIMOS EN UN RANGO")
print("Introduce  el primer número del rango:")
a = int(input())
print("Introduce el último número del rango:")
b = int(input())

if a > b:
    print("El primer número del rango debe ser menor o igual al último")
else:
    print(f"Numeros primos entre {a} y {b}:")
    
    for num in range(a, b + 1): # rango

        if num > 1: # Si es mayor a 1 asume que es primo
            esPrimo = True
            
            for i in range(2, int(num**0.5)+1): # Solo necesitamos comprobar hasta la raíz cuadrada del número
                if num % i == 0:   # Si el número es divisible entre i no es primo y sale del bucle
                    esPrimo = False  
                    break 
                
            if esPrimo:  # Si el número es primo lo imprime
                print(num)
                

