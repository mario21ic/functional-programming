"""
Una funcion se encarga de una sola cosa y usa otra para reutilizar
"""

def alCuadrado(numero):
    return numero * numero
print(alCuadrado(2))

def sumaDeCuadrados(num1, num2):
    return alCuadrado(num1) + alCuadrado(num2)
print(sumaDeCuadrados(2, 3))

def cuadradoAntecesorMasSucesor(numero):
    return sumaDeCuadrados(numero-1, numero+1)

print(cuadradoAntecesorMasSucesor(5))

