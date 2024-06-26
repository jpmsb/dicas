#!/usr/bin/env python3

import sys
import tkinter as tk

def mostrar_cores(cores_hex):
    # Limpa mensagens de erro anteriores
    mensagem_erro.config(text="")

    # Verifica se a lista de cores é válida
    for i, cor_hex in enumerate(cores_hex):
        try:
            # Configura a cor de fundo do quadrado correspondente
            quadrados[i].config(bg=cor_hex)
        except tk.TclError:
            # Em caso de erro (ex: formato hexadecimal inválido), configura o fundo como branco
            quadrados[i].config(bg="white")
            mensagem_erro.config(text=f"Formato hexadecimal inválido para cor {i+1}! Use o formato #RRGGBB")

# Verifica se pelo menos uma cor foi fornecida
if len(sys.argv) < 2:
    print("Uso: python script.py #RRGGBB [ #RRGGBB ... ]")
    sys.exit(1)

# Recebe as cores do argumento de linha de comando
cores_hex = sys.argv[1:]

# Cria a janela principal
janela = tk.Tk()
janela.title("Visualizador de Cores")

# Cria e posiciona um Label para mostrar mensagens de erro
mensagem_erro = tk.Label(janela, text="", fg="red")
mensagem_erro.grid(row=0, column=0, columnspan=len(cores_hex))

# Cria e posiciona os quadrados coloridos
quadrados = []
for i in range(len(cores_hex)):
    quadrado = tk.Label(janela, text="", width=20, height=10, bg="white")
    quadrado.grid(row=1, column=i, padx=5, pady=10)
    quadrados.append(quadrado)

# Chama a função para mostrar as cores
mostrar_cores(cores_hex)

# Inicia o loop principal da interface gráfica
janela.mainloop()

