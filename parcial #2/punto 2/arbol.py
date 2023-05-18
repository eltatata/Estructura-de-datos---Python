from cola import ColaCiruclar
from pila import Stack


class nodo_arbol:
    def __init__(self):
        self.informacion = None
        self.izq = None
        self.dere = None


class arbol_binario:
    def __init__(self):
        self.raiz = None
        self.num_nodos = 0

    def insertar(self, informacion):
        n = nodo_arbol()

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

        self.num_nodos += 1

    def insertar_izquierda(self, nodo_padre, informacion):
        n = nodo_arbol()

        n.informacion = informacion
        n.izq = None
        n.dere = None

        if self.raiz == None:
            self.raiz = n
        else:
            actual = self.raiz
            padre = None

            while actual != None:
                padre = actual
                actual = actual.izq

            padre.izq = n

        self.num_nodos += 1

    def insertar_derecha(self, nodo_padre, informacion):
        n = nodo_arbol()

        n.informacion = informacion
        n.izq = None
        n.dere = None

        if self.raiz == None:
            self.raiz = n
        else:
            actual = self.raiz
            padre = None

            while actual != None:
                padre = actual
                actual = actual.dere

            padre.dere = n

        self.num_nodos += 1

    def preorden_recursivo(self, r):
        if r != None:
            print(r.informacion, end=" ")
            self.preorden_recursivo(r.izq)
            self.preorden_recursivo(r.dere)

    def preorden(self, r):
        pila = Stack()

        nodo = r

        while True:

            while nodo is not None:
                print(nodo.informacion, end=" ")
                pila.push(nodo)
                nodo = nodo.izq

            if pila.size() == 0:
                break

            nodo_eliminado = pila.pop()
            nodo = nodo_eliminado.dere

    def inorden_recursivo(self, r):
        if r != None:
            self.inorden_recursivo(r.izq)
            print(r.informacion, end=" ")
            self.inorden_recursivo(r.dere)

    def inorden(self, r):
        pila = Stack()

        # se hace a el nodo igual a la raiz
        nodo = r

        while True:
            # cuando nodo = nodo.izq --> None se hace del while secundario
            # o
            # cuando nodo = None se hace del while secundario
            while nodo is not None:
                pila.push(nodo)
                nodo = nodo.izq

            # si la pila no esta vacia se sigue el en while principal
            if pila.size() == 0:
                break

            # se hace pop
            nodo_eliminado = pila.pop()
            # se imprime el nodo eliminado
            print(nodo_eliminado.informacion, end=" ")
            # y hace el nodo == a el nodo.dere de el nodo eliminado
            nodo = nodo_eliminado.dere

    def postorden_recursivo(self, r):
        if r != None:
            self.postorden_recursivo(r.izq)
            self.postorden_recursivo(r.dere)
            print(r.informacion, end=" ")

    def amplitud(self, r):
        cola = ColaCiruclar()
        cola.enque(r)

        while cola.size() > 0:
            nodo = cola.deque()

            print(nodo.informacion, end=" ")

            if nodo.izq != None:
                cola.enque(nodo.izq)

            if nodo.dere != None:
                cola.enque(nodo.dere)

    def profundidad(self, r):
        pila = Stack()

        pila.push(r)

        while pila.cabeza != None:
            nodo = pila.pop()

            print(nodo.informacion, end=" ")

            if nodo.dere != None:
                pila.push(nodo.dere)

            if nodo.izq != None:
                pila.push(nodo.izq)

    def nivel_profundidad(self, r):
        cola = ColaCiruclar()
        profundidad = 0

        cola.enque(r)

        while cola.size() > 0:
            n = cola.size()

            print(f"{profundidad})", end=" ")

            for i in range(n):
                nodo = cola.deque()

                print(nodo.informacion, end=" ")

                if nodo.izq != None:
                    cola.enque(nodo.izq)

                if nodo.dere != None:
                    cola.enque(nodo.dere)

            profundidad += 1

            print()

        print(f"El nivel de profundidad es: {profundidad}")

    def buscar(self, r, informacion):
        actual = r

        while actual != None:
            # print(actual.informacion, informacion)

            if actual.informacion == informacion:
                return True
            elif informacion > actual.informacion:
                actual = actual.dere
            else:
                actual = actual.izq

        return False

    def eliminar(self, r, informacion):
        actual = r
        padre = None
        nodo_elminar = None

        res = self.buscar(r, informacion)

        if res is not True:
            print(f"{informacion} No esta dentro de el arbol")
            return False

        while actual.informacion != informacion:

            # print(actual.informacion, informacion)

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

        # case en el que el nodod a eliminar no tenga hijos
        if nodo_elminar.izq == None and nodo_elminar.dere == None:
            if informacion < padre.informacion:
                padre.izq = None
            else:
                padre.dere = None

        # caso #1: si el nodo a eliminar no
        # tiene hijos a la izquierda, pero si tiene a la derecha.
        # se junta al padre con el nodo hijo de la derecha de el nodo a eliminar
        elif nodo_elminar.izq == None and nodo_elminar.dere != None:
            print("Se esta eliminando el noto, por el metodo 1...")

            # print(f"el padre de {nodo_elminar.informacion} es {padre.informacion}")
            print(f"(p): {padre.informacion}")
            print(f"(e): {nodo_elminar.informacion}")
            print(f"(r): {nodo_elminar.dere.informacion}")

            # si el nodo padre de el nodo a eliminar es la raiz
            # y la informacion de el nodo a eliminar es mayor que el padre(raiz)
            if padre.informacion == self.raiz.informacion and nodo_elminar.informacion > padre.informacion:
                # se hace padre.dere = nodo_elminar.dere
                padre.dere = nodo_elminar.dere
            else:
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
            print(f"(hi): {hi.informacion}")

            # 1) cambiar valores de el nodo a eliminar con el valor de (r)
            nodo_elminar.informacion = r.informacion
            pr.dere = hi  # 2) conectar pr con hi (r.izq)
            del r  # 3) eliminar r

            print("Se elimino por el metodo 2")

        self.num_nodos -= 1
