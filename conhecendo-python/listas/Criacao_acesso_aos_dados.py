'''
CRIANDO LISTA

listas em python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas utilizando o construtor list, a função range ou colocando valores separados por vírgular dentro de colchetes. Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.
'''

frutas = ["laranja", "maça", "uva"]
Frutas = []
letras = list("python") # uma lista em que cada letra é um elemento
print(letras)
numeros = list(range(10))
print(numeros)
carro = ["Ferrari", "F8", 42000000, 2020, 2900, "são paulo", True]

'''
Acesso Direto

A lista é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero?
'''
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[-1]) # último elemento da lista
print(frutas[-2])

'''
Listas aninhadas

Listas podem armazenar todos os tipos de objeto Python, portanto podemos ter lista que armazenam outras listas. Com isso podemos criar estruturas bidimensionais (tabela), e acessar informando os índices de linha e coluna.
'''

matriz = [[],[],[]]
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
print(matriz[0]) # valor de 1 linha
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])
print(matriz[0:])

'''
Fatiamento

Além de acessar elementos diretamente, podemos extrair um conjunto de valores de sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursos deve "pular" no acesso.
'''
lista = ["p","y","t","h","o","n"]

lista[2:]
lista[:2]
lista[1:3]
lista[0:3:2]
lista[::]
lista[::-1]

'''
Iterar Lista

A forma mais comum para percorrer os dados de uma lista é utilizando o comando for.
'''
carros = ["gol", "celta", "palio"]
for carro in carros:
    print(carro)

'''
Função Enumerate

Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate 
'''
for indice,carro in enumerate(carros):
    print(f"{indice+1}: {carro}")

'''
Compreensão de listas

A compreensão de lista oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.
'''

# Filtro versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero) # adiciona valor a lista

# Filtro versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

# Modificando valores versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

# Modificando valores versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]

# [].append
lista = []

lista.append(1)
lista.append("Python")
lista.append([40,30,20])

print(lista) # [1, "python", [40,30,20]]

lista.clear()
print(lista)

# [].copy
lista = [1, "python", [40,30,20]]
l2 = lista.copy() # Lista igual mas não é a mesma instância
print(lista)

print(id(lista), id(l2))

# [].count
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

# [].extend
linguagem = ["python", "js", "c"]
print(linguagem)

linguagem.extend(["java", "csharp"])
print(linguagem)

#[].index
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))
print(linguagens.index("python"))