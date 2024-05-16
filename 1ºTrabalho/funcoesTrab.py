import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import t

def ordenaValores(lista):
    lista.sort()


def mediaPonderada(lista):
    quantElementos = len(lista)
    soma = 0
    peso = 0

    for i in range(quantElementos):
        
        soma = soma + lista[i][0] * lista[i][1]
        peso = peso + lista[i][1]

    media = soma/peso
    valFim = round(media, 3)

    return valFim

def media_aritmetica(lista):
    quantElementos = len(lista)
    total = 0
    for i in range(quantElementos):
        total = total + lista[i]

    media = total/quantElementos
    valFim = round(media, 3)

    return valFim

def mediana(lista):
    quantElementos = len(lista)
    valor = 0
    ordenaValores(lista)

    if(quantElementos%2==0):
        pos = (quantElementos//2)-1
        valor = lista[pos]
        valor = valor + lista[quantElementos//2]
        valor = valor // 2
    else:
        valor = lista[quantElementos//2]
    return valor

def mediaGeometrica(lista):
    quantElementos = len(lista)
    valor = 1

    for i in range(quantElementos):
        valor = valor * lista[i]
    raiz = valor ** (1/quantElementos)

    valFim = round(raiz, 3)

    return valFim

def mediaHarmonica(lista):
    quantElementos = len(lista)
    valor = 0

    for i in range(quantElementos):
        valor = valor + (1/lista[i])
    
    return round(quantElementos/valor, 3)

def mediaTaxa(lista):
    quantElementos = len(lista)
    soma1 = 0
    soma2 = 0

    for i in range(quantElementos):
        soma1 = soma1 + lista[i][0]
        soma2 = soma2 + lista[i][1]

    media1 = soma1/quantElementos
    media2 = soma2/quantElementos

    valFim = media2/media1
    valFim = round(valFim, 3)

    return valFim

def calculaModa(lista):
    contagemElem = {}
    
    for elemento in lista:
        if elemento in contagemElem:
            contagemElem[elemento] += 1
        else:
            contagemElem[elemento] = 1
    
    contagemMax = max(contagemElem.values()) #Podemos utilizar essa função max?
    
    modas = [elemento for elemento, contagem in contagemElem.items() if contagem == contagemMax]
    
    return modas

def menorvalor(lista):
    menor = lista[0]
    i = 1

    for i in range(len(lista)):
        if(menor > lista[i]):
            menor = lista[i]
    return menor

def maiorvalor(lista):
    maior = lista[0]
    i = 1

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

    return round(resultado, 3)

def produtoNotavel(a, b):
    resultado = (a*2) - (2*a*b) + (b*2)

    return resultado


def varianciaAmostral(lista):
    x = mediaAmostral(lista)
    quantElementos = len(lista)
    soma = 0
    aux = 0

    for i in range(quantElementos):
        aux = lista[i] - x
        aux = aux ** 2
        soma = soma + aux
    
    resultado = 1 / (quantElementos-1)
    resultado = resultado * soma

    return round(resultado, 3)

def desvioPadrao(lista):
    resultado = varianciaAmostral(lista)
    resultado = resultado ** (1/2)
    return round(resultado, 3)

def coeficenteVariacao(lista):
    x = mediaAmostral(lista)
    s = desvioPadrao(lista)

    cv = (s/x)*100

    return round(cv, 3)

def obterQuartis(lista):
    quartis = np.percentile(lista, [25, 50, 75])
    return quartis

def amplitudeInterQuartil(lista):
    # Calcular quartis
    Q1 = np.percentile(lista, 25)
    Q3 = np.percentile(lista, 75)

    return round(Q3-Q1, 3)

def diagramaCaixa(amostra):
    plt.boxplot(amostra)
    plt.ylabel('Valores')
    plt.show()

def todasMedidasDispercao(amostra):
    print("\nAmplitude: ", amplitude(amostra))
    print("Media Amostral: ",mediaAmostral(amostra))
    print("Variancia amostral: ",varianciaAmostral(amostra))
    print("Desvio Padrao: ", desvioPadrao(amostra))
    print("Coeficiente de Variacao: ", coeficenteVariacao(amostra))
    print("Quartis: ", obterQuartis(amostra))
    print("Amplitude Interquatil: ", amplitudeInterQuartil(amostra))
    diagramaCaixa(amostra)
    
def intervaloConfianca(lista, nivelConfianca):
    quantElementos = len(lista)

    x = mediaAmostral(lista)
    s = desvioPadrao(lista)

    intervalo = []

    if nivelConfianca == 90:
        z = 1.645
        param = 0.95
    elif nivelConfianca == 95:
        z = 1.960
        param = 0.975
    elif nivelConfianca == 99:
        z = 2.576
        param = 0.995
    else:
        print("Nível de confiança inválido!!")
        return intervalo
    
    if quantElementos >= 30:
        y = (s * z) / (quantElementos ** (1/2))
        resultadoL = x - y
        resultadoR = x + y
        intervalo = (round(resultadoL, 3), round(resultadoR, 3))

    else:
        df = quantElementos - 1 #df = grau de liberdade
        valor_t = t.ppf(param, df)
        y = (s * valor_t) / (quantElementos ** (1/2))
        resultadoL = x - y
        resultadoR = x + y
        intervalo = (round(resultadoL, 3), round(resultadoR, 3))
    
    return intervalo    

def testeMediaZero(amostra, nivelConfianca):
    intervalo = intervaloConfianca(amostra, nivelConfianca)
    if(intervalo[0] <= 0):
        print("Intervalo de confiança da amostra -> {}\nIntervalo de confiança inclui zero" .format(intervalo))
        return 1
    else:
        print("Intervalo de confiança da amostra -> {}\nIntervalo de confiança não inclui zero" .format(intervalo))
        return -1

def desvPadDifMedia(amostraA, amostraB):
    sA = desvioPadrao(amostraA)
    nA = len(amostraA)
    sB = desvioPadrao(amostraB)
    nB = len(amostraB)

    valFim = (sA ** 2 / nA) + (sB ** 2 / nB)
    valFim = math.sqrt(valFim)

    return valFim


def calcGrausLiberdade(amostraA, amostraB):
    sA = desvioPadrao(amostraA)
    nA = len(amostraA)
    sB = desvioPadrao(amostraB)
    nB = len(amostraB)

    aux1 = (sA ** 2 / nA) + (sB ** 2 / nB)

    aux2 = (1 / (nA + 1)) * ((sA ** 2 / nA) ** 2)

    aux3 = (1 / (nB + 1)) * ((sB ** 2 / nB) ** 2)

    numGrausLib = (aux1 ** 2) / (aux2 + aux3)
    numGrausLib = numGrausLib - 2

    return numGrausLib

def intervaloConfiancaDifMedias(amostraA, amostraB, nivelConfianca, valDesvPadDifMed, grausLiberdade):
    xA = mediaAmostral(amostraA)
    xB = mediaAmostral(amostraB)
    difMedAmostral = xA - xB

    if nivelConfianca == 90:
        param = 0.95
    elif nivelConfianca == 95:
        param = 0.975
    elif nivelConfianca == 99:
        param = 0.995

    valor_t = t.ppf(param, grausLiberdade)

    val = valDesvPadDifMed * valor_t
    valFim1 = difMedAmostral - val
    valFim2 = difMedAmostral + val

    intervalo = (round(valFim1, 3), round(valFim2, 3))

    return intervalo

def testeMediaZeroDuasAmostras(amostraA, amostraB, nivelConfianca, pareadas): # Valor de 'pareadas' pode ser 1 ou -1. 1 = amostras pareadas | -1 = amostras não pareadas
    tamA = len(amostraA)
    tamB = len(amostraB)

    if(pareadas == 1): # Amostras são pareadas se o i-ésimo teste em A corresponde ao i-ésimo teste em B. As amostras são tratadas como uma
        listaDif = []

        for i in range(tamA):
            listaDif.append(amostraA[i] - amostraB[i])

        if(testeMediaZero(listaDif, nivelConfianca) == 1):
            print("Os sistemas NÃO SÃO diferentes!")
            return 1
        else:
            print("Os sistemas SÃO diferentes!")
            return -1

    elif(pareadas == -1):
        valDesvPadDifMed = desvPadDifMedia(amostraA, amostraB)

        numGrausLib = calcGrausLiberdade(amostraA, amostraB)
        #numGrausLib = math.ceil(calcGrausLiberdade(amostraA, amostraB))

        intervalo = intervaloConfiancaDifMedias(amostraA, amostraB, nivelConfianca, valDesvPadDifMed, numGrausLib)

        if(intervalo[0] <= 0):
            print("Intervalo de confiança da amostra -> {}\nIntervalo de confiança inclui zero" .format(intervalo))
            return 1
        else:
            print("Intervalo de confiança da amostra -> {}\nIntervalo de confiança não inclui zero" .format(intervalo))
            return -1

amostra1= [145, 74, 56, 98, 32, 97]

amostra2= [48, 81, 33, 40, 84]

#print("Amostra 1:")

#print("Media Amostral: ",mediaAmostral(amostra1))
#print("Variancia amostral: ",varianciaAmostral(amostra1))
#print("Desvio Padrao: ", desvioPadrao(amostra1))


#print("\nAmostra 2:")

#print("Media Amostral: ",mediaAmostral(amostra2))
#print("Variancia amostral: ",varianciaAmostral(amostra2))
#print("Desvio Padrao: ", desvioPadrao(amostra2))

vetorPeso = [[5,2], [4,4], [8,4]]# 37/6= 
#tam = len(vetorPeso)

vetor = [[18,13],[11,8,10,58],[12,7,9],[9,10,7,2]]
#vetor = [405, 367, 405, 419, 388]
#diagramaCaixa(vetor)

amostra = [2, 1, 100, 10, 9, 0, 0, 10, 2]

amostra3 = [1, 8, 10, 6, 2, 3, 6, 7, 10, 2, 3, 5, 5, 5, 8, 9, 10, 1, 1, 1, 2, 3, 8, 7, 6, 4, 10, 7, 7, 2, 3]
amostra4 = [1, 8, 10, 6, 2, 3, 6, 7, 10, 2, 3, 5, 5, 5, 8]
amostra5 = [1, 8, 10, 6, 2, 3, 6, 7, 10, 2, 3, 5, 5, 5, 8, 9, 10, 1, 1, 1, 2, 3, 8, 7, 6, 4, 10, 7, 7, 2]
amostra6 = [1, 8, 10, 6, 2, 3, 6, 7, 10, 2, 3, 5, 5, 5, 8, 9, 10, 1, 1, 1, 2, 3, 8, 7, 6]

amostraA = [5.4, 16.6, 0.6, 1.4, 0.6, 7.3]
amostraB = [19.1, 3.5, 3.4, 2.5, 3.6, 1.7]

amostraC = [1.5, 2.6, -1.8, 1.3, -0.5, 1.7, 2.4]

amostraD = [5.36, 16.57, 0.62, 1.41, 0.64, 7.26]
amostraE = [19.12, 3.52, 3.38, 2.50, 3.60, 1.74]

#testeConfianca99 = intervaloConfianca(amostraC, 99)
#print(testeConfiancaA99)

#testeMediaZero99 = testeMediaZero(amostraC, 99)

#testeMZAeB90 = testeMediaZeroDuasAmostras(amostraA, amostraB, 90, 1)

testeMZAeB90 = testeMediaZeroDuasAmostras(amostraD, amostraE, 90, -1)

#testeMZAeB95 = testeMediaZero(amostraA, amostraB, 95)
#testeMZAeB99 = testeMediaZero(amostraA, amostraB, 99)

#print("Teste de Média Zero das amostras A e B com nível de confiança de 90%: ", testeMZAeB90)
#print("\n")
#print("Teste de Média Zero das amostras A e B com nível de confiança de 95%: ", testeMZAeB95)
#print("\n")
#print("Teste de Média Zero das amostras A e B com nível de confiança de 99%: ", testeMZAeB99)

#moda = calculaModa(amostra)
#print(moda)

#quartis = obterQuartis(amostra)
#print(quartis)

#vetorTax = [[80, 40.00], [40, 45.00], [12, 50.00]]
#vetorTax = [[100, 3.0], [100, 5.0], [100, 4.2], [100, 5.2], [100, 8.6]]
#valMediaTax = mediaTaxa(vetorTax)
#print(valMediaTax)

#valoMediaGeo = mediaGeometrica(vetor)
#print(valoMediaGeo)

#valorMediaPeso = mediaPonderada(vetorPeso)

#valor = vetorPeso[1][0] * vetorPeso[1][1]

#print(vetorPeso[0][0])
#print(valorMediaPeso)