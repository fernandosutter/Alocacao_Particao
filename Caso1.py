from bestfit import Bestfit
from firstfit import Firstfit
from worstfit import Worstfit


# Best-fit
# Setup inicial da memória
print('Best-fit')

tamanho = 10
memoria = [''] * tamanho

memoria[1] = 'A'
memoria[6] = 'B'
memoria[7] = 'B'
memoria[8] = 'B'

Bestfit(memoria, 'C', 1)
Bestfit(memoria, 'D', 2)
Bestfit(memoria, 'E', 2)
print(memoria)


# Worst-fit
# Setup inicial da memória
print('Worst-fit')

tamanho = 10
memoria = [''] * tamanho

memoria[1] = 'A'
memoria[6] = 'B'
memoria[7] = 'B'
memoria[8] = 'B'

Worstfit(memoria, 'C', 1)
Worstfit(memoria, 'D', 2)
Worstfit(memoria, 'E', 2)

print(memoria)

# First-fit
# Setup inicial da memória
print('First-fit')

tamanho = 10
memoria = [''] * tamanho

memoria[1] = 'A'
memoria[6] = 'B'
memoria[7] = 'B'
memoria[8] = 'B'

Firstfit(memoria, 'C', 1)
Firstfit(memoria, 'D', 2)
Firstfit(memoria, 'E', 2)

print(memoria)