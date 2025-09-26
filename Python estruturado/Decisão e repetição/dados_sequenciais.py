# Criando uma lista com alguns elementos: 
lista = [10, 20, 30, 40, 50]

# Acrescentando elementos individuais da lista: 
primeiro_elemento = lista[0]
segundo_elemento = lista[1]

# Imprimindo os elementos acessados: 
print(f"O primeiro elemento da lista é {primeiro_elemento}")
print(f"O segundo elemento da lista é {segundo_elemento}")

# Adicionando um elemento final da lista: 
lista.append(60)                            # O append serve para adicionar um elemeto ao final da lista.
print(f"Lista após adicionar 60: {lista}")

# Inserindo um elemento em uma posição específica:
lista.insert(2, 25)                         # O insert serve para inserir um elemento em um posição específica. No primeiro lugar do '()' é a posição desejada e no segundo lugar do '()' é o que você deseja adicionar.
print(f"Lista após inserir 25 na posição 2: {lista}")

# Removendo um elemento da lista:
lista.remove(40)                            # Remove o primeiro valor '40' encontrado na lista.
print(f"Lista após remover 40: {lista}")

# Removendo o último elemento da lista:
ultimo_elemento = lista.pop()               # O 'lista.pop()' me retorna e remove o último elemento da lista.
print(f"Elemento removido: {ultimo_elemento}")
print(f"Lista após remover o ultimo elemento: {lista}")

# Acessando um subgrupo da lista (fatiamento):
sub_lista = lista[1:4]                      # Esse '[1:4]' está pedindo a lista para me retornar os elementos nas posições 1 ate a 3.
print(f"Sub-lista (elementos de índice 1 a 3): {sub_lista}")

# Ordenando a lista: 
lista.sort()
print(f"Lista ordenada: {lista}")

# Iterando sobre os elementos da lista:
print("Iterando sobre a lista: ")
for elemento in lista:
    print(elemento)
