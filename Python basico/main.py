def multiplicador(numero):
    a = 2 #essa variavel tem o escopo local 
    print(f"Dentro dessa função, a variável vale: {a}")
    return a * numero

a = 3
b = multiplicador(5)

print(f"Fora da função, a variável a vale: {a}")

