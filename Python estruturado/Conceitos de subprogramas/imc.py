def calcula_imc (peso, altura):
    return peso * 100 / (altura * 2)

peso = eval(input("Digite o peso em kg: \n"))
altura = eval(input("Digite a altura em cm: \n"))
calcula_imc(peso, altura)
imc = calcula_imc (peso, altura)
print("imc = ", imc)


