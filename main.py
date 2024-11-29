import tkinter as tk
from tkinter import ttk, messagebox
from gato import Gato
from cachorro import Cachorro

animais = []

def atualizar_mensagem(mensagem, tipo="info"):
    """Atualiza o quadro de mensagens com texto colorido"""
    if tipo == "info":
        label_mensagem.config(text=mensagem, foreground="green")
    elif tipo == "erro":
        label_mensagem.config(text=mensagem, foreground="red")

def cadastrar_gato():
    nome = entry_nome.get()
    idade = entry_idade.get()
    raca = entry_info.get()
    if nome and idade and raca:
        try:
            idade = int(idade)
            gato = Gato(nome, idade, raca)
            animais.append(gato)
            atualizar_mensagem("Gato cadastrado com sucesso!")
            atualizar_contador()
        except ValueError:
            atualizar_mensagem("Idade deve ser um número!", "erro")
    else:
        atualizar_mensagem("Preencha todos os campos!", "erro")

def cadastrar_cachorro():
    nome = entry_nome.get()
    idade = entry_idade.get()
    porte = entry_info.get()
    if nome and idade and porte:
        try:
            idade = int(idade)
            cachorro = Cachorro(nome, idade, porte)
            animais.append(cachorro)
            atualizar_mensagem("Cachorro cadastrado com sucesso!")
            atualizar_contador()
        except ValueError:
            atualizar_mensagem("Idade deve ser um número!", "erro")
    else:
        atualizar_mensagem("Preencha todos os campos!", "erro")

def mostrar_lista():
    lista.delete(0, tk.END)
    for animal in animais:
        lista.insert(tk.END, animal.mostrar())

def atualizar_contador():
    label_contador.config(text=f"Animais cadastrados: {len(animais)}")

janela = tk.Tk()
janela.title("Cadastro de Animais")
janela.geometry("500x450")

# Estilo Notebook
janelinha = ttk.Notebook(janela)
janelinha.pack(fill="both", expand=True, padx=10, pady=10)

# Aba de Cadastro
tab1 = ttk.Frame(janelinha)
janelinha.add(tab1, text="Cadastro")

# Título
titulo = tk.Label(tab1, text="Cadastro de Animais", font=("Arial", 16))
titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Campos de entrada
ttk.Label(tab1, text="Nome:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_nome = ttk.Entry(tab1)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(tab1, text="Idade:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_idade = ttk.Entry(tab1)
entry_idade.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(tab1, text="Raça/Porte:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_info = ttk.Entry(tab1)
entry_info.grid(row=3, column=1, padx=10, pady=5)

# Botões de cadastro
btn_cadastrar_gato = ttk.Button(tab1, text="Cadastrar Gato", command=cadastrar_gato)
btn_cadastrar_gato.grid(row=4, column=0, padx=10, pady=10)

btn_cadastrar_cachorro = ttk.Button(tab1, text="Cadastrar Cachorro", command=cadastrar_cachorro)
btn_cadastrar_cachorro.grid(row=4, column=1, padx=10, pady=10)

# Quadro de mensagens
label_mensagem = tk.Label(tab1, text="", font=("Arial", 10), fg="green")
label_mensagem.grid(row=5, column=0, columnspan=2, pady=5)

# Aba de Lista
tab2 = ttk.Frame(janelinha)
janelinha.add(tab2, text="Lista")

# Botão para mostrar lista
btn_mostrar = ttk.Button(tab2, text="Mostrar Lista", command=mostrar_lista)
btn_mostrar.pack(pady=10)

# Lista
lista = tk.Listbox(tab2)
lista.pack(fill="both", expand=True, padx=10, pady=10)

# Rodapé com contador
rodape = tk.Frame(janela)
rodape.pack(fill="x", pady=5)

label_contador = tk.Label(rodape, text="Animais cadastrados: 0", font=("Arial", 10))
label_contador.pack()
janela.mainloop()
