"""Zadanie 1. Korzystając z techniki programowania dynamicznego napisz program obliczania
elementów ciągu Fibonacciego:"""


def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    elif i > 1:
        return fib(i-1) + fib(i-2)
    

f = int(input("Podaj którą liczbę ciągu Fibonacciego szukasz: "))

a = fib(f)

print(f," liczba ciągu Fibonacciego wynosi: ",a)