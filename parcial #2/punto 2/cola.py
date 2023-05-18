class ColaCiruclar:
    def __init__(self):
        self.q = [None] * 10
        self.frente = 0
        self.final = -1
        self.tamaño = 0

    def enque(self, e):
        if self.frente == 0 and self.final == len(self.q) - 1:
            print("COLA LLENA 1")
        elif self.frente != 0 and self.frente - 1 == self.final:
            print("COLA LLENA 2")
        elif self.final == len(self.q) - 1:
            self.q[0] = e

            self.final = 0

            self.tamaño += 1
        else:
            self.q[self.final + 1] = e

            self.final += 1

            self.tamaño += 1

    def deque(self):
        if (self.tamaño == 0):
            return "No se puede eliminar cola vacia"

        # si se elimina al unico cliente de la fila se hace reset a las posiciones
        if (self.tamaño == 1):
            e = self.q[self.frente]

            self.q[self.frente] = None

            self.frente = 0
            self.final = -1

            self.tamaño -= 1
        else:
            e = self.q[self.frente]

            self.q[self.frente] = None

            self.frente += 1

            self.tamaño -= 1

            # si se elimino al primero de la lista y
            # este estaba en la posicion 9 de la lista
            # hacer reset de frente y hacer igual a 0
            if self.frente == 10:
                self.frente = 0

        return e

    def size(self):
        return self.tamaño