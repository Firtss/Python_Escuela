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
Altura = int(input("Dame la altura del triangulo: "))
Base = int(input("Dame la base del triangulo: "))
def area(Altura,Base):
    area = Base * Altura / 2.0
    return area

area_triangulo = area(Altura,Base)
print(area_triangulo)
#https://github.com/Firtss/Python_Escuela/tree/main/Examen
valido = False

def validar(valor):
    entero = int(valor)
    return entero >= 0 and entero <= 100
try:
    print("Introduzca un valor: ",end="")
    while not valido:
        valor = input()
        valido = validar(valor)
        if not valido:
            print("El valor no es valido")
    print(f"El valor es valido {valor}")
except: 
    print("No introduciste un valor numerico")
#https://github.com/Firtss/Python_Escuela/tree/main/Examen
