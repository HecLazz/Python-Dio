from sys import displayhook
import pandas as pd

tabela = pd.read_excel("Vendas.xlsx")
displayhook(tabela)