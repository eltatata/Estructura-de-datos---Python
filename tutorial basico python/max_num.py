# Escriba un programa en Python que le pida al usuario tres valores. 
# Determine y muestre cuál de los tres valores ingresados por el usuario es el número mayor.

nums = []

for i in range(3):
    num = float(input())
    nums.append(num)

mayor = max(nums)

print(f"El mayor es {mayor}")