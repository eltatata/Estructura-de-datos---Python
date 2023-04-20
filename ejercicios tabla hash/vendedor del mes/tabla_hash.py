from lista_simple import SimpleList


class TablaHash:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.tabla = [None] * capacidad
        self.winner = None

    def hash(self, key):
        return hash(key) % self.capacidad

    def set(self, key, value):
        hash_indice = self.hash(key)

        if self.tabla[hash_indice] == None:
            lista = SimpleList()

            lista.insert_beginning(key, value)

            self.tabla[hash_indice] = lista
        else:
            # buscar el nodo por medio de el key en la lista que desprende de el espacio en la tabla
            lista = self.tabla[hash_indice]
            nodo = lista.find_nodo(key)

            if nodo != None:
                lista.replace_value(key, value)
            else:
                self.tabla[hash_indice].insert_end(key, value)

            # self.tabla[hash_indice].insert_end(key, value)
        
    def delete(self, key):
        hash_indice = self.hash(key)

        self.tabla[hash_indice].delete_nodo(key)

        if self.tabla[hash_indice].cola == None and self.tabla[hash_indice].cabeza == None:
            self.tabla[hash_indice] = None

    def get(self, key):
        nodo = None
        hash_indice = self.hash(key)

        if self.tabla[hash_indice] != None:
            lista = self.tabla[hash_indice]
            nodo = lista.find_nodo(key)

        return nodo
    
    def get_winner():
        pass

    def show(self):
        cadena = ""
        for i in self.tabla:
            if i != None:
                cadena += f"{i.print_list()}"
        print("{" + cadena + "}")
