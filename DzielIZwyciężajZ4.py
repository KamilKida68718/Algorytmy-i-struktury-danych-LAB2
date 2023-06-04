"""Dana jest tablica n liczb całkowitych. Przedstaw algorytm liczący sumę elementów w
tablicy z zastosowaniem metody „dziel i zwyciężaj”."""

def QuickSort (l, r, A):

    if (r == l + 1):
        return A[l]+A[r]
    elif l == r:
        return A[l]
    
    p = int((l + r)/2)

    suma = 0

    suma = suma + QuickSort(l, p, A)
    suma = suma + QuickSort(p + 1, r, A)

    return suma



lista = [44,6,10,25]

a = QuickSort(0, len(lista)-1, lista)

print("Suma elementów tablicy: ",a)



