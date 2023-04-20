from tabla_hash import TablaHash

n_messages = int(input())

tabla = TablaHash(n_messages)

for i in range(n_messages):
    seller = input().split(":")
    tabla.set(seller[0], int(seller[1]))

tabla.show()


# tabla = TablasHash(10)

# tabla.set("Hola", 13)
# tabla.set("Juan", 8)
# tabla.set("David", 777)
# tabla.set("Maria", 23)
# tabla.set("Mariana", 43)
# tabla.set("Pedro", 63)
# tabla.set("Mariana", 666)
# tabla.set("David", 777888)

# print(tabla.hash("Hola"))
# print(tabla.hash("Juan"))
# print(tabla.hash("David"))
# print(tabla.hash("Maria"))
# print(tabla.hash("Mariana"))
# print(tabla.hash("Pedro"))

# print(tabla.tabla)

# valorClave = tabla.get("David")
# print(f"\nEl valor de clave es: {valorClave}\n")

# tabla.show()

# tabla.delete("Maria")

# tabla.show()

# print()

# print(tabla.tabla)
