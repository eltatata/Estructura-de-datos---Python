class Nodo:
    def __init__(self):
        self.info = None
        self.next = None


class Pila:
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
        copy = self.cabeza

        self.cabeza = copy.next

        info = copy.info

        del copy

        self.total -= 1

        return info

    def top(self):
        print(f"El top: {self.cabeza.info}")

    def empty(self):
        if self.cabeza == None and self.cola == None:
            return True
        return False

    def len(self):
        return self.total
