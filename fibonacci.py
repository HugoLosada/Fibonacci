def fibonacci_recursivo_naive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo_naive(n - 1) + fibonacci_recursivo_naive(n - 2)

# Implementar Memoization
def fibonacci_memoization(n, memo={}):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)

    return memo[n]

import time

# Medir el tiempo de ejecución para la Solución Recursiva Naive
tiempo_inicio_naive = time.time()
resultado_naive = fibonacci_recursivo_naive(35)  # Usa un número grande
tiempo_naive = time.time() - tiempo_inicio_naive

# Medir el tiempo de ejecución para Memoization
tiempo_inicio_memoization = time.time()
resultado_memoization = fibonacci_memoization(35)  # Usa el mismo número grande
tiempo_memoization = time.time() - tiempo_inicio_memoization

print(f"Resultado Recursivo Naive: {resultado_naive}")
print(f"Resultado Memoization: {resultado_memoization}")

print(f"Tiempo Recursivo Naive: {tiempo_naive} segundos")
print(f"Tiempo Memoization: {tiempo_memoization} segundos")

    

    

