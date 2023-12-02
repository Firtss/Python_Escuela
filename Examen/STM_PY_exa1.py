num = int(input("Dame  un numero: "))

def factorial(num):
    if num  == 0 or num == 1:
        resultado = 1
    elif num > 1:
        resultado = num * factorial(num - 1)
    return resultado

fact = factorial(num)
print(fact)
#https://github.com/Firtss/Python_Escuela/tree/main/Examen