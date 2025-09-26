# Construtores e método "__init__" e "self"
# "self" é a forma da classe se referir a ela mesma.
#"__init__" é o método construtor que cria o objeto da classe.

class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

# Observe os parâmetros passados na criação do objeto.
# Instanciar uma classe é como fazer um objeto real a partir de um molde.
# Instanciando a class Conta:

def main():
    c1 = Conta(1, 1, "João", 1000)    # Objeto sendo instanciado (c1)
    print(f"Nome do títular da conta: {c1.nomeTitular}")
    print(f"Número da conta: {c1.numero}")
    print(f"CPF do títular da conta: {c1.cpf}")
    print(f"Saldo da conta: {c1.saldo}")


"""Quando um script python é executado, a váriavel reservada 
NAME referente a ele tem valor igual a '__main__'.
Nesse caso, a condição do IF a seguir será TRUE.
Então o que está no corpo do IF sera executado.
No caso, é um chamado ao método '__main__' do script"""

if __name__ == "__main__":
    main()
