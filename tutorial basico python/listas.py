# Escriba un programa en Python que permita de manera indefinida ingresar valores numéricos
# (enteros y reales) a una lista. El usuario ingresa los valores 
# hasta que ingrese la palabra fin. Con la lista de valores ingresados:
# imprima: la lista en orden ascendente, 
# la lista en orden inverso, 
# el mayor valor, 
# el menor valor y 
# el promedio de los valores.

nums = list()

while True:
    num = input()
    
    if num == 'fin':
        break
    
    nums.append(float(num))


sort = sorted(nums)
reverse = sorted(nums, reverse=True)
max = max(nums)
min = min(nums)
promedio = sum(nums) / len(nums)

print(f"Ordenada = {sort}\nInversa = {reverse}\nMayor = {max}\nMenor = {min}\nPromedio = {promedio}")