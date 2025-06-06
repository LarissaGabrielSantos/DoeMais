import tkinter as tk
from tkinter import ttk
from datetime import datetime

LOG_PATH = "log_atividades.txt"

def registrar_log(quem, o_que, acao, de_quem=None):
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if acao.lower() == "exclusão" and de_quem:
        o_que += f", De quem: {de_quem}"

    linha_log = f"{data_hora} | Quem: {quem} | Ação: {acao} | O quê: {o_que}\n"
    
    with open(LOG_PATH, "a", encoding="utf-8") as log_file:
        log_file.write(linha_log)

def criar_pagina_relatorio(root):
    frame = tk.Frame(root)

    label = tk.Label(frame, text="Relatório de Atividades", font=("Arial", 16))
    label.pack(pady=10)

    txt_log = tk.Text(frame, width=100, height=25)
    txt_log.pack(padx=10, pady=10)

    def atualizar_relatorio():
        try:
            with open(LOG_PATH, "r", encoding="utf-8") as log_file:
                conteudo = log_file.read()
                txt_log.delete(1.0, tk.END)
                txt_log.insert(tk.END, conteudo)
        except FileNotFoundError:
            txt_log.delete(1.0, tk.END)
            txt_log.insert(tk.END, "Nenhum log encontrado.")

    btn_atualizar = tk.Button(frame, text="Atualizar Relatório", command=atualizar_relatorio)
    btn_atualizar.pack(pady=5)

    atualizar_relatorio()  

    return frame
