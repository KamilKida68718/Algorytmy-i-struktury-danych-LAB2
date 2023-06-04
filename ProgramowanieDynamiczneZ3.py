"""Dany jest ciąg o wyrazie ogólnym
S(n)
Zaproponuj algorytm obliczania n-tego wyrazu tego ciągu, wykorzystujący metodę programowania
dynamicznego."""


def S(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n > 1:
        return 2*S(n-1) - S(n-2)


m = int(input("Podaj n element ciągu: "))

a = S(m)

print(m, " wyraz ciągu wynosi: ", a)
