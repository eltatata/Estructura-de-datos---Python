class ColaCiruclar:
    def __init__(self, tamaño):
        self.q = [None] * tamaño
        self.frente = 0
        self.final = -1

    def insert(self, e):
        if self.frente == 0 and self.final == len(cola.q) - 1:
            print("Cola llena")
        else:
            self.q[self.final + 1] = e
           
            self.final += 1
       
        if self.final == len(cola.q) - 1:
            self.q[self.final + 1] = e

            self.final += 1

    def remove(self):
        e = self.q[self.frente]

        self.q[self.frente] = None

        self.frente += 1

        return e


cola = ColaCiruclar(4)

cola.insert("A")
cola.insert("B")
cola.insert("C")
cola.insert("D")

print(cola.q, cola.frente, cola.final)

cola.insert("E") #cola llena

cola.remove()
cola.remove()

print(cola.q, cola.frente, cola.final)

# cola.insert("F")

# print(cola.q, cola.frente, cola.final)