import numpy as np

def menorvalor(lista):
    menor = lista[0]
    i =1

    for i in range(len(lista)):
        if(menor > lista[i]):
            menor = lista[i]
    return menor

def maiorvalor(lista):
    maior = lista[0]
    i =1

    for i in range(len(lista)):
        if(maior < lista[i]):
            maior = lista[i]
    return maior

def amplitude(lista):
    menor = menorvalor(lista)
    maior = maiorvalor(lista)

    return maior - menor




def mediaAmostral(lista):
    quantElementos = len(lista)

    soma = 0

    for i in range(quantElementos):
        soma = soma + lista[i]
    resultado = (1/quantElementos) * soma

    return round(resultado, 1)

def produtoNotavel(a, b):

    resultado = (a**2) - (2*a*b) + (b**2)

    return resultado


def varianciaAmostral(lista):
    x = mediaAmostral(lista)
    quantElementos = len(lista)
    soma = 0
    aux = 0


    for i in range(quantElementos):
        aux = lista[i] - x
        #aux = produtoNotavel(lista[i], x)
        aux = aux ** 2
        soma = soma + aux
    
    resultado = 1 / (quantElementos-1)
    resultado = resultado * soma

    return round(resultado, 1)

def desvioPadrao(lista):
    resultado = varianciaAmostral(lista)
    resultado = resultado ** (1/2)
    return round(resultado, 1)

def coeficenteVariacao(lista):
    x = mediaAmostral(lista)
    s = desvioPadrao(lista)

    cv = (s/x)*100

    return round(cv, 1)


def amplitudeInterQuartil(lista):
    # Calcular quartis
    Q1 = np.percentile(lista, 25)
    Q3 = np.percentile(lista, 75)

    return round(Q3-Q1, 1)

def todasMedidasDispercao(amostra):
    print("\nAmplitude: ", amplitude(amostra))
    print("Media Amostral: ",mediaAmostral(amostra))
    print("Variancia amostral: ",varianciaAmostral(amostra))
    print("Desvio Padrao: ", desvioPadrao(amostra))
    print("Coeficiente de Variacao: ", coeficenteVariacao(amostra))
    print("Amplitude Interquatil: ", amplitudeInterQuartil(amostra))


if "__main__":
    amostra1= [145, 74, 56, 98, 32, 97]

    amostra2= [76,102,12,39,55,93,98,53,102]

    print("Amostra 1: ")
    todasMedidasDispercao(amostra1)
    print("\nAmostra 2:")
    todasMedidasDispercao(amostra2)

