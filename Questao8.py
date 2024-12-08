# Explicação:
# A recursão pode causar problemas de profundidade de pilha (quando o número de chamadas recursivas é muito alto) e repetição excessiva de cálculos (quando a função recalcula subproblemas já resolvidos).
# Vamos explorar três técnicas para otimizar a recursão: Memorização, Recursão de Cauda e Iteração.

# 1. Memorização
# Memorização é uma técnica onde armazenamos resultados de subproblemas já calculados para evitar cálculos repetidos. 
# Aqui, otimizamos a função Fibonacci utilizando um dicionário para armazenar os valores já calculados.

def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print("Fibonacci(50) com memorização:", fibonacci(50))


# 2. Recursão de Cauda
# Recursão de cauda ocorre quando a chamada recursiva é a última operação da função, permitindo que o compilador ou interpretador otimizar o uso da pilha.
# Exemplo de cálculo de fatorial com recursão de cauda:

def fatorial(n, acumulador=1):
    if n == 0:
        return acumulador
    return fatorial(n - 1, n * acumulador)

print("Fatorial(5) com recursão de cauda:", fatorial(5))


# 3. Solução Iterativa
# Em alguns casos, podemos transformar a recursão em uma solução iterativa para evitar os problemas de profundidade de pilha e melhorar a performance.

def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print("Fibonacci(50) com solução iterativa:", fibonacci_iterativo(50))
