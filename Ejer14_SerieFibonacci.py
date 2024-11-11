print("SERIE FIBONACCI")
print("Introduce un número entero positivo para mostrar los primeros N números de la serie de Fibonacci:")
num = int(input())

if num <= 0:
    print("Por favor, introduce un número entero positivo.")
else:
    fibonacci_series = [] 

    a = 0
    b = 1

    for _ in range(num):
        # Agregar el número actual a la lista
        fibonacci_series.append(a)  
        # Actualizar a y b para los siguientes números de Fibonacci
        a, b = b, a + b  

    print(f"Los primeros {num} números de la serie de Fibonacci son: {fibonacci_series}")