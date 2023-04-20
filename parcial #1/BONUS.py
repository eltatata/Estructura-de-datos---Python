class Nodo:  # contructor de la clase
    def __init__(self):
        self.informacion = None
        self.siguiente = None
        self.anterior = None


class listadoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    # a) Insertar Nodo al principio de la lista
    def InsertarPrincipio(self, info):
        n = Nodo()
        n.informacion = info
        n.anterior = None
        if self.cabeza == None:
            n.siguiente = None
            self.cabeza = n
            self.cola = n
        else:
            n.siguiente = self.cabeza
            self.cabeza.anterior = n
            self.cabeza = n

    # b) Insertar un nodo a final de la lista.
    def InsertarFinal(self, info):
        actual = self.cola
        n = Nodo()
        n.informacion = info
        n.siguiente = None
        n.anterior = actual
        actual.siguiente = n
        self.cola = n

    #  c) Eliminar cualquier nodo de la lista. Validar situaciones de primer nodo, ultimo nodo y único nodo de la lista.
    def EliminarNodo(self, info):
        actual = self.cabeza
        while actual != None:
            if actual.informacion == info:
                if actual.anterior == None and actual.siguiente == None:
                    dup = actual
                    dup.siguiente = None
                    dup.anterior = None
                    self.cabeza = None
                    self.cola = None
                    dup = None
                    print("Era el unico nodo. La lista quedo vacia")
                elif actual.anterior == None:
                    dup = actual
                    dup.siguiente.anterior = None
                    self.cabeza = dup.siguiente
                    dup.siguiente = None
                    dup = None
                elif actual.siguiente == None:
                    dup = actual
                    dup.anterior.siguiente = None
                    self.cola = dup.anterior
                    dup.anterior = None
                    dup = None
                elif actual.anterior != None and actual.siguiente != None:
                    dup = actual
                    dup.siguiente.anterior = dup.anterior
                    dup.anterior.siguiente = dup.siguiente
                    dup.anterior = None
                    dup.siguiente = None
                    dup = None
            actual = actual.siguiente

    # d) d. Mostrar el contenido de cada uno de los nodos de la lista.
    def ImprimirLista(self):
        if self.cabeza != None:
            actual = self.cabeza
            while actual != None:
                print(actual.informacion)
                actual = actual.siguiente

    # e) e. Mostrar la lista en orden inverso.
    def ImprimirListaInverso(self):
        if self.cola != None:
            actual = self.cola
            while actual != None:
                print(actual.informacion)
                actual = actual.anterior

    # f) Insertar un nodo en cualquier parte de la lista: antes o después de cierto nodo.
    def InsertarNodoUbicado(self, info):
        d = {1: "1. Ingresar nodo antes",
             2: "2. Ingresar nodo después"}
        for k in d:
            print(d[k])
        opcion = int(input("Seleccione una opcion: "))
        info = input(f"Deseas ingresar {opcion}  de que nodo ? ")
        n = Nodo()
        n.informacion = info
        actual = self.cabeza
        while actual != None:
            if actual.informacion == info:
                if opcion == 1:
                    dup = actual.anterior
                    n.siguiente = actual
                    n.anterior = dup
                    dup.siguiente = n
                    actual.anterio = n
                elif opcion == 2:
                    dup = actual.siguiente
                    n.siguiente = dup
                    n.anterior = actual
                    actual.siguiente = n
                    dup.anterior = n
        actual = actual.siguiente

    # g) Ordenar la lista ascendentemente. Implemente cualquier algoritmo de ordenamiento de datos.
    def OrdenarLista(self):
        actual = self.cabeza
        while actual != None:
            if actual.informacion > actual.siguiente.informacion:
                dup = actual.anterior
                ant = actual.siguiente
                actual.siguiente = dup
                actual.anterior = dup.anterior
                ant.anterior = dup
                dup.siguiente = ant
                dup.anterior = actual
                dup = None
                ant = None
        actual = actual.siguiente

    # h) Insertar un nodo manteniendo el orden de la lista. La lista ha sido ordenada previamente y cualquier inserción debe garantizar el orden actual de la lista.
    def InsertarNodoOrdenado(self, info):
        n = Nodo()
        n.informacion = info
        actual = self.cabeza
        while actual != None:
            if actual.informacion >= n.informacion:
                dup = actual.siguiente
                n.siguiente = dup
                n.anterio = actual
                dup.anterior = n
                actual.siguiente = n
        actual = actual.siguiente


lista = listadoble()

# menu
d = {1: "1. Ingresar nodo al principio",
     2: "2. Ingresar nodo al final",
     3: "3. Eliminar nodo",
     4: "4. Mostrar lista",
     5: "5. Mostrar lista inversa",
     6: "6. Insertar nodo", # ERROR
     7: "7. Ordenar Lista", # ERROR
     8: "8. Insertar nodo en orden", # ERROR
     9: "9. Salir"}

print("MENÚ DE OPCIONES")

for k in d:
    print(d[k])

print(" ")

while True:
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        info = input("Ingrese info: ")
        lista.InsertarPrincipio(info)
    elif opcion == 2:
        info = input("Ingrese info: ")
        lista.InsertarFinal(info)
    elif opcion == 3:
        info = input("Ingrese info: ")
        lista.EliminarNodo(info)
    elif opcion == 4:
        lista.ImprimirLista()
    elif opcion == 5:
        lista.ImprimirListaInverso()
    elif opcion == 6:
        info = input("Ingrese info: ")
        lista.InsertarNodoUbicado(info)
    elif opcion == 7:
        lista.OrdenarLista()
    elif opcion == 8:
        info = input("Ingrese info: ")
        lista.InsertarNodoOrdenado(info)
    elif opcion == 9:
        break
