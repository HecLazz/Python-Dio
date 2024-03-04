'''
O QUE SÃO?

São operadores utilizados em conjuntos com os operadores de comparação, para montar uma expressão lógica. Quando um operadores de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos.
'''
saldo = 1000
saque = 200
limite = 100

saldo >= saque
saque <= limite

# Operador E
print(saldo >= saque and saque <= limite)

# Operador OU
print(saldo >= saque or saque <= limite)

# Operador Negação
contatos_emergencia = [] # lista vazia é considerado falso
print(not 1000 > 1500)
print(not contatos_emergencia)
print(not "saque 15000") # String com valor = verdadeira
print(not "") # String vazia = false

# Parênteses
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # assim como na matemática os parênteses em primeiro lugar

