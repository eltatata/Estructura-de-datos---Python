from lista_simple import SimpleList

class TablaHash:
    def __init__(self, n):
        self.tamaño = n
        self.tabla = [None] * n
   
    def f(self, K):
        # HASH PROPIO
        suma = 0

        for c in K:
            suma += ord(c)

        # HASH PYTHON
        # suma = hash(K)

        # if suma < 0:
        #     suma *= -1
       
        return suma % self.tamaño
   
    def set(self, V):
        posicion = self.f(V)

        L = SimpleList()

        if self.tabla[posicion] == None:
            L.InsertBeginning(V)
            self.tabla[posicion] = L
        else:
            self.tabla[posicion].insertEnd(V)
       
        self.tabla[posicion].PrintList()

    def get(self, V):
        posicion = self.f(V)

        return posicion

t = TablaHash(10)
t.set("Hola")
t.set("Juan")
t.set("David")
t.set("david")
t.set("leidy")

print(t.f("Hola"))
print(t.f("Juan"))
print(t.f("David"))
print(t.f("david"))
print(t.f("leidy"))

print(t.tabla)

print()

t.tabla[8].PrintList()
