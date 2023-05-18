from cola import ColaCiruclar
from pila import Stack


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

    def amplitud(self, r):
        cola = ColaCiruclar()

        cola.enque(r)

        while cola.size() > 0:
            nodo = cola.deque()

            print(nodo.informacion)

            if nodo.izq != None:
                cola.enque(nodo.izq)

            if nodo.dere != None:
                cola.enque(nodo.dere)

    def profundidad(self, r):
        pila = Stack()

        pila.push(r)

        while pila.cabeza != None:
            nodo = pila.pop()

            print(nodo.informacion)

            if nodo.dere != None:
                pila.push(nodo.dere)

            if nodo.izq != None:
                pila.push(nodo.izq)

    def eliminar(self, r, informacion):
        actual = r
        padre = None
        nodo_elminar = None

        while actual.informacion != informacion:

            print(actual.informacion, informacion)

            if informacion > actual.informacion:
                padre = actual
                actual = actual.dere
            else:
                padre = actual
                actual = actual.izq

        if informacion == actual.informacion:
            nodo_elminar = actual
        elif informacion > padre.informacion:
            nodo_elminar = padre.dere
        else:
            nodo_elminar = padre.izq

        # caso #1: si el nodo a eliminar no tiene hijos a la izquierda, pero si tiene a la derecha.
        # se junta al padre con el nodo hijo de la derecha de el nodo a eliminar
        if nodo_elminar.izq == None and nodo_elminar.dere != None:
            print("Se esta eliminando el noto, por el metodo 1...")

            padre.izq = nodo_elminar.dere

            del nodo_elminar

            print("Se elimino por el metodo 1")

        # caso #2: si el nodo tiene hijo a la izquierda,
        # se tiene que preguntar si ese hijo tiene hijo a la derecha
        # elif nodo_elminar.izq != None: 
        else:      
            print("Se esta eliminando el noto, por el metodo 2...")

            # (e) = nodo_eliminar
            print(f"(e): {nodo_elminar.informacion}")

            pr = nodo_elminar.izq
            
            # verificar si se cumple la variacion en el caso 2
            if pr.dere == None and pr.izq != None:
                pr = nodo_elminar
            
            print(f"(pr): {pr.informacion}")

            r = pr.dere
            print(f"(r): {r.informacion}")
            
            hi = r.izq

            # 1) cambiar valores de el nodo a eliminar con el valor de (r)
            nodo_elminar.informacion = r.informacion
            pr.dere = hi  # 2) conectar pr con hi (r.izq)
            del r  # 3) eliminar r

            print("Se elimino por el metodo 2")


# arbol1 = arbol_binario()

# arbol1.insertar(101)

# arbol1.insertar(50)
# arbol1.insertar(110)

# arbol1.insertar(45)
# arbol1.insertar(56)
# arbol1.insertar(105)
# arbol1.insertar(120)

# arbol1.insertar(30)
# arbol1.insertar(55)
# arbol1.insertar(108)
# arbol1.insertar(121)

# arbol1.amplitud(arbol1.raiz)

# print()

# arbol2 = arbol_binario()

# arbol2.insertar(100)

# arbol2.insertar(80)
# arbol2.insertar(110)

# arbol2.insertar(70)
# arbol2.insertar(85)
# arbol2.insertar(105)
# arbol2.insertar(120)

# arbol2.insertar(60)
# arbol2.insertar(81)
# arbol2.insertar(108)
# arbol2.insertar(130)

# arbol2.profundidad(arbol2.raiz)


arbol3 = arbol_binario()

# caso1

# arbol3.insertar(20)

# arbol3.insertar(10)
# arbol3.insertar(40)

# arbol3.insertar(16)
# arbol3.insertar(30)
# arbol3.insertar(80)

# arbol3.insertar(27)
# arbol3.insertar(50)

# arbol3.eliminar(arbol3.raiz, 10)
# arbol3.inorden_recursivo(arbol3.raiz)
# --------------------------
# caso1

# arbol3.insertar(8)

# arbol3.insertar(5)
# arbol3.insertar(20)

# arbol3.insertar(3)
# arbol3.insertar(6)
# arbol3.insertar(15)

# arbol3.insertar(10)
# arbol3.insertar(18)

# arbol3.insertar(16)

# arbol3.insertar(17)

# arbol3.eliminar(arbol3.raiz, 16)
# arbol3.inorden_recursivo(arbol3.raiz)
# --------------------------
# caso2

# arbol3.insertar(8)

# arbol3.insertar(5)
# arbol3.insertar(20)

# arbol3.insertar(3)
# arbol3.insertar(6)
# arbol3.insertar(15)

# arbol3.insertar(10)
# arbol3.insertar(18)

# arbol3.insertar(16)

# arbol3.insertar(17)

# arbol3.eliminar(arbol3.raiz, 18)
# arbol3.inorden_recursivo(arbol3.raiz)
# --------------------------
# caso2

# arbol3.insertar(20)

# arbol3.insertar(10)
# arbol3.insertar(40)

# arbol3.insertar(16)
# arbol3.insertar(30)
# arbol3.insertar(80)

# arbol3.insertar(14)
# arbol3.insertar(27)
# arbol3.insertar(50)

# arbol3.eliminar(arbol3.raiz, 20)
# arbol3.inorden_recursivo(arbol3.raiz)
# --------------------------
# caso2 y variacion

# arbol3.insertar(20)

# arbol3.insertar(10)
# arbol3.insertar(40)

# arbol3.insertar(16)
# arbol3.insertar(30)
# arbol3.insertar(80)

# arbol3.insertar(27)
# arbol3.insertar(50)

# arbol3.eliminar(arbol3.raiz, 40)
# arbol3.inorden_recursivo(arbol3.raiz)