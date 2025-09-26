"""
Classe sem método construtor.
Python não obriga a existência do construtor, ele somente é necessário se o objeto instanciado necessitar
de alguma ação, como a inicialiazção e/ou atribuição de valores.
"""

class A():
    def f(self):
        print("foo")

def main():
    obj_A = A()   # Objeto sendo instanciado
    obj_A.f()
    