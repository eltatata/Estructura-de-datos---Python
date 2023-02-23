# Escriba un programa en Python que dibuje la bandera inglesa 
# usando únicamente los caractéres0 y +. 
# Considere banderas con un largo L (cantidad de caracteres horizontales) 
# y un alto H (cantidad de caracteres verticales) 
# siendo ambos valores impares mayores a 2 y menores a 20.

l = int(input())
h = int(input())

if l % 2 != 0 and h % 2 != 0 and l > 2 and h < 20:
    for i in range(h):
        if i + 1== h / 2 + 0.5:
            for i in range(l):
                print("+", end="")
        else:
            for i in range(l):
                if i + 1 == l / 2 + 0.5:
                    print("+", end="")
                else:
                    print("0", end="")
        print()