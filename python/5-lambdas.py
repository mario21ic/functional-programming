"""
Una funcion puede recibir como parametro otra funcion y otros normales
Retornan tipos de datos strings, integeres, etc
"""

def mapearLista(lista, accion):
    if len(lista) == 1:
        return [accion(lista[0])]
    else:
        return [accion(lista[0])] + mapearLista(lista[1:], accion)
print(mapearLista([1, 2, 3, 4], lambda numero: numero*2))
print(mapearLista([1, 2, 3, 4], lambda numero: numero*3))


