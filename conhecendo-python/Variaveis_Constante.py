# Python consegue reconhecer o tipo de dado sem precisar declarar antes.
age = 23
name = 'Jorge'
print(f"Meu nome é {name} e eu tenho {age} anos de idade.")

# Pode ser definido várias variáveis em uma única linha, só precisa separa-las por virgula.
idade, nome = (25, "Lucas")
print(f"Meu nome é {nome} e tenho {idade} anos de idade.")

# Não podemos criar uma variável sem atribuir um valor, para alterar basta fazer um atribuição de um novo valor
age = 50
name = "Marcos"
print (f"Nome: {name}\nIdade: {age}")

# CONSTANTES - Armazena valores e permanece esse valor até o final da execução do programa, ou seja, valor é imutável.
# Em python usamos a convenção que diz ao programador que é uma constante. Para fazer isso, você deve criar a variável com o nome todo em letra maíusculas:
ABS_PATH = "hector\Documents\PYTHON"
DEBUG = True
STATES = ['SP', 'RJ', 'MG']
AMOUT = 30.2

# Práticando
limite_Saque_Diario = 1202
ESTADOS_BRASILEIROS = ["SP", "BA", "RJ", "SC" ]
print(ESTADOS_BRASILEIROS)
