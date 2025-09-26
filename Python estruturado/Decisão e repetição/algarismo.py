for num in range(1000, 10000):
    menor = num % 100     # Obtem o número dos algarismos menos significativos.
    maior = num // 100    # Obtem o número dos algarismos mais significativos.
    raiz = menor + maior  # Obtem a raiz.

    if (raiz * raiz) == num:    # Valida se a raiz gera o número testado.
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print("Terminou")
print("Saiu", num)
