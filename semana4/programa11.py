"""Programa11
   Nombre: Meloddy Sofia R,J
   Fecha: 09/02/2023
   Descripción: Se crearan 8 pruebas utilizando "mayor" para probar que los codigos sean funcionales codigo1

"""

def mayor(numero1 , numero2):
    result = None
    if numero1 > numero2:
         result = numero1
    elif numero2 > numero1:
         result = numero2
    return result 

print(mayor(2,1))
print(mayor(1,2))
print(mayor(2,2))
print(mayor(2,-1))
print(mayor(-1,2))
print(mayor(-1,-1))
print(mayor(-2,-1))
print(mayor(-1,-2))