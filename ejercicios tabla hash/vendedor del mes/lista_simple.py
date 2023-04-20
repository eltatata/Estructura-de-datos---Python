class Nodo:
    def __init__(self):
        self.key = None
        self.info = None
        self.next = None


class SimpleList:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insert_beginning(self, key, value):
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

    def insert_end(self, key, value):
        n = Nodo()

        n.key = key
        n.info = value

        self.cola.next = n

        self.cola = n

        n = None

    def delete_nodo(self, key):
        if self.cabeza != None:
            actual = self.cabeza
            anterior = None

            while actual != None:
                if actual.key == key:
                    copy = actual
                    if anterior == None:  # en caso se que se este eliminando la cabeza
                        self.cabeza = copy.next
                        if self.cabeza == None:  # si la lista esta vacia actualizar el puntero de la cola
                            self.cola = None
                    else:  # caso general: eliminar un nodo que no es la cabeza
                        anterior.next = copy.next
                        if actual.next == None:  # actualizar el puntero cola si el nodo eliminado era el último de la lista
                            self.cola = anterior
                    del copy
                    break
                anterior = actual
                actual = actual.next

    def print_list(self):
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

    def find_nodo(self, key):
        value = None

        if self.cabeza != None:
            actual = self.cabeza

            while actual != None:
                if actual.key == key:
                    value = actual.info
                    break
                actual = actual.next

        return value

    def replace_value(self, key, value):
        if self.cabeza != None:
            actual = self.cabeza

            while actual != None:
                if actual.key == key:
                    actual.info += value
                    return True
                actual = actual.next

            return False
