import tkinter as tk

def clic_mouse(event):
    x = event.x
    y = event.y
    label_coordenadas["text"] = f"Ultimo clique do botão direito - X={x}, Y={y}"

janela = tk.Tk()
janela.title("Captura clique direito")

label_coordenadas = tk.Label(janela, text="Clique em qualquer lugar da janela!")
label_coordenadas.pack(padx=200, pady=100)

janela.bind("<Button-3>", clic_mouse)

janela.mainloop()
