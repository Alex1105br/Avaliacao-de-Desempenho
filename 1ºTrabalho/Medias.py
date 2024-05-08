def ordenaValores(lista):
    lista.sort()


def mediaPonderada(lista):
    quantElementos = len(lista)
    soma=0
    peso=0

    for i in range(quantElementos):
        
        soma = soma + lista[i][0] * lista[i][1]
        peso = peso + lista[i][1]

    return round(soma/peso)



def media_aritmetica(lista):
    quantElementos = len(lista)
    total = 0
    for i in range(quantElementos):
        total = total + lista[i]
    return round(total/quantElementos, 1)

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

    return round(raiz, 1)



def mediaHarmonica(lista):
    quantElementos = len(lista)
    valor = 0

    for i in range(quantElementos):
        valor = valor + (1/lista[i])
    
    return round(quantElementos/valor, 1)



def mediaTaxas(lista):
    quantElementos = len(lista)
    somaTaxas = 0 #taxas de perdas
    somaDuracaoMedicao = 0

    

    for i in range(quantElementos):
        
        somaTaxas = somaTaxas + lista[i][1]
        somaDuracaoMedicao = somaDuracaoMedicao + lista[i][0]
    
    resultadoTaxas = somaTaxas/quantElementos
    resultadoMedicao = somaDuracaoMedicao/quantElementos

    resultado = resultadoTaxas/resultadoMedicao
    resultado = resultado*100

    return round(resultado, 1)

    


def moda(lista):
    frequencia = {}
    
    # Contagem da frequência de cada elemento no vetor
    for elemento in lista:
        if elemento in frequencia:
            frequencia[elemento] += 1
        else:
            frequencia[elemento] = 1
    
    # Encontrar o elemento com a maior frequência
    moda = None
    max_frequencia = 0
    for elemento, freq in frequencia.items():
        if freq > max_frequencia:
            moda = elemento
            max_frequencia = freq
    
    return moda

# Exemplo de uso da função moda
vetor = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]
print("Moda:", moda(vetor))


def calculaModa(lista):
    contagem_elementos = {}
    
    # Contar a frequência de cada elemento na amostra
    for elemento in lista:
        if elemento in contagem_elementos:
            contagem_elementos[elemento] += 1
        else:
            contagem_elementos[elemento] = 1
    
    # Encontrar a contagem máxima
    contagem_maxima = max(contagem_elementos.values())
    
    # Encontrar todos os elementos com a contagem máxima
    modas = [elemento for elemento, contagem in contagem_elementos.items() if contagem == contagem_maxima]
    
    return modas

#vetorTaxa = [[100,3.0], [100,5.0], [100,4.2], [100, 5.2], [100, 8.6]]


#tam = len(vetorPeso)

#vetor = [18,13,11,8,10,58,12]
#vetor = [405, 367, 405, 419, 388]

#valorMedia = mediaTaxas(vetorTaxa)

#print(valorMedia)


#valorMediaPeso = mediaPonderada(vetorPeso)

#valor = vetorPeso[1][0] * vetorPeso[1][1]

#print(vetorPeso[0][0])
#print(valorMediaPeso)




"""
def calcular_media_apropriada(amostra):
    # Verificar se a amostra está vazia
    if not amostra:
        return None
    
    # Verificar se todos os elementos da amostra são iguais
    if len(set(amostra)) == 1:
        return amostra[0]
    
    # Verificar se há valores negativos na amostra
    if any(x < 0 for x in amostra):
        return media_aritmetica(amostra)
    
    # Verificar se há valores positivos na amostra
    if any(x > 0 for x in amostra):
        # Calcular o produto dos elementos da amostra
        produto = 1
        for valor in amostra:
            produto *= valor
        
        # Se o produto for positivo, usar média geométrica
        if produto > 0:
            return mediaGeometrica(amostra)
        
        # Se o produto for negativo, usar média harmônica
        return mediaHarmonica(amostra)
    
    # Caso nenhum dos critérios anteriores se aplique, usar a média aritmética
    return media_aritmetica(amostra)


amostra_1 = [2, 4, 6, 8, 10]  # Todos os valores são positivos
amostra_2 = [-3, -1, 0, 2, 4]  # Existem valores positivos e negativos
amostra_3 = [1, 1, 1, 1, 1]  # Todos os valores são iguais

# Exemplo de uso da função calcular_media_apropriada com diferentes amostras
print("Amostra 1:", calcular_media_apropriada(amostra_1))
print("Amostra 2:", calcular_media_apropriada(amostra_2))
print("Amostra 3:", calcular_media_apropriada(amostra_3))

"""