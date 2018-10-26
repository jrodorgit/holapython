# BUSCADOR DE CADENAS EN ARCHIVOS
from pathlib import Path
import re

def listado(ruta):
    """ devuelve una lista con los ficheros de tipo .py presentes en la ruta deseada y en directorios hijos """
    p=Path(ruta)
    return list(p.glob('**/*.java'))

def leeLineaAjustaPatron(fichero,patron):
    """ IMPRIME MATCH ENCONTRADO POR CADA LINEA QUE CONTIENE EL PATRON """
   
    #print(fichero)
    with open(fichero, "r",encoding="Cp1252") as read_file:
        nline = 1
        for line in read_file:
            #print('leyendo linea...')
            match = re.search(patron,line)
            #print(match)
            if match:
                print(fichero)
                print('match encontrado...')
                print(nline)
                #print(line)
                #print(fichero)
            nline = nline+1
    read_file.close()
    return
    
import os
os.chdir(r'P:\git\GoDicodef\src\test\resources')

files = listado(r'C:\sinfradef\7.1.3.0g_20180913')

print('Numero de ficheros java en directorio:')

print(len(files))
#sString = '50097587'
sString = 'SINCRONIZARUCOCCSINCRONIZACION'

for f in files:
    leeLineaAjustaPatron(f,sString)





