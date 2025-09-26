import tkinter as tk

# A função 'capturar_clic' vai capturar onde na janela foi o último clique esquerdo.
def capturar_clic(event):
    x = event.x
    y = event.y
    label_coordenadas["text"] = f"Último clique: X={x}, Y={y}"

# Criando a janela:
janela = tk.Tk()
janela.title("Tratamento de Eventos - Captura de Clique Esquerdo")

# Criando a widget de rótulo:
label_coordenadas = tk.Label(janela, text="Clique em qualquer lugar da janela")
label_coordenadas.pack(padx=200, pady=100)

# Ligando o evento de clique esquerdo à função:
janela.bind("<Button-1>", capturar_clic)

# Rodando o looping principal:
janela.mainloop()

