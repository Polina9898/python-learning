# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


def f(a, b):
    if b == 0:
        return a
    return f(a + 1, b - 1)

m = int(input())
n = int(input())

print(f(n, m))