import msvcrt
import time
from arbol import arbol_binario

while True:
    print("Presiones |Enter| para crear un nuevo arbol, o |escape| tecla para salir")
    if msvcrt.getch() == b'\x1b':
        print("Saliendo del el programa...")
        time.sleep(1)
        break
    else:
        print("Inicializando arbol binario...")
        time.sleep(1)

        arbol = arbol_binario()
        
        print("\nMENU DE OPCIONES DE ARBOL BINARIO:")
        print("1) Insertar nodo")
        print("2) Buscar nodo")
        print("3) Eliminar nodo")
        print("4) Imprimir en posorden")
        print("5) Imprimir en preorden")
        print("6) Imprimir en inorden")
        print("7) Saber numero de nodos en el arbol")
        print("8) Saber profundidad de el arbol")
        print("9) Para dejar arbol binario")

        while True:
            try:
                operacion = int(input("\nDigite la opcion que desee: "))

                if operacion <= 0 or operacion > 9:
                    raise ValueError("La opcion no esta dentro de el menu")

                if operacion == 9:
                    print("Saliendo...")
                    time.sleep(1)
                    print()
                    break
                
                if operacion == 1:
                    valor = int(input("Indique en el contenido del nodo: ")) # CAMBIR A STR QUITAR EL INT()
                    arbol.insertar(valor)
                elif operacion == 2:
                    nodo_buscar = int(input("Indique el nodo a buscar: "))
                    res = arbol.buscar(arbol.raiz, nodo_buscar)
                    if res:
                        print(f"El nodo con valor: {nodo_buscar} esta dentro del arbol")
                    else:
                        print(f"{nodo_buscar} No esta dentro de el arbol")
                elif operacion == 3:
                    nodo_eliminar = int(input("Indique el nodo a eliminar: ")) # CAMBIR A STR QUITAR EL INT()
                    arbol.eliminar(arbol.raiz, nodo_eliminar)
                elif operacion == 4:
                    print("Recorrido en posorden: ", end="")
                    arbol.postorden_recursivo(arbol.raiz)
                    print()
                elif operacion == 5:
                    print("Recorrido en preorden: ", end="")
                    arbol.preorden_recursivo(arbol.raiz)
                    print()
                elif operacion == 6:
                    print("Recorrido en inorden: ", end="")
                    arbol.inorden(arbol.raiz)
                    print()
                elif operacion == 7:
                    print(f"El numero de nodos dentro de el arbol es: {arbol.num_nodos}")
                elif operacion == 8:
                    arbol.amplitud(arbol.raiz)
                    print()
                    arbol.nivel_profundidad(arbol.raiz)
                
            except ValueError as e:
                print(f"Error: {e}\n")
