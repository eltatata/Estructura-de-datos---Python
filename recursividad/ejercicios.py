# 1)
def f_message(msg, n):
    if n > 0:
        print(msg)
        f_message(msg, n - 1)
    
f_message("Hola Mundo", 5)
print()

# 1) EN FORMA DE LAMBDA
f_message_lambda = lambda msg, n: (print(msg), f_message_lambda(msg, n - 1)) if n > 0 else None
f_message_lambda("Hola Mundo en lambda", 5)
print()

# 2)
def max_divisor(n1, n2):
    res = n1 % n2
    
    if res == 0:
        return n2
    
    return max_divisor(n2, res)

print(max_divisor(15, 2))

# 2) EN FORMA DE LAMBDA
max_divisor_lambda = lambda n1, n2: n2 if (n1 % n2 == 0) else max_divisor_lambda(n2, n1 % n2)
print(max_divisor_lambda(15, 2))