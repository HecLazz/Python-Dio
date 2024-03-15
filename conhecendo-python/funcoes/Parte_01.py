'''
O QUE SÃO FUNÇÕES?

Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros, esses parâmetros podem ou não ter valores padrões. Usar funções torna o código mais legível e possibilita o reaproveitamento de código. Programar baseado em funções, é o mesmo que dizer que estamos programando de maneira estruturada.
'''

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

'''
RETORNANDO VALORES

Para retornar um valor, utilizamos a palavra reservada return. Toda função python retorna none por padrão. diferente de outras linguagens de programação, em python uma função pode retornar mais de um valor.
'''

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor



print(calcular_total([10,20,34]))
print(retorna_antecessor_e_sucessor(10))

'''
Argumentos nomeados

Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor
'''

def salvar_carro(marca,modelo,ano,placa):
    print(f"Carro inserido com sucesso ! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat","Palio",1999, "abc-223")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "abd-334"})

'''
Args e Kwargs

Podemos combinar parâmetros obrigatório com args e kwargs. Quando esses são definidos (*args e **kwargs), o método recebe os valores como tupla e dicionário respectivamente.
'''

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of Python", "Beautiful is better tahn ugly.", autor="Tim Peters", ano=1999)


'''
 Parâmetros especiais

 Por padrão, argumento podem ser passados para um função python tanto por posição quanto explicitamente pelo nome. Para um melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, assim um dev precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome, ou por nome

'''

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-2345", marca="Fiat", motor="1.0", combustivel="Gasolina")

# Keyword only

def criar_carro2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro2(modelo="Shelby GT500", ano=2018, placa="HEC-666", marca="Ford", motor="V8", combustivel="Gasolina")

'''
Objetos de primeira classe

Em python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos de primeira classe. Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados (lista, tuplas, dicionários, etc) e usar como valor de retorno para um função (closures).
'''

def somar(a,b):
    return a + b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10,10,somar)

op = somar

print(op(1,23))

'''
Escopo local e escopo global

Python trabalha com escopo local e global, dentro do bloco da função e escopo é local. Portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado. Para usar objetos globais utilizamos a palavra-chave global, que informa ao interpretador que a variável que está sendo manipulado no escopo local é global. essa não é um boa prática e deve ser evitada
'''

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))