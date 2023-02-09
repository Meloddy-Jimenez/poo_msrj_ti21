"""Programa10
   Nombre: Meloddy Sofia R,J
   Fecha: 07/02/2023
   Descripción: Multiples formas de realizar una aplicacion que lea dos numeros enteros, los compare, y muestre el numero mayor 

"""
n1 = int(input("Numero1")) 
n2 = int(input("Numero2"))

#forma1
if n1 > n2:
  print(n1)
if n2 > n1:
  print(n2)
if n1 == n2:
  print(None)

#forma2
if n2 > n1:
  print(n2)
if n1 > n2:
  print(n2)
else:
  print(None)

#forma 3
if n1 > n2:
  print(n1)
elif n2 > n1:
  print(n2)
else:
  print(None)
#Es una forma mas facil y practica de elaborar el codigo

  
#forma 4
if n1 == n2:
  print(None)
elif n1 > n2:
  print(n1)
elif n2 > n1:
 print(n2)


#forma 5
if n1 < n2:
  print(n2)
if n2 < n1:
  print(n1)
if n1 == n2:
  print(None)
  

#forma 6
if n2 > n1:
  print(n2)
if n2 < n1:
  print (n1)
else:
  print (None)


#forma 7
if (n2 < n1 > n2):
  print(n1)
elif (n2 < n1 > n2):
  print(n2)
else:
  print(None)

#forma 8 if anidado 

if n1 <= n2:
    if n1 == n2:
      print (None)
else:
  print (n2)
else:
  print (n1)


#forma 9
def mayor(n1, n2):
  if n1>=n2:
    if n1 == n2
        print(None)
  else:
    print(n1)
else:
    print(n2)

  


