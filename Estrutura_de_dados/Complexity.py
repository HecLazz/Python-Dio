# exemplo para entender o conceito do complexidade

def inverter_lista(lista):
    tamanho = len(lista)
    limite = tamanho//2
    for i in range(limite):
        aux = lista[i]
        lista[i] = lista[n-1]
        lista[i-1] = aux

# 4 + N memória - complexidade de espaço
# 2 + 2 * N - complexidade de tempo -- 2 == operações antes do for // 4 * (N/2) == 3 operações que são repetidas n/2 vezes -- mas fazendo o calculo 4*(N/2) == 2*N

# 2*N é a operação dominante, pois ele vai demandar o tanto de recurso que o algoritmo vai realizar

def inveter_lista2(lista):
    nova_lista=[]
    tamanho = len(nova_lista)

    for i in range(tamanho):
        nova_lista.append(tamanho - i)
    return nova_lista

# 2+N tempo
# 3 + 2 * N espaço