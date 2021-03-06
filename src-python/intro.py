# esto es un comentario.

#esto es una asignacion multiple de variables
 a,b = 1,2
 
#esto imprime una cadena
print('c:\hola\numero')
 
# la anterior cadena lleva \n que lo intrepreta como un salto de linea
# si lo quiero evitar pongo un r delante de la cadena
print(r'c:\hola\numero')

#esto es una lista
milista = [1,4,9,16,25]

#generacion de lista a partir de expresiones.
milistatuplacuadrados = [(x, x**2) for x in range(6)]

# esto anade un elemento mas a mi lista
milista.append(36)

# esto devuelve los elementos 2,3 y 4 de milista.. el primer elemento de la lista es el 0
milista[2:5]

# esto es una lista de listas milista_c tendra 2 elementos cada uno de ellos a su vez una lista
milista_b = [0,1,2,3]
milista_c = [milista,milista_b]

#esto es una tupla. es un objeto inmutable.
tupla = (1,4,5)
tupla2 = (1,4),(1,8)
otratupla = 1,2,3
#si queremos asignar los valors de la tupla a otras variables podemos...
x,y,z = otratupla

#esto es un conjunto o set. elemento no repetidos. la a solo estara en el conjunto una vez.
setuno = {'a','b','c','a'}
# este conjunto tendra los caracteres c y a
setdos = set('caca')
# sobre los conjuntos se pueden hacer operaciones matematicas del tipo
# esto devolvera los elementos que estan en setuno o en setdos pero no los comunes.
setuno ^ setdos

# esto es un diccionario
telefonos = {'jack':3455, 'alfred':989}
#le anado mas numeros de telefono
telefonos['guido'] = 345

otrodiccionario = dict(sape=4139, guido=4127, jack=4098)
otromas = {x: x**2 for x in (2, 4, 6)}

# esto es un bucle while que genera los primeros  elementos de la serie de fibonacci
a, b = 0,1
while a < 10:
 print(a)
 a, b = b , a+b

#esto es un bucle for
words = ['gato','perro','canario']
for w in words:
 print(w,len(w))
 

#bucle for para generar los numeros primos menores de 10
# else va asociado el segundo bucle for y se ejecuta siempre  y cuando se salga de este sin pasar por break
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		# loop fell through without finding a factor
		print(n, 'is a prime number')
  
# esto es un bucle for con con colecciones a la vez
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


#esto es un sentencia de control
x = int(input("inserta un numero"))
 
if x < 0:
 x=0
 print('de negativo a cero')
elif x == 0:
 print('cero')
elif x == 1:
 print("single")
else:
 print("more")

# esto es otro sentencia de control
if ok in ('y', 'ye', 'yes'):
    return True

#esto declara una funcion para luego poder ser ejecutada.
def fibo(n):
	"""Print fibonacci series up to n """
	a, b = 0,1
	while a < 10:
 		print(a)
 		a, b = b , a+b
	print()

#llamada a un funcion definida en un fichero fibo.py situado en P:\mypython\fibo.py
#nos situamos en el lugar donde esta el script py
import os
os.getcwd()
os.chdir(r'P:\mypython')
os.getcwd()

#importamos el fichero
import fibo

# declaramos que de ese fichero vamos a utilizar la funcion fibo
from fibo import fibo
#ejecutamos la funcion
fibo()
# si cambiamos una libreria para que se refrequen los cambios...
import importlib
importlib.reload(milibreria)

# formateo de cadenas.
print('{0} and {1}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible'))

#lectura de fichero, limpieza de caracteres y conversion a float
with open('P:\R-scripts\Klout.csv') as f:
    klout = list(f)

f.close()

klout2 = [x.replace("\n","") for x in klout]
klout2 = [float(x) for x in klout2]

# lectura de fichero con formato json
import json
with open(r'C:\Users\jrodor5\Desktop\JRODOR\RAM\ram_persona.json', "r",encoding="utf-8") as read_file:
    persona = json.load(read_file)

read_file.close()

