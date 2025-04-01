import tkinter as tk
from tkinter import ttk
from src.converter import converter_moeda

def converter():
    """Converte o valor inserido e exibe o resultado."""
    valor = valor_entry.get()
    moeda_origem = moeda_origem_combo.get()
    moeda_destino = moeda_destino_combo.get()

    # Verifica se o valor inserido é um número
    try:
        valor = float(valor)
    except ValueError:
        resultado_label.config(text="Erro: Valor inválido.", foreground="red")  # Correção: foreground em vez de fg
        return

    mensagem_resultado = converter_moeda(valor, moeda_origem, moeda_destino)
    resultado_label.config(text=mensagem_resultado, foreground="black")  # Correção: foreground em vez de fg

# Configuração da janela principal
janela = tk.Tk()
janela.title("Conversor de Moedas")
janela.geometry("400x250")
janela.configure(bg="#f0f0f0")

# Estilo para os widgets
estilo = ttk.Style()
estilo.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
estilo.configure("TButton", font=("Arial", 12), padding=5)
estilo.configure("TCombobox", font=("Arial", 12))

# Widgets
titulo_label = tk.Label(janela, text="Conversor de Moedas", font=("Arial", 16, "bold"), bg="#f0f0f0")
titulo_label.pack(pady=10)

valor_label = ttk.Label(janela, text="Valor:")
valor_label.pack()
valor_entry = ttk.Entry(janela, font=("Arial", 12))
valor_entry.pack()

moedas = ["USD", "EUR", "BRL", "JPY", "GBP"]

moeda_origem_label = ttk.Label(janela, text="Moeda de Origem:")
moeda_origem_label.pack()
moeda_origem_combo = ttk.Combobox(janela, values=moedas)
moeda_origem_combo.current(0)
moeda_origem_combo.pack()

moeda_destino_label = ttk.Label(janela, text="Moeda de Destino:")
moeda_destino_label.pack()
moeda_destino_combo = ttk.Combobox(janela, values=moedas)
moeda_destino_combo.current(1)
moeda_destino_combo.pack()

converter_botao = ttk.Button(janela, text="Converter", command=converter)
converter_botao.pack(pady=10)

resultado_label = ttk.Label(janela, text="")
resultado_label.pack()

janela.mainloop()