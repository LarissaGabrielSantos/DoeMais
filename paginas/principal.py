import tkinter as tk
from paginas.formulario import criar_formulario
from paginas.doacoes import criar_pagina_doacoes

def criar_pagina_principal(pai, usuario_logado):
    frame = tk.Frame(pai, bg="#0c5763")
    frame.pack(expand=True, fill="both")

    menu = tk.Frame(frame, bg="#0c5763")
    menu.pack(pady=10)

    conteudo = tk.Frame(frame, bg="#0c5763")
    conteudo.pack(expand=True, fill="both")

    tk.Label(menu, text=f"Bem-vindo(a), {usuario_logado.get('nome', '')}!", bg="#0c5763", fg="white", font=("Helvetica", 13)).pack(side="left", padx=10)

    def mostrar_formulario():
        for w in conteudo.winfo_children():
            w.destroy()
        criar_formulario(conteudo)

    def mostrar_doacoes():
        for w in conteudo.winfo_children():
            w.destroy()
        criar_pagina_doacoes(conteudo, usuario_logado)

    tk.Button(menu, text="Nova Doação", command=mostrar_formulario).pack(side="left", padx=10, pady=5)
    tk.Button(menu, text="Doações Feitas Para a Comunidade", command=mostrar_doacoes).pack(side="left", padx=10, pady=5)

    mostrar_formulario()

    return frame
