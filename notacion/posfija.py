from modelo_pila import Pila
expresionPosfija = "6 2 3 + - 3 8 2 / + * 2 ** 3 +"

# utilizando listas de python y la funcion eval()

# pila = list()

# for simbolo in expresionPosfija.split():
#     if simbolo in ["**", "*", "/", "+", "-"]:
#         val1 = pila.pop()
#         val2 = pila.pop()

#         print(f"operacion = {val2} {simbolo} {val1}\n")

#         res = eval(f"{val2} {simbolo} {val1}")

#         pila.append(res)
#     else:
#         pila.append(simbolo)

#     print(pila)
# -----------------------------------------------------------------------------------------------
# utlizando la clase de el modulos pila.py

pila = Pila()

for simbolo in expresionPosfija.split():
    if simbolo in ["**", "*", "/", "+", "-"]:
        val1 = pila.pop()
        val2 = pila.pop()

        print(f"operacion = {val2} {simbolo} {val1}\n")

        res = eval(f"{val2} {simbolo} {val1}")

        print(pila.push(res))
    else:
        val = pila.push(simbolo)
        
        print(val)