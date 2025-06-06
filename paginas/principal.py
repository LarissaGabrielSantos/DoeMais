import tkinter as tk
from tkinter import ttk, messagebox  
from paginas.formulario import criar_formulario
from paginas.doacoes import criar_pagina_doacoes
from paginas.relatorio import criar_pagina_relatorio, registrar_log
from paginas.login import criar_pagina_login

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

    def mostrar_relatorio():
        for w in conteudo.winfo_children():
            w.destroy()
        relatorio_frame = criar_pagina_relatorio(conteudo)
        relatorio_frame.pack(expand=True, fill="both")

    def logout():
        confirmar = messagebox.askyesno("Confirmação", "Deseja realmente sair?")
        if confirmar:
            registrar_log(usuario_logado.get("nome", "desconhecido"), "Logout realizado", "Logout")
            pai.trocar_tela("login")

    tk.Button(menu, text="Nova Doação", command=mostrar_formulario).pack(side="left", padx=10, pady=5)
    tk.Button(menu, text="Doações Feitas Para a Comunidade", command=mostrar_doacoes).pack(side="left", padx=10, pady=5)
    tk.Button(menu, text="Relatório", command=mostrar_relatorio).pack(side="left", padx=10, pady=5)
    tk.Button(menu, text="Sair", command=logout, bg="red", fg="white").pack(side="right", padx=10, pady=5)

    mostrar_formulario()

    return frame
