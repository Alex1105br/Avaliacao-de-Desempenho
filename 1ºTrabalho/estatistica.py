import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import t

def distribProbVAQualquer(listaValAssumidos, listaMassaProbabilidade):
    valAux = 0
    tam = len(listaValAssumidos)
    valP = 0
    valListaAnt = 0

    for i in range(tam):
        if valAux == 0 and i == 0:
            print("F(x) = 0\tx < {}" .format(listaValAssumidos[i]))
            valAux += 1
            valListaAnt = listaValAssumidos[i]
            valP += listaMassaProbabilidade[i]
        elif valAux == 1 and i != tam - 1:
            print("F(x) = {}\t{} <= x < {}" .format(valP, valListaAnt, listaValAssumidos[i]))
            valP += listaMassaProbabilidade[i]
            valListaAnt = listaValAssumidos[i]
        elif valAux == 1 and i == tam - 1:
            print("F(x) = {}\t{} <= x < {}" .format(valP, valListaAnt, listaValAssumidos[i]))
            valP += listaMassaProbabilidade[i]
            valListaAnt = listaValAssumidos[i]
            valAux += 1

        if valAux == 2:
            print("F(x) = {}\tx >= {}" .format(valP, valListaAnt))


def calcEstatVADisc(listaValAssumidos, listaMassaProbabilidade):
    print("==================================")
    distribProbVAQualquer(listaValAssumidos, listaMassaProbabilidade)
    print("==================================")

    valEspVA = 0
    valEspVA2 = 0
    var = 0

    tam = len(listaValAssumidos)

    for i in range(tam):
        valEspVA += listaValAssumidos[i] * listaMassaProbabilidade[i]
        valEspVA2 += ((listaValAssumidos[i]) ** 2) * listaMassaProbabilidade[i]

    var = valEspVA2 - ((valEspVA) ** 2)

    valEspVA = round(valEspVA, 3)
    valEspVA2 = round(valEspVA2, 3)
    var = round(var, 3)

    print("E[X] = {}\nE[X^2] = {}\nVar[X] = {}" .format(valEspVA, valEspVA2, var))
    print("==================================")


def calcEstatVABernoulli(probSucesso): # X = 1 Representa sucesso | X = 0 representa fracasso
    probSucessoDec = probSucesso * 0.01
    probFracassoDec = 1 - probSucessoDec

    print("P(X = 1) = {}\tP(X = 0) = {}\n" .format(round(probSucessoDec, 3), round(probFracassoDec, 3)))

    valEsperado = probSucessoDec
    var = valEsperado * (probFracassoDec)
    coefVar = math.sqrt(var) / valEsperado

    valEsperado = round(valEsperado, 3)
    var = round(var, 3)
    coefVar = round(coefVar, 3)

    print("E[X] = {}\tVar[X] = {}\tCV[X] = {}" .format(valEsperado, var, coefVar)) # X pode ser tanto 1 quanto 0, para ser esses valores

def calcEstatVABinomial(probSucesso, nRepeticoes, kSucessos):
    probSucessoDec = probSucesso * 0.01

    fatorialNeK = (math.factorial(nRepeticoes)) / ((math.factorial(kSucessos)) * (math.factorial(nRepeticoes - kSucessos)))
    funcMassaProb = fatorialNeK * ((probSucessoDec) ** kSucessos) * ((1 - probSucessoDec) ** (nRepeticoes - kSucessos))
    funcMassaProb = round(funcMassaProb, 3)

    print("P[{}] = {}\n" .format(kSucessos, funcMassaProb))

    valEsperado = nRepeticoes * probSucessoDec
    var = valEsperado * (1 - probSucessoDec)
    coefVar = (math.sqrt(var)) / valEsperado

    valEsperado = round(valEsperado, 3)
    var = round(var, 3)
    coefVar = round(coefVar, 3)

    print("E[{}] = {}\tVar[{}] = {}\tCV[{}] = {}" .format(kSucessos, valEsperado, kSucessos, var, kSucessos, coefVar))

def calcEstatVAGeometrica(probSucesso, repetAteSucesso):
    probSucessoDec = probSucesso * 0.01

    funcMassaProb = probSucessoDec * ((1 - probSucessoDec) ** (repetAteSucesso - 1))
    funcMassaProb = round(funcMassaProb, 3)

    print("P[{}] = {}\n" .format(repetAteSucesso, funcMassaProb))

    valEsperado = 1 / probSucessoDec
    var = (1 - probSucessoDec) / (probSucessoDec ** 2)
    coefVar = (math.sqrt(var)) / valEsperado

    valEsperado = round(valEsperado, 3)
    var = round(var, 3)
    coefVar = round(coefVar, 3)

    print("E[{}] = {}\tVar[{}] = {}\tCV[{}] = {}" .format(repetAteSucesso, valEsperado, repetAteSucesso, var, repetAteSucesso, coefVar))

def calcEstatVAPoisson(eventoEquiprovavel, taxaMedia):
    funcMassaProb = ((math.e) ** (taxaMedia * -1)) * ((taxaMedia ** eventoEquiprovavel) / (math.factorial(eventoEquiprovavel)))
    funcMassaProb = round(funcMassaProb, 3)

    print("P[{}] = {}\n" .format(eventoEquiprovavel, funcMassaProb))

    valEsperado = round(taxaMedia, 3)
    var = valEsperado
    coefVar = round((math.sqrt(taxaMedia) / taxaMedia), 3)

    print("E[{}] = {}\tVar[{}] = {}\tCV[{}] = {}" .format(eventoEquiprovavel, valEsperado, eventoEquiprovavel, var, eventoEquiprovavel, coefVar))

def calcEstatVADiscSelec(tipoVA, probSucesso, nRepeticoes, kSucessos, repetAteSucesso, eventoEquiprovavel, taxaMedia): 
    """
    A variável tipo vai ser usada para determinar que tipo de VA discretas iremos utilizar, podendo assumir os valores:
    1 -> VA Bernoulli | 2 -> VA Binomial | 3 -> VA Geométrica | 4 -> VA Poisson
    """
    print("==========================================================")
    if tipoVA == 1:
        print("VA escolhida: Bernoulli")
        print("==========================================================")
        calcEstatVABernoulli(probSucesso)
    elif tipoVA == 2:
        print("VA escolhida: Binomial")
        print("==========================================================")
        calcEstatVABinomial(probSucesso, nRepeticoes, kSucessos)
    elif tipoVA == 3:
        print("VA escolhida: Geométrica")
        print("==========================================================")
        calcEstatVAGeometrica(probSucesso, repetAteSucesso)
    elif tipoVA == 4:
        print("VA escolhida: Poisson")
        print("==========================================================")
        calcEstatVAPoisson(eventoEquiprovavel, taxaMedia)
    else:
        print("VA inválida!!\nOpções que podem ser escolhidas:\n[1 -> VA Bernoulli | 2 -> VA Binomial | 3 -> VA Geométrica | 4 -> VA Poisson]")
        print("==========================================================")
        return -1
    print("==========================================================")


listaVal = [-1, 1, 2, 3]
listaProb = [0.25, 0.125, 0.125, 0.5]

# calcEstatVADisc(listaVal, listaProb)

# calcEstatVADiscSelec(tipoVA, probSucesso, nRepeticoes, kSucessos, repetAteSucesso, eventoEquiprovavel, taxaMedia)

calcEstatVADiscSelec(4, 90, 10, 6, 4, 3, 5)