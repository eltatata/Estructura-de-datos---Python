class Nodo:
    def __init__(self):
        self.key = None
        self.info = None
        self.next = None


class SimpleList:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def InsertBeginning(self, key, value):
        n = Nodo()

        n.key = key
        n.info = value
        n.next = None

        if self.cabeza == None:
            self.cola = n
        else:
            n.next = self.cabeza

        self.cabeza = n

        n = None

    def insertEnd(self, key, value):
        n = Nodo()

        n.key = key
        n.info = value

        self.cola.next = n

        self.cola = n

        n = None

    def deleteHead(self):
        copy = self.cabeza

        self.cabeza = copy.next

        copy = None

    def deleteEnd(self):
        if self.cabeza != None:
            actual = self.cabeza
            anterior = None

            while actual.next != None:
                anterior = actual
                actual = actual.next

            anterior.next = None

            self.cola = anterior
        else:
            print("No hay nodos dentro de la lista")

    def DeleteNodo(self, key):
        if self.cabeza != None:
            actual = self.cabeza
            anterior = None

            while actual != None:
                if actual.key == key:
                    copy = actual
                    if anterior == None:
                        self.cabeza = copy.next
                        if self.cabeza == None:
                            self.cola = None
                    else:
                        anterior.next = copy.next
                        if actual.next == None:
                            self.cola = anterior
                    del copy
                    break
                anterior = actual
                actual = actual.next

    def lenList(self):
        cont = 0

        if self.cabeza != None:
            actual = self.cabeza

            while actual != None:
                actual = actual.next
                cont += 1

        print(cont)

    def PrintList(self):
        cadena = ""

        if self.cabeza != None:
            actual = self.cabeza

            while actual != None:
                cadena += f"{actual.key}: {actual.info}, "
                actual = actual.next
        else:
            pass
            print(f"No hay nodos dentro de la lista {self.cabeza} {self.cola}")

        return cadena

    def FindNodo(self, key):
        value = None

        if self.cabeza != None:
            actual = self.cabeza

            while actual != None:
                if actual.key == key:
                    value = actual.info
                    break
                actual = actual.next

        return value

    def ReplaceNodo(self, key, value):
        if self.cabeza != None:
            actual = self.cabeza

            while actual != None:
                if actual.key == key:
                    actual.info = value
                    return True
                actual = actual.next

            return False
