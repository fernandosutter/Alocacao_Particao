# First-fit

# memoria - Variavel que representa a memoria nos casos
# programa - Qual programa será inserido na memoria
# tamanho - Qual o tamanho do programa a ser inserido na memoria.

def Firstfit(memoria, programa, tamanho):
    vazio = 0
    for i in range(0, 10):
        if memoria[i] == '' and tamanho == 1:
            memoria[i] = programa 
            break
        if memoria[i] == '':
            vazio += 1
        if memoria[i] != '':
            vazio = 0
        if vazio == tamanho:
            posini = (i+1) - vazio
            for j in range(posini, i+1):
                memoria[j] = programa
            break
    else:
        print("Não é possível alocar o programa " + programa + " na memória!!!")
    return memoria
    