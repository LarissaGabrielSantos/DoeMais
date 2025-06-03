# paginas/formulario.py
import tkinter as tk
from tkinter import messagebox
from bd.banco import conectar
from paginas.doacoes import atualizar_tabela_global

def criar_formulario(pai):
    frame = tk.Frame(pai, bg="#466064") 
    frame.pack(expand=True, fill="both")

    tamanho_fonte_emoji = 35
    label_pombas = tk.Label(frame, text="🕊️🕊️🕊️🕊️", font=("Arial", tamanho_fonte_emoji), bg="#466064") # ou bg="#173438" se quiser um fundo diferente
    label_pombas.pack(pady=(10, 5))

    tk.Label(frame, text="Faça uma doação", font=("Helvetica", 18, "bold"), bg="#466064", fg="white").pack(pady=10)
    tk.Label(frame, text="Você não sabe o quanto a sua ajuda é importante, por mais simples que pareça. Vale a pena, pratique este ato de amor.", font=("Helvetica", 10), bg="#466064", fg="white").pack(pady=10)

    campos = ["Nome completo", "Item", "Quantidade", "Observações"]
    entradas = []

    for campo in campos:
        tk.Label(frame, text=campo, bg="#466064", fg="white").pack()
        entrada = tk.Entry(frame)
        entrada.pack()
        entradas.append(entrada)

    tk.Label(frame, text="ONG", bg="#466064", fg="white").pack()
    ong_var = tk.StringVar()
    ong_var.set("ONG Esperança")
    opcoes_ongs = ["ONG Esperança", "ONG Amor ao Proximo", "ONG Cuidar", "ONG Unidos por Todos", "ONG Mundo Melhor"]
    tk.OptionMenu(frame, ong_var, *opcoes_ongs).pack()

    var1 = tk.IntVar()
    var2 = tk.IntVar()

    tk.Checkbutton(frame, text="Aceita os termos?", variable=var1, bg="#466064").pack()
    tk.Checkbutton(frame, text="Confirmar doação?", variable=var2, bg="#466064").pack()

    def doar():
        if not var1.get() or not var2.get():
            messagebox.showwarning("Aviso", "Você precisa aceitar os termos.")
            return

        valores = [e.get() for e in entradas]
        if not all(valores):
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO doacoes (nome, item, quantidade, observacoes, ong) VALUES (?, ?, ?, ?, ?)",
                           (*valores, ong_var.get()))
            conn.commit()

        atualizar_tabela_global()
        messagebox.showinfo("Sucesso", "Doação registrada.")
        for e in entradas:
            e.delete(0, tk.END)

    tk.Button(frame, text="Doar", command=doar).pack(pady=10)

    tamanho_fonte_emoji = 35
    label_pombas = tk.Label(frame, text="🕊️🕊️🕊️🕊️", font=("Arial", tamanho_fonte_emoji), bg="#466064") # ou bg="#173438" se quiser um fundo diferente
    label_pombas.pack(pady=(10, 5))

    return frame 