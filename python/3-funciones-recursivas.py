"""
"""

# Da error porque no termina
def saludar(mensaje):
    print(mensaje)
    saludar(mensaje)
#saludar("obligame perro!")

"""
# No es recursivo, es imperativo e impulsa mutaciones (objetos que luego se modifican)
def duplicarLista(lista):
    nueva_lista = []
    for numero in lista:
        nueva_lista.append(numero*2)
    return nueva_lista
print(duplicarLista([1, 2, 3, 4]))
"""

# SI es recursivo
def duplicarLista(lista):
    if len(lista) == 1:
        return [lista[0] * 2]
    else:
        return [lista[0] * 2] + duplicarLista(lista[1:])
print(duplicarLista([1, 2, 3, 4]))


