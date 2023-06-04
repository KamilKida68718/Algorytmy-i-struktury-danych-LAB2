"""Zaproponuj algorytm sprawdzania poprawności różnych symboli. """

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
        if symbol =="(" or symbol == "{" or symbol == "["  :
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
print(parCheker('(([()])))})))'))
print(parCheker('((({()}[])()))'))