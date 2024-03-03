'''
O QUE SÃO?

São operadores utilizados para comparar se os dois objetos testados ocupam a mesmo posição na memória
'''
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)
print(curso is not nome_curso) # negação
print(saldo is limite)

saldo = 2000
limite = 2000

print(saldo is limite)
print(saldo is not limite)