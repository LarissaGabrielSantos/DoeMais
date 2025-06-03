import tkinter as tk
from paginas.login import criar_pagina_login
from paginas.principal import criar_pagina_principal
from bd.banco import criar_tabela

criar_tabela()

#
root = tk.Tk()
root.title("Doe+")
root.geometry("800x600")

frame_atual = None
usuario_logado = {}

def trocar_tela(nome_tela):
    global frame_atual
    if frame_atual:
        frame_atual.destroy()
    if nome_tela == "login":
        frame_atual = criar_pagina_login(root, trocar_tela, usuario_logado)
    elif nome_tela == "principal":
        frame_atual = criar_pagina_principal(root, usuario_logado)

trocar_tela("login")
root.mainloop()
