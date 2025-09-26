while True:
    print("Você esta no primeiro laço!")
    opcao1 = input("Deseja sair dele? Digite 'SIM' para sair. \n")
    if opcao1 == "SIM":
        break
    else: 
        while True:
            print("Você esta no segundo laço!")
            opcao2 = input("Deseja sair dele? Digite 'SIM' para sair. \n")
            if opcao2 == "SIM":
                break
            print("Você saiu do segundo laço!")
print("Você saiu do primeiro laço")
