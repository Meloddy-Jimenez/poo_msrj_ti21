"""Programa7
   Nombre: Meloddy Sofia R,J
   Fecha: 31/01/2023
   Descripción: Calcular e imprimir el area y perimetro de un circulo y un cuadrado 

"""
print ("calcular el area y el perimetro de un circulo") 
print ("ingrese la medida del radio")
radio = input("radio :") #obtiene el dato necesario para calcular el area del circulo 
print ("el area del circulo es de")
area = float(radio) * 3.14 * float(radio)
print (area) #variable que calcula el area del circulo
print ("el perimetro del circulo es de")#obtiene el dato necesario para poder calcualar el perimetro
perimetro = float(radio) * 3.14 * 2 #variable que calcula el perimetro del circulo 
print (perimetro)

print

print ("calcula el area y el perimetro de un cuadrado") 
print ("ingrese la medida de los lados del cuadrado") #obtiene el dato de los lados del cuadrado
lado = input("lado")
print ("el area del cuadrado es")
area = float(lado) ** 2 #variable que calcula el area del cuadrado 
print (area)
print ("el perimetro del cuadrado es") 
perimetro = float(lado) + float(lado) + float(lado) + float(lado) #variable que permite sumar todos los lados del cuadrado y sacar el perimetro
print (perimetro)




      