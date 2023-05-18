class nodo:
    def __init__(self):
        self.informacion = None
        self.izq = None
        self.dere = None


class arbol_binario:
    def __init__(self):
        self.raiz = None

    def insertar(self, informacion):
        n = nodo()

        n.informacion = informacion
        n.izq = None
        n.dere = None

        if self.raiz == None:
            self.raiz = n
        else:
            actual = self.raiz
            padre = None

            while actual != None:
                if n.informacion > actual.informacion:
                    padre = actual
                    actual = actual.dere
                else:
                    padre = actual
                    actual = actual.izq

            if n.informacion > padre.informacion:
                padre.dere = n
            else:
                padre.izq = n

    def prorden_recursivo(self, r):
        if r != None:
            print(r.informacion)
            self.prorden_recursivo(r.izq)
            self.prorden_recursivo(r.dere)
           
    def inorden_recursivo(self, r):
        if r != None:
            self.inorden_recursivo(r.izq)
            print(r.informacion)
            self.inorden_recursivo(r.dere)
           
    def postorden_recursivo(self, r):
        if r != None:
            self.postorden_recursivo(r.izq)
            self.postorden_recursivo(r.dere)
            print(r.informacion)

arbol = arbol_binario()

arbol.insertar(100)

arbol.insertar(51)
arbol.insertar(120)

arbol.insertar(43)
arbol.insertar(60)
arbol.insertar(112)
arbol.insertar(131)

arbol.insertar(40)
arbol.insertar(45)
arbol.insertar(59)
arbol.insertar(70)
arbol.insertar(110)
arbol.insertar(123)
arbol.insertar(140)

arbol.insertar(50)
arbol.insertar(90)

# LA VISUALIZACION QUE HACE CON PYTHON TUTOR

arbol.prorden_recursivo(arbol.raiz)
print()
arbol.inorden_recursivo(arbol.raiz)
print()
arbol.postorden_recursivo(arbol.raiz)