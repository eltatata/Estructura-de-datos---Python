from modelo_pila import Pila

pila = Pila()

ecuacion = input()


def validar_exprecion():
    if ecuacion == "":
        print("Expresion no valida")
    else:
        for caracter in ecuacion:
            if caracter == "(" or caracter == "{" or caracter == "[":
                pila.push(caracter)
            elif caracter == ")" or caracter == "}" or caracter == "]":
                if pila.empty():
                    return False
                else:
                    try:
                        value = pila.pop()

                        if value == "(" and caracter == ")":
                            pass
                        elif value == "{" and caracter == "}":
                            pass
                        elif value == "[" and caracter == "]":
                            pass
                        else:
                            return False
                    except:
                        return False

        if pila.len() == 0:
            return True
        else:
            return False

res = validar_exprecion()

if res:
    print("Exprecion valida")
else:
    print("Exprecion invalida")