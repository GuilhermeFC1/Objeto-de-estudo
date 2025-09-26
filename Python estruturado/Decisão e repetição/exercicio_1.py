vrn = eval(input("Digite um número: "))
print("Valor digitado", vrn)
print("Antes do if")
if vrn <= 100:
    print("Entrou no if do 100")
elif vrn <= 500:
    print("Entrou no elif do 500")
elif vrn <= 1000:
    print("Entrou no elif de 1000")
else:
    print("Entrou no else")
print("Saiu do if")

