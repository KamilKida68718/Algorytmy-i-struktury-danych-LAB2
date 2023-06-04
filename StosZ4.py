"""Napisz program czytający wyrażenie arytmetyczne w notacji postfiksowej (Odwrotna
Notacja Polska) i obliczający jego wartość z wykorzystaniem stosu.
ONP (ang. RPN - Reverse Polish Notation) jest sposobem zapisu wyrażeń arytmetycznych bez
stosowania nawiasów, w którym symbol operacji występuje po argumentach. Poniżej podajemy
przykłady wyrażeń w ONP:
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]


def operations(line):
    stack = Stack()
    index = 0

    while index < len(line):
        symbol = line[index]

        if symbol == '+':
            z1 = stack.pop()
            z2 = stack.pop()

            dz = z1 + z2

            stack.push(dz)

            index += 1

        elif symbol == '-':
            z1 = stack.pop()
            z2 = stack.pop()

            dz = z1 - z2

            stack.push(dz)

            index += 1

        elif symbol == '*':
            z1 = stack.pop()
            z2 = stack.pop()

            dz = z1 * z2

            stack.push(dz)

            index += 1

        elif symbol == '/':
            z1 = stack.pop()
            z2 = stack.pop()

            dz = z2 / z1

            stack.push(dz)

            index += 1

        elif symbol == '^':
            z1 = stack.pop()
            z2 = stack.pop()

            dz = z2 ** z1

            stack.push(dz)

            index += 1

        elif symbol == '=':
            return stack.peek()

        else:
            lic = int(symbol)
            stack.push(lic)

            index += 1


p = '73+52-2^*='

print(operations(p))
