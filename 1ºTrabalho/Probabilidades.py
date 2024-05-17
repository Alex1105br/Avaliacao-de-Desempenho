import math
from medidasDispersao import*

def probabilidade_classica(n, m):
    #n : possibilidade equiprovavel
    #m : possibilidade favoravel
    return m/n

def distribuicaoProb(listaValAssumidos, listaMassaProbabilidade):
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

def valor_Esperado_VA(valores, probabilidades):
    tamValores = len(valores)
    resultado = 0

    for i in range(tamValores):
        resultado = resultado + (valores[i] * probabilidades[i])
    return resultado

def valor_Esperado_VA_quadrado(valores, probabilidades):
    tamValores = len(valores)
    resultado = 0

    for i in range(tamValores):
        resultado = resultado + ((valores[i]**2) * probabilidades[i])
    return resultado

def valor_Esperado_VA_VAR(valores, probabilidades):
    tamValores = len(valores)
    #tamProbabilidades = len(probabilidades)

    valor_Esperado = valor_Esperado_VA(valores, probabilidades)
    valor_Esperado2 = valor_Esperado_VA_quadrado(valores, probabilidades)

    resultado = valor_Esperado2 - (valor_Esperado**2)
    return resultado

def calcEstatisticasValAleatorios(listaValAssumidos, listaMassaProbabilidade):
    print("==================================")
    distribuicaoProb(listaValAssumidos, listaMassaProbabilidade)
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



def encontra_probabilidade_faltando(probabilidades):
    #soma = sum(probabilidades)
    soma = 0
    for i in range(len(probabilidades)):
        soma = soma + probabilidades[i]
    return round(1 - soma, 3)


# Dados fornecidos pelo exercício
idades = [16, 17, 18, 19, 20, 21, 22]
probabilidades = [0.05, 0.10, 0.15, 0.25, 0.20, 0.15, 0.10]

#Exercício do slide 22
media = valor_Esperado_VA(idades, probabilidades)
variancia = valor_Esperado_VA_VAR(idades, probabilidades)

print(f"Média (E[X]): {media}")
print(f"Variância (Var[X]): {variancia}")


# Exercício do slide 23
valores_y = [0, 1, 4, 9, 16, 25]
probabilidades_y = [0.01, 0.05, 0.25, 0.35, 0.30]  # Substitua com os valores corretos de p(y)


print(f"(a) p(4): {encontra_probabilidade_faltando(probabilidades_y)}")






