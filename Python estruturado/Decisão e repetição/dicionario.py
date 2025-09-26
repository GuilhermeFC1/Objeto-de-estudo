# Criando um dicionário com alguns pares chave-valor:
dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

# Acessando e imprimindo valores individuais usando chaves:
nome = dicionario["nome"]
idade = dicionario["idade"]
cidade = dicionario["cidade"]

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Cidade: {cidade}")

# Adicionando um novo par chave-valor ao dicionário:
dicionario["profissão"] = "Engenharia"
print(f"Dicionário após adicionar profissão: {dicionario}.")

# Modificando o valo associado a uma chave existente:
dicionario["idade"] = 26
print(f"Dicionário após modificar a idade: {dicionario}.")


# Removendo um par chave-valor do dicionário:
del dicionario["cidade"]
print(f"Dicionário após remover a cidade: {dicionario}.")


# Acessando todas as chaves e valores do dicionário:
chaves = dicionario.keys()
valores = dicionario.values()

print(f"Chaves: {list(chaves)}.")
print(f"Valores: {list(valores)}.")


# Iterando sobre os pares chave-valor do dicionário:
print("Iterando sobre o dicionário:")
for chave, valor in dicionario.items():
    print(f"{chave}:{valor}")


# Verificando se uma chave existe no dicionário:
if "nome" in dicionario:
    print(f"O nome do dicionário é: {dicionario["nome"]}.")
else:
    print("A chave 'nome' não está no dicionário.")


# Usando método 'get()' para acessar valores de forma segura:
profissao = dicionario.get("profissão", "Desconhecido")
print(f"Profissão: {profissao}")


# Limpando todos os elementos do dicionário:
dicionario.clear()
print(f"Dicionário após limpar todos os elementos: {dicionario}")
