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
memoria[9] = 'G'

Bestfit(memoria, 'C', 2)
Bestfit(memoria, 'D', 3)
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
memoria[9] = 'G'

Worstfit(memoria, 'C', 2)
Worstfit(memoria, 'D', 3)
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
memoria[9] = 'G'

Firstfit(memoria, 'C', 2)
Firstfit(memoria, 'D', 3)
Firstfit(memoria, 'E', 2)
Firstfit(memoria, 'F', 1)

print(memoria)