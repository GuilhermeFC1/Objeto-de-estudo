# Tuplas são estruturas de dados IMUTÁVEIS usadas para armazenar coleções ordenadas de elementos. São parecidas com as listas porém não podem ser modificadas após a criação.

tupla_heterogenea = (1, "Olá", 3.14, [10, 20, 30], {"chave": "valor"})

# Acessando e imprimindo itens individuais da tupla:
print(f"Inteiro: {tupla_heterogenea[0]}")
print(f"String: {tupla_heterogenea[1]}")
print(f"Float: {tupla_heterogenea[2]}")
print(f"Lista: {tupla_heterogenea[3]}")
print(f"Dicionário: {tupla_heterogenea[4]}")


# Modificando a lista dentro da tupla:
tupla_heterogenea[3].append(40)
print(f"Lista modificada: {tupla_heterogenea[3]}")


# Acessando um valor no dicionário dentro da tupla:
valor_dict = tupla_heterogenea[4]["chave"]
print(f"Valor no dicionario: {valor_dict}")


# Iterando sobre a tupla e imprimindo os tipos de cada elemento:
for elemento in tupla_heterogenea:
    print(f"Elemento: {elemento}, tipo: {type(elemento)}")
