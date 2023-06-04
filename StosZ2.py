"""Zapoznaj się z poniższym algorytmem sprawdzania poprawności nawiasów i zaproponuj
jego rozwiązanie (implementacja w Python oraz schemat blokowy).
W większości zastosowań liczba nawiasów musi być zbilansowana, tzn. powinno być tyle samo
prawych co lewych nawiasów. Ponadto, nawiasy muszą być poprawnie zagnieżdżone:
(()()()())
(((())))
(()((())()))
Dla porównania, poniżej znajduje się kilka przykładów niepoprawnych nawiasów:
((((((())
()))
(()()(()
Sprawdzanie poprawności nawiasów w różnych wyrażeniach to jedno z częstych i ważnych zadań, z
którym muszą uporać się programiści. Naszym celem będzie teraz uporanie się z tym problemem przy
użyciu stosu. Zauważmy przede wszystkim że w sekwencji nawiasów pierwszy z nawiasów
zamykających musi pasować do ostatniego nawiasu otwierającego. Podobnie, pierwszy z nawiasów
otwierających musi "czekać" do ostatniego nawiasu zamykającego. Innymi słowy, nawiasy zamykające
powinny pasować do otwierających w odwrotnym porządku.
Z tego właśnie powodu stos wydaje się być strukturą odpowiednią do rozwiązania tego zagadnienia. Po
wybraniu struktury reszta algorytmu jest prosta:
1. Rozpocznij z pustym stosem.
2. Wczytaj ciąg znaków z nawiasami.
3. Przetwarzaj ciąg idąc od lewej do prawej.
4. Jeśli aktualny znak jest nawiasem otwierającym, wstaw go na stos.
5. Jeśli aktualny znak jest nawiasem zamykającym, ściągnij nawias otwierający z wierzchołka
stosu.
6. Jeśli po dojściu do końca ciągu stos jest pusty i nie wystąpiły żadne błędy, nawiasy są poprawne.
"""

class Stack:
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    




def parCheker(symbolString):
    s = Stack()
    index = 0
    error  = True

    while index <len(symbolString) and error:
        symbol = symbolString[index]
        if symbol =="(":
            s.push(symbol)
        else:
            if s.isEmpty():
                error = False
            else:
                s.pop()
        index += 1
    if error and s.isEmpty:
        return True
    else:
        return False





print(parCheker('((()))'))
print(parCheker('((())))))))'))
print(parCheker('((()()()))'))