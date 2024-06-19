import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import pandas as pd

# Função para fazer a consulta de IPs utilizando a API do IP-API.com
def consultar_ips(ips):
    resultados = []
    for ip in ips:
        try:
            response = requests.get(f'http://ip-api.com/json/{ip}?fields=status,country,as')
            data = response.json()
            if data['status'] == 'success':
                pais = data.get('country', 'N/A')
                asr = data.get('as', 'N/A')
                resultados.append({'IP': ip, 'PAÍS': pais, 'ASR': asr})
            else:
                resultados.append({'IP': ip, 'PAÍS': 'Erro', 'ASR': 'Erro'})
        except Exception as e:
            resultados.append({'IP': ip, 'País': 'Erro', 'ASR': 'Erro'})
    return resultados

# Função para carregar os IPs a partir de um arquivo
def carregar_arquivo():
    filepath = filedialog.askopenfilename(title="Selecione o arquivo de texto com IPs", filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, 'r') as file:
            ips = [line.strip() for line in file.readlines()]
        resultados = consultar_ips(ips)
        salvar_resultados(resultados)

# Função para salvar os resultados em uma planilha Excel
def salvar_resultados(resultados):
    df = pd.DataFrame(resultados)
    savepath = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if savepath:
        df.to_excel(savepath, index=False)
        messagebox.showinfo("Sucesso", "Os resultados foram salvos com sucesso!")

# Função para exibir o autor
def exibir_autor():
    messagebox.showinfo("Autor", "Nome do Autor: cybersys_br")

# Configuração da interface gráfica
def criar_interface():
    root = tk.Tk()
    root.title("Query IPs Info")

    frame = tk.Frame(root)
    frame.pack(pady=20, padx=20)

    label = tk.Label(frame, text="Selecione um arquivo de texto com uma lista de IPs:")
    label.pack(pady=10)

    button_carregar = tk.Button(frame, text="Carregar Arquivo", command=carregar_arquivo)
    button_carregar.pack(pady=10)

    button_autor = tk.Button(frame, text="Exibir Autor", command=exibir_autor)
    button_autor.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    criar_interface()
