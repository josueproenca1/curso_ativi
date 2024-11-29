from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk

# Classe abstrata Animal
class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def mostrar(self):
        pass

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade


# Classe concreta Cachorro
class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.porte = porte

    def mostrar(self):
        return f"Cachorro: {self.nome}, Idade: {self.idade}, Porte: {self.porte}"

    def getPorte(self):
        return self.porte

    def setPorte(self, porte):
        self.porte = porte


# Classe concreta Gato
class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def mostrar(self):
        return f"Gato: {self.nome}, Idade: {self.idade}, Raça: {self.raca}"

    def getRaca(self):
        return self.raca

    def setRaca(self, raca):
        self.raca = raca


# Lista para armazenar os animais
animais = []

# Funções para manipulação das telas
def cadastrar_animal():
    nome = entry_nome.get()
    idade = entry_idade.get()
    tipo = combo_tipo.get()

    if tipo == "Cachorro":
        porte = entry_porte.get()
        novo_animal = Cachorro(nome, idade, porte)
    elif tipo == "Gato":
        raca = entry_raca.get()
        novo_animal = Gato(nome, idade, raca)
    else:
        return

    # Adicionar o novo animal à lista
    animais.append(novo_animal)
    atualizar_lista()
    limpar_campos()

def atualizar_lista():
    lista.delete(*lista.get_children())
    for animal in animais:
        lista.insert("", "end", values=(animal.mostrar(),))

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_porte.delete(0, tk.END)
    entry_raca.delete(0, tk.END)
    combo_tipo.set("")

def habilitar_campos(event):
    tipo = combo_tipo.get()
    if tipo == "Cachorro":
        entry_porte.config(state="normal")
        entry_raca.config(state="disabled")
    elif tipo == "Gato":
        entry_porte.config(state="disabled")
        entry_raca.config(state="normal")
    else:
        entry_porte.config(state="disabled")
        entry_raca.config(state="disabled")


# Criar a interface com Tkinter
root = tk.Tk()
root.title("Sistema de Cadastro de Animais")

# Tabs
tab_control = ttk.Notebook(root)
tab_cadastro = ttk.Frame(tab_control)
tab_lista = ttk.Frame(tab_control)

tab_control.add(tab_cadastro, text="Cadastro")
tab_control.add(tab_lista, text="Lista de Animais")
tab_control.pack(expand=1, fill="both")

# Tela de Cadastro
tk.Label(tab_cadastro, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(tab_cadastro)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(tab_cadastro, text="Idade:").grid(row=1, column=0, padx=10, pady=5)
entry_idade = tk.Entry(tab_cadastro)
entry_idade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(tab_cadastro, text="Tipo:").grid(row=2, column=0, padx=10, pady=5)
combo_tipo = ttk.Combobox(tab_cadastro, values=["Cachorro", "Gato"])
combo_tipo.grid(row=2, column=1, padx=10, pady=5)
combo_tipo.bind("<<ComboboxSelected>>", habilitar_campos)

tk.Label(tab_cadastro, text="Porte (Cachorro):").grid(row=3, column=0, padx=10, pady=5)
entry_porte = tk.Entry(tab_cadastro, state="disabled")
entry_porte.grid(row=3, column=1, padx=10, pady=5)

tk.Label(tab_cadastro, text="Raça (Gato):").grid(row=4, column=0, padx=10, pady=5)
entry_raca = tk.Entry(tab_cadastro, state="disabled")
entry_raca.grid(row=4, column=1, padx=10, pady=5)

tk.Button(tab_cadastro, text="Cadastrar", command=cadastrar_animal).grid(row=5, column=0, columnspan=2, pady=10)

# Tela de Lista de Animais
lista = ttk.Treeview(tab_lista, columns=("Descrição"), show="headings")
lista.heading("Descrição", text="Descrição")
lista.pack(expand=True, fill="both")

# Executar a aplicação
root.mainloop()
