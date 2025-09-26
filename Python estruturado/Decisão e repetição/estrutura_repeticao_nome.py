nomes = ["Laura", "Valentina", "Liz", "Guilherme", "Roberto"]

for nome in nomes:
    if nome == "Liz":
        continue   # O "continue" serve para que o debugador se encontrar o que o comando "if" quer, no caso seria o nome "Liz", ele leia esse nome se existir, não mostra ele e continue mostrando o restante.
    print(nome)
