# Capturando tipo de exceção:
while True:
    try: 
        nr = int(input("Digite um número: "))
        s = nr * 3
        print(s)
        q = 12 / s
        print(q)
        break
    except ValueError:
        print("Digite um número válido.")
    except ZeroDivisionError:
        print("O número não pode ser zero.")
