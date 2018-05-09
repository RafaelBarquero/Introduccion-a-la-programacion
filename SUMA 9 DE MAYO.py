"""Calcular la suma de todos los valores de una matriz de n x m y determinar el
valor promedio de estos"""
def sumatriz(lista):
    if isinstance (lista,list):
        return operacion(lista,0,0,len(lista),len(lista[0]),0)
    else:
        return "Error: Valor no valido"

def operacion(lista,F,C,CF,CC,P):
    if F==CF:
        return P/(CF*CC)
    elif C < CC-1:
        return operacion(lista,F,C+1,CF,CC,P+lista[F][C])
    elif C == CC-1:
        return operacion(lista,F+1,0,CF,CC,P+lista[F][C])


