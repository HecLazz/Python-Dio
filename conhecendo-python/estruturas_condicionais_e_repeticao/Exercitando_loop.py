
# percorrer lista
lista_produto = ["faca", "garfo", "panela", "frigideira", "flavorstone"]

for produto in lista_produto: #para cada item em uma lista_de_itens
    print(produto.capitalize()) # Inicial maiúscula

# calcular o imposto sobre vários valores
lista_precos = [10, 200, 10, 50, 300]
for preco in lista_precos:
    imposto = preco * 0.1 # 10% de imposto
    print(preco + imposto)


print()
# Percorrendo um dicionário
produtos = {
        "faca": 10,
        "garfo": 10,
        "panela": 200,
        "frigideira": 50,
        "flavorstone": 300,
    }

for produto in produtos:
    print(produto.capitalize(), ": ",produtos[produto])


print()
# RANGE
for _ in range(5): # ' _ '-> esse tipo de variável é usada apenas nesse loop, pq o python obriga a criar essa variável
    print("email@gmail.com")

# Exemplo aplicado - análise de vendas
with open("C:\\Users\\hecto\\Documents\\PYTHON SUCKA BLYAT\\Python-developer\\Python-Dio\\conhecendo-python\\estruturas_condicionais_e_repeticao\\vendasloja.txt", "r") as arquivo:
    texto = arquivo.read()
lista_texto = texto.split("\n") # separarar cada linha pleo ENTER == \n
# transforma o texto em um lista no python

faturamento = 0
lista_texto = lista_texto[1:]# ignora o primeiro item e vai até o fim da lista

for linha in lista_texto:
    poisicao_pv = linha.find(";")
    valor = float(linha[poisicao_pv+1 : ])
    faturamento += valor
print(faturamento)

