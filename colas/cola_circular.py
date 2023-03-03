class ColaCiruclar:
    def __init__(self, tamaño):
        self.q = [None] * tamaño
        self.frente = 0
        self.final = -1

    def insert(self, e):
        if self.frente == 0 and self.final == len(cola.q) - 1:
            print("Cola llena")
        elif self.frente != 0 and self.frente - 1 == self.final:
            print("Cola llena")
        elif self.final == len(cola.q) - 1:
            self.q[0] = e

            self.final = 0
        else:
            self.q[self.final + 1] = e

            self.final += 1

    def remove(self):
        e = self.q[self.frente]

        self.q[self.frente] = None

        self.frente += 1

        return e


cola = ColaCiruclar(4)

cola.insert("A")

print(cola.q, cola.frente, cola.final)

cola.insert("B")

print(cola.q, cola.frente, cola.final)

cola.insert("C")

print(cola.q, cola.frente, cola.final)

cola.insert("D")

print(cola.q, cola.frente, cola.final)

cola.insert("E")

cola.remove()
cola.remove()

print(cola.q, cola.frente, cola.final)

cola.insert("E")

print(cola.q, cola.frente, cola.final)

cola.insert("F")

print(cola.q, cola.frente, cola.final)

cola.insert("G")

print(cola.q, cola.frente, cola.final)

cola.remove()

print(cola.q, cola.frente, cola.final)

cola.insert("H")

print(cola.q, cola.frente, cola.final)

cola.insert("I")

print(cola.q, cola.frente, cola.final)