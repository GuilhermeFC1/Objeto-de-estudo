def encontrar_maior_elemento_iterativo(lista):
    if len(lista) <= 1:
        return lista[0]
    maior_elemento = lista[0]
    for numero in lista[1:]:
        if numero > maior_elemento:
            maior_elemento = numero
    return maior_elemento

lista_exemplo = [11, 14, 8, 6, 25, 3]
maior_elemento = encontrar_maior_elemento_iterativo(lista_exemplo)
print(f"O maior elemento da lista é: {maior_elemento}")

