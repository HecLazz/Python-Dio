'''
Em alguns momentos é necessário converter o tipo de uma variável para manipular de forma diferente. Por Exemplo:
    Variáveis do tipo String, que armazenam números e precisamos fazer alguma operação matemática com esse valor.
'''

#Inteiro para Float
preco = 10
preco = float(preco)
print(preco)

preco = 10 / 2 # divisão gera como resultado um valor de ponto flutuante
print(preco)

# Float para Inteiro
preco = 10.30
print(preco)

preco = int(preco)
print(preco)

print(preco // 2) # Utilizando duas barras, o número inteiro é preservado

# Número para String
preco = 10.50
idade = 28
print(str(preco))
print(str(idade))

texto = f"idade {idade} preco {preco}"
print(texto)

# String para Número
preco = "10.50"
idade = "28"

print(float(preco))
print(int(idade))

a = "10"
a = int(a)
print(type(a))