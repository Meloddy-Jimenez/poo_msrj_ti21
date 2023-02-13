"""Programa7
   Nombre: Meloddy Sofia R,J
   Fecha: 
   Descripción: Calcular e imprimir el area y perimetro de un triangulo

"""
lado1 = float(input("Ingrese la longitud del primer lado del triángulo: ")) #pedira el primer lado del triangulo
lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))#pedira el segundo lado del triagulo
lado3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))#pedria el tercer lado del triangulo para poder calcular el area y perimetro

# Calcular el perímetro del triángulo
perimetro = lado1 + lado2 + lado3

# Calcular el semiperímetro del triángulo
semiperimetro = perimetro / 2

# Calcular el área del triángulo usando la fórmula de Herón
area = (semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5

# Mostrar el área y el perímetro del triángulo
print("El área del triángulo es:", area)
print("El perímetro del triángulo es:", perimetro)