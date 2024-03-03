'''
O QUE SÃO?

A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.


IF

- Para criar um estrutura condicional simples, compostar por um único desvio, podemos utilizar a palavra reservado if. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas
'''

import sys


saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
if saldo < saque:
    print("Saldo insuficiente!")

'''
IF / ELSE

Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else. Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado. Caso contrário o bloco de código do else será executado.
'''

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

'''
IF / ELIF / ELSE

Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada elif. O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do elif será executado. Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código.
'''

opcao = int(input("Informe uma opção: [1] Sacar\n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    print(f"Saque realizado com sucesso no valor de R$: {valor}")

elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("opção inválida")

# testes
carteira_cliente = 500.0
valor_produto = 15.50
quantidade = int(input("Quantos será comprado: "))

valor_final = quantidade * valor_produto

if carteira_cliente > valor_final:
    print("Compra efetuada com sucesso!")
    print(f"Muito obrigado pela compra!\nValor: {valor_final}\nQuantidade: {quantidade}")
else:
    print("Saldo insuficiente")

'''
If Aninhado

Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de estruturas if/elif/else
'''
conta_normal = True
conta_universitaria = False
saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com cheque especial")
    else:
        print("Saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")
else:
    print("Sistema não reconheceu esse tipo de conta, entre em contato com o gerente.")

'''
If Ternário

O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes:
1 - o retorno caso a expressão retorne verdadeiro;
2 - a expressão lógica;
3 - o retorno caso a expressão não seja atendida;
'''
saldo = 2000
saque = 1500
status = "Sucesso" if saldo >= saque else "Falha" # utilizado para ações mais simples
print(f"{status} ao realizar o saque!")