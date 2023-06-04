"""Zadanie 3. Stosując metodę "dziel i zwyciężaj", ułóż algorytm wyznaczania największego elementu
wektora."""



def QuickSort(l, r, A):
    if l >= r:
        return A
    
    v = A[r]
    p = l

    temp1 = 0
    temp2 = 0

    for i in range(len(A)):

        if A[i] < v:

            temp1 = A[p]
            A[p] = A[i]
            A[i] = temp1
            p = p + 1

    
    temp2 = A[p]
    A[p] = A[r]
    A[r] = temp2

    QuickSort(l, p -1, A)
    QuickSort(p + 1, r, A)

    return A[-1]


L = [1,2,33,4,53231312313123,22,33,42,241]

a = QuickSort(0,len(L)-1, L)

print("Największy element wektora: ",a)
    


