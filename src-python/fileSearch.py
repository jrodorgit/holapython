# BUSCADOR DE CADENAS EN ARCHIVOS
from pathlib import Path
import re

def listado(ruta):
    """ devuelve una lista con los ficheros de tipo .py presentes en la ruta deseada y en directorios hijos """
    p=Path(ruta)
    return list(p.glob('**/*.xml'))

def leeLineaAjustaPatron(fichero,patron):
    """ IMPRIME MATCH ENCONTRADO POR CADA LINEA QUE CONTIENE EL PATRON """
   
    #print(fichero)
    with open(fichero, "r",encoding="utf-8") as read_file:
        for line in read_file:
            #print('leyendo linea...')
            match = re.search(patron,line)
            #print(match)
            if match:
                print(fichero)
                print('match encontrado...')
                #print(line)
                #print(fichero)
        
    read_file.close()
    return
    
import os
os.chdir(r'P:\git\GoDicodef\src\test\resources')

files = listado(r'C:\Users\jrodor5\dependencias_ucos')

print('Numero de ficheros XML en directorio:')

print(len(files))
sString = '50097587'
#sString = 'CABALLERIA  MONTESA'

for f in files:
    leeLineaAjustaPatron(f,sString)




