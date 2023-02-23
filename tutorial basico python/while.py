# Escriba un programa en Python que lea repetidamente números enteros hasta que el usuario 
# introduzca la palabra fin. Una vez se haya introducido fin, muestre el total de números 
# leídos, la suma de los números leídos y la media aritmética de dichos números, 
# tal cual como se indica a continuación.

nums = list()

while True:
    num = input()
    
    if num == 'fin':
        break
    
    nums.append(int(num))

total = len(nums)
sum = sum(nums)
media = sum / total

print(f"Total: {total}\nSuma: {sum}\nMedia: {media}")