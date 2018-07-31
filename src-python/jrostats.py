# libreria jrostats.
import math

def mean(p):
    """ Calculo de la media de un conjunto de valores.... """
    resultado = 0.0
    n = len(p)
    for x in p:
        resultado = resultado + x
    return resultado/n


def standarDeviation(p):
    """ Calculo de la desviacion standard ..."""
    media = mean(p)
    distanciasALaMedia = [ (x-media)**2 for x in p]
    sd = math.sqrt(sum(distanciasALaMedia)/len(p))
    return sd


