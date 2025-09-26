# Leitra de dados como strings:
idade_str = "25"
altura_str = "1.75"

# Conversão de tipos
idade = int(idade_str)        # Convertendo string para inteiro (int).
altura = float(altura_str)    # Convertendo string para float.

# Processando usando novos tipos de dados convertidos:
mensagem = "Idade: " + str(idade) + ", Altura: " + str(altura)
print(mensagem)
