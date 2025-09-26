# Utilizando a biblioteca Numpy para calcular as raízes:

import numpy as np

# Função para calcular as raízes da equação de segundo grau:

def calcular_raizes(a, b, c):
    # Passando os coeficientes:
    coeficientes = [a, b, c] 

    # Usando o numpy.roots para calcular as raízes:
    raizes = np.roots(coeficientes)
    return raizes

# Solicitando os coeficientes ao usuário:
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente b: "))

# Calculando as raízes:
raizes = calcular_raizes(a, b, c)

# Imprimindo os resultados:
print(f"As raízes da equação são: {raizes[0]} e {raizes[1]}.")

