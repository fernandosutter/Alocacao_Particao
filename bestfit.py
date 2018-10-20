# Best-fit

# memoria - Variavel que representa a memoria nos casos
# programa - Qual programa será inserido na memoria
# tamanho - Qual o tamanho do programa a ser inserido na memoria.


def Bestfit(memoria, programa, tamanho): 
    lentamanho = tamanho
    space = []
    r = []
    for i in range(0, 10):
        vazio = 0
        if memoria[i] == '':
            r.append(i)
        if memoria[i] != '':
            if len(r)> 0: 
                space.append(r)
                r = [] 
                  
        if memoria[i] == '' and i == 9:
            space.append(r) 
    space2 = []
    r2 = []
    for i in range (0, len(space)):
        r2 = (len(space[i]) - tamanho)  
        space2.append(r2)
    aux = []
    vazio = 0
    sub = False
    for i in range(0, 10):
        if memoria[i] == '':
            vazio += 1
            sub = False
        if memoria[i] != '' and sub == False:
            aux.append(vazio)
            vazio = 0
            sub = True
        if memoria[i] == '' and i == 9:
            aux.append(vazio)
    

    menor = min(aux)
    alcance = []

    

    for j in space:
        if len(j) >= menor:
            alcance = j
            
          
    if len(alcance) >= tamanho:
        for h in alcance:
            memoria[h] = programa
            lentamanho -= 1
            if lentamanho == 0 or h > 9:
                break     
    else:
        print("Não é possível alocar o programa " + programa + " na memória!!!")
        

    return memoria

            
        
    
    
