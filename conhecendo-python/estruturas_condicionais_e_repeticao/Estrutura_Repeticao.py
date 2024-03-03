'''
FOR

O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.
'''

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letras in texto:
    if letras.upper() in VOGAIS:
        print(letras, end="")
else:
    print()

lista_preco = [100, 200, 300, 400]
imposto = 35

for preco in lista_preco:
    print(preco + imposto)

'''
FUNÇÂO RANGE

Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo). Se usarmos range(i, j) será produzido:
i, i+1, i+2, i+3, ..., j-1

Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step (opcional).
'''

# RANGE
# range(stop) -> range object
# range(start ,stop[, step]) -> range object

print(list(range(4)))

# Utilizando range com for

for numero in range(0,11):
    print(numero, end=" ")

print()

# Exibindo a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end="-")

'''
COMANDO WHILE

O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.
'''
print()

opcao = -1

while opcao != 0:
    opcao = int(input("\n[1] Sacar\n[2] Extrato\n[0] Sair\n"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar noss sistema bancário, até logo!")



while True:
    opcao_2 = int(input("Informe o número: "))

    if opcao_2 == 10:
        break
    print(opcao_2)
#  opção continue ele pula tal operação do laço, se eu colocasse o continue ao invés do break, o código apenas pularia o valor 10.
