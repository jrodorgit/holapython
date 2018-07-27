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

# esto anade un elemento mas a mi lista
milista.append(36)

# esto devuelve los elementos 2,3 y 4 de milista.. el primer elemento de la lista es el 0
milista[2:5]

# esto es una lista de listas milista_c tendra 2 elementos cada uno de ellos a su vez una lista
milista_b = [0,1,2,3]
milista_c = [milista,milista_b]

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
