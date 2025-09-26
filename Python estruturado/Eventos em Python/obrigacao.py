# Obrigado a digitar um número válido.

while True:
    try:
        nr = eval(input("Digite um número: "))
        s = nr * 3
        print(s)
        q = 12 / 2
        print(q)
    except ValueError:
        print("Entre com um valor válido.")
