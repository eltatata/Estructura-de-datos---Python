# Escriba un programa en Python que le pida al usuario la temperatura en grados Celcius (°C) 
# y convierta dicha temperatura a grados Fahrenheit (°F). 
# Muestre el resultado de la conversión como se indica a continuación.

celsius = float(input())

fahrenheit = celsius * 1.8 + 32

print(f"{celsius}°C equivalen a {round(fahrenheit, 2)}°F")