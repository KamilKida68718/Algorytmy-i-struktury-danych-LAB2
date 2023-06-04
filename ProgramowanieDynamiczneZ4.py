"""Korzystając z techniki programowania dynamicznego ułóż algorytm wyznaczania
współczynnika dwumianowego"""


def wDwu(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return wDwu(n - 1, k - 1) + wDwu(n - 1, k)


d = int(input("Podaj `n` element: "))
t = int(input("Podaj `m` elememt: "))

a = wDwu(d, t)

print("Wsółczynnik dwuwymiarowy dla 'n' równego: ",d," i 'm' równego: ",t," wynosi :", a)
