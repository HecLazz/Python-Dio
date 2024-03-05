# Old Style %
nome = "guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

# Método Format
print("Olá, me chamo {}. eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

# F-String
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos, trabalho como {profissao} e estou matriculado no curso de {linguagem}")

# Formatar string com f-string
PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")
