from bestfit import Bestfit
from firstfit import Firstfit
from worstfit import Worstfit


# Best-fit
# Setup inicial da memória
print('Best-fit')

tamanho = 10
memoria = [''] * tamanho

memoria[2] = 'A'
memoria[6] = 'B'

Bestfit(memoria, 'C', 3)
Bestfit(memoria, 'D', 1)
Bestfit(memoria, 'E', 2)
Bestfit(memoria, 'F', 1)

print(memoria)


# Worst-fit
# Setup inicial da memória
print('Worst-fit')

tamanho = 10
memoria = [''] * tamanho

memoria[2] = 'A'
memoria[6] = 'B'

Worstfit(memoria, 'C', 3)
Worstfit(memoria, 'D', 1)
Worstfit(memoria, 'E', 2)
Worstfit(memoria, 'F', 1)

print(memoria)

# First-fit
# Setup inicial da memória
print('First-fit')

tamanho = 10
memoria = [''] * tamanho

memoria[2] = 'A'
memoria[6] = 'B'

Firstfit(memoria, 'C', 3)
Firstfit(memoria, 'D', 1)
Firstfit(memoria, 'E', 2)
Firstfit(memoria, 'F', 1)

print(memoria)