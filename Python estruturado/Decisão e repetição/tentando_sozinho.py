idade = eval(input("Digite a idade do paciente: "))

if idade <= 13:
    print("Ele será atendido na pediatria.")
elif idade <= 18:
    print("Ele ainda será atendido na pediatria.")
else:
    print("Ele será atendido com os adultos.")

