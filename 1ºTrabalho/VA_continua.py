from scipy.integrate import quad
import math

#Variavel aleatória uniforme, slide 45
def variavel_aleatoria_uniforme(x, a, b):
    if a <= x < b:
        return 1 / (b - a)
    else:
        return 0

# Exemplo de uso
x = 0.5  # Valor de X
a = 0    # Limite inferior do intervalo
b = 1    # Limite superior do intervalo

#resultado = variavel_aleatoria_uniforme(x, a, b)
#print(f"f(x) para x={x}, a={a}, e b={b} é {resultado}")




#Slide 46

#Variavel aleatória uniforme

def VA_uniforme_valor_esperado(a, b):
    resultado = (a+b)/2
    return resultado

def VA_uniforme_valor_esperado_variancia(a,b):
    resultado = ((b-a)**2)/12
    return resultado

def VA_uniforme_coeficiente_variacao(a,b):
    v1 = (3 **(1/3))/3
    v2 = ((b-a)**2)/(a+b)

    return v1*v2




#Variável Aleatória Exponencial



def VA_exponencial_distribuicao_exponencial(x, a):
    e = math.e
    
    # Função Distribuição Acumulada (CDF)
    F_x = 1 - (e**(-x/a))
    
    return  F_x

def VA_exponencial_densidade_probabilidade(x, a):
    e = math.e
    expoente = (x/a)*-1
    # Função Densidade de Probabilidade (PDF)
    f_x = (1 / a) * (e**expoente)
    print("E: {}".format(e))

    return f_x

def VA_exponencial_valor_esperado(a):
    return a

def VA_exponencial_variancia(a):
    return a**2

def VA_exponencial_coeficiente_varianca():
    return 1



#Variável Aleatória Normal




def VA_normal_densidade_probabilidade(desvioPadrao, media, x):
    e = math.e
    v1 = 1 / (desvioPadrao*((2*3.14)**(1/2)))
    v2 = ((x-media)**2)/e**(((2*desvioPadrao)**2)*(-1))

    resultado = v1 * v2
    return resultado

def VA_normal_valor_esperado(media):
    return media

def VA_normal_densidade_variancia(desvioPadrao):
    return desvioPadrao**2

def VA_normal_densidade_coeficiente_variacao(desvioPadrao, media):
    return desvioPadrao/media




# Teste com valores específicos de x e a
x = 2  # Substitua pelo valor real de x
a = 3  # Substitua pelo valor real de a
#pdf, cdf = distribuicao_exponencial(x, a)

#print(f"Função Densidade de Probabilidade: {pdf}")
#print(f"Função Distribuição Acumulada: {cdf}")
