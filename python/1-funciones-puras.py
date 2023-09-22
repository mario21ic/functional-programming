"""
Function Pura:
Devuelve el mismo resultado cuando el input es la mismo anteriormente
"""

def sumaPura(num1, num2):
    return num1 + num2

print("## sumaPura")
print(sumaPura(2, 3))
print(sumaPura(2, 3))
print(sumaPura(2, 3))
print(sumaPura(2, 3))

total = 0
def sumaNOPura(num1, num2):
    global total
    total = total + num1 + num2
    return total

print("## sumaNOPura")
print(sumaNOPura(2, 3))
print(sumaNOPura(2, 3))
