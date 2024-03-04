# Adição, Subtração e Multiplicação
print(1 + 1)
print(10 - 2)
print(4 * 3)

# Divisão e Divisão inteira
print(12 / 3)
print(12 // 2)

# Módulo e Exponenciação
print(10 % 3)
print(1 ** 3)

'''
PRECEDÊNCIA DE OPERADORES

NA MATEMÁTICA
- Existe uma regra que indica quais operações devem ser executadas primeiro. Isto é útil pois ao analisar uma expressão, a depender da ordem das operações o valor pode ser diferente:

x = 10 - 5 * 2
x é igual a 10 ou 0?

A definição indica a seguinte ordem como a correta:
- Parêntesis
- Expoêntes
- Multiplicações e divisões (da esquerda para a direita)
- Soma e subtração (da esquerda para a direita)
'''
print(10 - 5 * 2)
print((10 - 5) * 2)
print(10 ** 2 * 2)
print(10 ** (2 * 2))
print(10 / 2 * 4)

produto_1 = 10
produto_2 = 20

print(produto_1 + produto_2)
print(produto_1 - produto_2)

novo_preco = ((produto_1 + produto_2) * 5 / 100)
print((produto_1 + produto_2) - novo_preco)
