import os
import math
from time import sleep

class Calculos:
	
	def __init__(self, x:int,y:int):
		self.numero1 = x
		self.numero2 = y
		
	def soma(self):
		
		self.total = self.numero1+self.numero2
		return self.total
		
	def subtrai(self):
		
		self.total= self.numero1-self.numero2
		return self.total
		
	def multiplica(self):
		self.total= self.numero1*self.numero2
		return self.total
	
	def divide(self):
		self.total= self.numero1/self.numero2
		return self.total
		
	def raiz(self):
		self.total=  math.sqrt(self.numero2)
		return self.total
	
os.system('cls')	

print()
print()

x = int(input('Digite o primeiro num: '))
y = int(input('Digite o segundo  num: '))

calcular = Calculos(x,y)	

os.system('cls')	

print('---Soma---')
print(calcular.numero1)
print(calcular.numero2)
print()
print(calcular.soma())
print()
sleep(5)
os.system('cls')

print('---Subtrai---')
print()
print(calcular.numero1)
print(calcular.numero2)
print()
print(calcular.subtrai())
print()
sleep(5)
os.system('cls')

print('---Multiplica---')
print()
print(calcular.numero1)
print(calcular.numero2)
print()
print(calcular.multiplica())
print()
sleep(5)
os.system('cls')

print('---Divide---')
print()
print(calcular.numero1)
print(calcular.numero2)
print()
print(calcular.divide())
print()
sleep(5)
os.system('cls')

print('---Raiz Quadrada Segundo Numero---')
print()
print(calcular.numero2)
print()
print(calcular.raiz())





