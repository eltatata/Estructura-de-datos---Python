# clases

class Nodo:
    def __init__(self):
        self.info = None
        self.next = None


class Stack:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.total = 0

    def push(self, info):
        n = Nodo()

        n.info = info
        n.next = None

        if self.cabeza == None:
            self.cola = n
        else:
            n.next = self.cabeza

        self.cabeza = n

        n = None

        info = self.cabeza.info

        self.total += 1

        return info

    def pop(self):
        if self.cabeza == None and self.cola == None:
            raise ValueError("Error: Empty stack")

        copy = self.cabeza

        self.cabeza = copy.next

        info = copy.info

        del copy

        self.total -= 1

        return info

    def peek(self):
        if self.cabeza == None and self.cola == None:
            raise ValueError("Error: Empty stack")

        return self.cabeza.info

    def show(self):
        if self.cabeza != None:
            actual = self.cabeza

            while actual != None:
                print(f"{actual.info} ", end="")
                actual = actual.next

            print()
        else:
            print("The stack is empty")

    def size(self):
        return self.total