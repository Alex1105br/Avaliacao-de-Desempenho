def ordenaValores(lista):
    lista.sort()


def mediaPonderada(lista):
    quantElementos = len(lista)
    soma=0
    peso=0

    for i in range(quantElementos):
        
        soma = soma + lista[i][0] * lista[i][1]
        peso = peso + lista[i][1]

    return soma//peso



def media_aritmetica(lista):
    quantElementos = len(lista)
    total = 0
    for i in range(quantElementos):
        total = total + lista[i]
    return total/quantElementos

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

    return raiz

vetorPeso = [[5,2], [4,4], [8,4]]# 37/6= 
tam = len(vetorPeso)

vetor = [18,13,11,8,10,58,12]

valoMediaGeo = mediaGeometrica(vetor)
print(valoMediaGeo)

#valorMediaPeso = mediaPonderada(vetorPeso)

#valor = vetorPeso[1][0] * vetorPeso[1][1]

#print(vetorPeso[0][0])
#print(valorMediaPeso)




