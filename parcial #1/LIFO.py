# clases

class Nodo:
    def __init__(self):
        self.info = None
        self.next = None


class Stack:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.total = 0

    def push(self, info):
        n = Nodo()

        n.info = info
        n.next = None

        if self.cabeza == None:
            self.cola = n
        else:
            n.next = self.cabeza

        self.cabeza = n

        n = None

        info = self.cabeza.info

        self.total += 1

        return info

    def pop(self):
        if self.cabeza == None and self.cola == None:
            raise ValueError("Error: Empty stack")

        copy = self.cabeza

        self.cabeza = copy.next

        info = copy.info

        del copy

        self.total -= 1

        return info

    def peek(self):
        if self.cabeza == None and self.cola == None:
            raise ValueError("Error: Empty stack")

        return self.cabeza.info

    def show(self):
        if self.cabeza != None:
            actual = self.cabeza

            while actual != None:
                print(actual.info, end="")
                actual = actual.next

            print()
        else:
            print("The stack is empty")

    def size(self):
        return self.total


pila = Stack()

# EXPRESIONES POSIBLES
# expresion = "([{((10 * 2) / 5)} / (10 * 2)] * 2)" #valida
# expresion = "((1 + 3) * {(1 + 3) / 2}" #invalida
# expresion = "([{((10 * 2) / 5)} / (10 * 2)] * 2))" #atributeError
# expresion = "({1 * 3 + 2} + 1] / (10 / 5))" #solucion punto e
# expresion = "[(10 / 5)) + (1 * 2)]" #solucion punto e
# expresion = "[(10 / A)) + (1 * 2)]" #solucion punto f
# expresion = "[(1 / 1) + (1 * 10 * 2) * X]" #solucion punto f

expresion = input("Ingrese la expresion: ")  

def validate_expression(exp):
    try:
        if exp == "":
            raise ValueError("Error: Empty expression")

        for c in exp:
            if c.isalpha():
                raise ValueError("Error: Invalid input expression")

            if c in ["(", "{", "["]:
                pila.push(c)
                pila.show()
            elif c in [")", "}", "]"]:
                value = pila.pop()

                if value == "(" and c != ")":
                    raise ValueError(f"The symbol {c} does not have a corresponding open symbol")
                elif value == "{" and c != "}":
                    raise ValueError(f"The symbol {c} does not have a corresponding open symbol")
                elif value == "[" and c != "]":
                    raise ValueError(f"The symbol {c} does not have a corresponding open symbol")

                pila.show()

        if (pila.size()) == 0:
            print("The expression is valid")
        else:
            print("The expression is invalid")
    except ValueError as e:
        print(f"Error: {e}")

validate_expression(expresion)