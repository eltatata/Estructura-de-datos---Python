from lista_simple import SimpleList


class TablasHash:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.tabla = [None] * capacidad

    def hash(self, llave):
        return hash(llave) % self.capacidad

    def set(self, llave, valor):
        hash_indice = self.hash(llave)

        if self.tabla[hash_indice] == None:
            lista = SimpleList()

            lista.InsertBeginning(llave, valor)

            self.tabla[hash_indice] = lista
        else:
            # buscar el nodo por medio de el key en la lista que desprende de el espacio en la tabla
            lista = self.tabla[hash_indice]
            nodo = lista.FindNodo(llave)

            if nodo != None:
                lista.ReplaceNodo(llave, valor)
            else:
                self.tabla[hash_indice].insertEnd(llave, valor)

            # self.tabla[hash_indice].insertEnd(llave, valor)

    def get(self, llave):
        valor = None
        hash_indice = self.hash(llave)

        if self.tabla[hash_indice] != None:
            lista = self.tabla[hash_indice]
            valor = lista.FindNodo(llave)

        return valor

    def show(self):
        cadena = ""
        for i in self.tabla:
            if i != None:
                cadena += f"{i.PrintList()}"
        print("{" + cadena + "}")

    def delete(self, llave):
        hash_indice = self.hash(llave)

        self.tabla[hash_indice].DeleteNodo(llave)

        if self.tabla[hash_indice].cola == None and self.tabla[hash_indice].cabeza == None:
            self.tabla[hash_indice] = None


tabla = TablasHash(10)

tabla.set("Hola", 13)
tabla.set("Juan", 8)
tabla.set("David", 777)
tabla.set("Maria", 23)
tabla.set("Mariana", 43)
tabla.set("Pedro", 63)
tabla.set("Mariana", 666)
tabla.set("David", 777888)

print(tabla.hash("Hola"))
print(tabla.hash("Juan"))
print(tabla.hash("David"))
print(tabla.hash("Maria"))
print(tabla.hash("Mariana"))
print(tabla.hash("Pedro"))

print(tabla.tabla)

valorClave = tabla.get("David")
print(f"\nEl valor de clave es: {valorClave}\n")

tabla.show()

tabla.delete("Maria")

tabla.show()

print()

print(tabla.tabla)

# tabla.tabla[1].PrintList()
