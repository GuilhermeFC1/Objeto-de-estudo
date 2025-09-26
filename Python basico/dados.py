def soma_numeros(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("Erro: entrada inválida.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    return None

# Testes da função com números válidos:
print(soma_numeros(2, 3))

# Testes da função com números inválidos:
print(soma_numeros("a", 3))

# Testes da função com outros tipos de dados:
print(soma_numeros(True, 3))

# Testes da função com uma lista:
print(soma_numeros([1, 2], 3))
