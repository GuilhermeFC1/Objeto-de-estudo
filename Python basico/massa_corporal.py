nome = "Alice"
idade = 20

# Entrada de dados do usuário:
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

# Cálculo do IMC (Índice de Massa Corporal):
imc = peso / (altura ** 2)

# Saída de dados formatada:
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura:.2f}m")
print(f"Peso: {peso:1f}kg")
print(f"IMC: {imc:.2f}")
