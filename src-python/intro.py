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
