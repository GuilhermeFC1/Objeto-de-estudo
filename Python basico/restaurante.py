refrigerante = 4.99
hamburguer = 19.99
batata_frita = 9.99

quantidade_refrigerante = int(input("Digite a quantidade de refrigerantes desejados: "))
quantidade_hamburguer = int(input("Digite a quantidade de hambúrgueres desejados: "))
quantidade_batata = int(input("Digite a quantidade de batatas fritas desejados: "))

preco_total = (hamburguer * quantidade_hamburguer) + (refrigerante * quantidade_refrigerante) + (batata_frita * quantidade_batata)

print("Seu total ficou: R$", preco_total)
