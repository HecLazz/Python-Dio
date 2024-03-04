'''
INTRODUÇÂO

A classe String do python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.
Em algumas linguagens manipular sequências de caracteres não é um trabalho trivial, porém, em python esse trabalho é muito simples.
'''

curso = "   Python  "
print(curso.strip())

curso = "Python"
print(curso.center(10,"="))
print(".".join(curso).center(20, "="))

texto = "hec@gmail.com"
print(len(texto)) # Tamanho da string
print(texto.find("@")) # achar onde essa letra esta na string

posicao = texto.find("@")
print(texto[posicao + 1: ])