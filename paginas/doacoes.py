import tkinter as tk
from tkinter import ttk, messagebox
from bd.banco import conectar
from paginas.relatorio import registrar_log  

tabela_global = None

def atualizar_tabela_global():
    global tabela_global
    if tabela_global is None or not tabela_global.winfo_exists():
        return
    for i in tabela_global.get_children():
        tabela_global.delete(i)
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, item, quantidade, observacoes, ong FROM doacoes")
        for row in cursor.fetchall():
            id_ = row[0]
            valores = row[1:]
            tabela_global.insert("", "end", iid=str(id_), values=valores)

def criar_pagina_doacoes(pai, usuario_logado):
    global tabela_global
    frame = tk.Frame(pai, bg="#3d6c74")
    frame.pack(expand=True, fill="both") 

    tk.Label(frame, text="Doações", font=("Arial", 20), bg="#3d6c74", fg="white").pack(pady=10)

    colunas = ["Nome completo", "Item", "Quantidade", "Observações", "ONG"]
    tabela = ttk.Treeview(frame, columns=colunas, show="headings")
    tabela_global = tabela

    scroll_y = ttk.Scrollbar(frame, orient="vertical", command=tabela.yview)
    scroll_x = ttk.Scrollbar(frame, orient="horizontal", command=tabela.xview)
    tabela.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    tabela.pack(side="top", expand=True, fill="both", padx=20, pady=10)
    scroll_y.pack(side="right", fill="y")
    scroll_x.pack(side="bottom", fill="x")

    larguras = [150, 150, 100, 200, 150]
    for col, largura in zip(colunas, larguras):
        tabela.heading(col, text=col)
        tabela.column(col, anchor="center", width=largura, minwidth=largura)

    def excluir():
        if usuario_logado.get("nome") != "adm":
            messagebox.showerror("Erro", "Apenas o usuário 'adm' pode excluir.")
            return

        item = tabela.selection()
        if not item:
            messagebox.showwarning("Aviso", "Selecione uma doação.")
            return

        confirmacao = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir?")
        if not confirmacao:
            return

        id_selecionado = item[0]
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM doacoes WHERE id=?", (id_selecionado,))
            conn.commit()

        quem = "ADM" if usuario_logado.get("nome") == "adm" else usuario_logado.get("nome")
        registrar_log(quem, f"Doação ID: {id_selecionado}", "Exclusão")

        atualizar_tabela_global()
        messagebox.showinfo("Sucesso", "Doação excluída com sucesso.")

    def editar():
        if usuario_logado.get("nome") != "adm":
            messagebox.showerror("Erro", "Apenas o usuário 'adm' pode editar.")
            return

        item = tabela.selection()
        if not item:
            messagebox.showwarning("Aviso", "Selecione uma doação.")
            return

        id_selecionado = item[0]
        valores = tabela.item(id_selecionado, "values")

        edit_win = tk.Toplevel()
        edit_win.title("Editar Doação")
        edit_win.geometry("350x350")
        edit_win.resizable(False, False)

        entradas = []
        campos = ["Nome completo", "Item", "Quantidade", "Observações", "ONG"]
        for i, campo in enumerate(campos):
            tk.Label(edit_win, text=campo).pack()
            e = tk.Entry(edit_win)
            e.insert(0, valores[i])
            e.pack()
            entradas.append(e)

        def salvar():
            novos_valores = [e.get() for e in entradas]
            with conectar() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE doacoes SET nome=?, item=?, quantidade=?, observacoes=?, ong=?
                    WHERE id=?
                """, (*novos_valores, id_selecionado))
                conn.commit()

            quem = "ADM" if usuario_logado.get("nome") == "adm" else usuario_logado.get("nome")
            registrar_log(quem, f"Doação ID: {id_selecionado}", "Edição")

            atualizar_tabela_global()
            edit_win.destroy()
            messagebox.showinfo("Sucesso", "Doação atualizada com sucesso.")

        tk.Button(edit_win, text="Salvar", command=salvar).pack(pady=10)

    tk.Button(frame, text="Editar", command=editar).pack(side="left", padx=20, pady=10)
    tk.Button(frame, text="Excluir", command=excluir).pack(side="right", padx=20, pady=10)

    atualizar_tabela_global()

    return frame
