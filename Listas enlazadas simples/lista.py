class Nodo:
    def __init__(self):
        self.info = None
        self.next = None
       
class SimpleList:
    def __init__(self):
        self.cabeza = None
        self.cola = None
   
    def InsertBeginning(self, info):
        n = Nodo()
       
        n.info = info
        n.next = None
       
        if self.cabeza == None:
            self.cola =  n      
        else:
            n.next = self.cabeza  
           
        self.cabeza = n
       
        n = None
   
    def insertEnd(self, info):
        n = Nodo()

        n.info = info

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
   
    def lenList(self):
        cont = 0
        
        if self.cabeza != None:
            actual = self.cabeza
           
            while actual != None:
                actual = actual.next
                cont += 1
        
        print(cont)

    def PrintList(self):
        if self.cabeza != None:
            actual = self.cabeza
           
            while actual != None:
                print(actual.info)
                actual = actual.next
                
            print()
        else:
            print("No hay nodos dentro de la lista")

# -------------------------------------------
# IMPRIMIR LISTA

lista = SimpleList()

lista.InsertBeginning("x")
lista.InsertBeginning("t")
lista.InsertBeginning("b")
lista.InsertBeginning("h")
lista.insertEnd("e")
lista.insertEnd("i")
lista.insertEnd("o")
lista.InsertBeginning("z")
lista.insertEnd("w")

lista.PrintList()

lista.deleteHead()

lista.deleteEnd()

lista.PrintList()

lista.deleteEnd()

lista.PrintList()

print()

lista.lenList()