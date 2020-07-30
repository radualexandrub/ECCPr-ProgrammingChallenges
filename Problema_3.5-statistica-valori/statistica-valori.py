from math import sqrt

m_lin = int(raw_input())
n_col = int(raw_input())

# citire "matrice" -- nu avem nevoie neaparat de o matrice pentru a vedea cat de frecvente sunt elementele din aceasta (histograma)
# vom folosi o lista in care sa tinem toate elementele citite
lista = []
for i in range(m_lin * n_col):
    lista.append(int(raw_input()))

# lista contor va fi histograma noastra (cu nr de aparitii al fiecarui element citit)
contor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cifre = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in cifre:
    for j in range(len(lista)):
        if cifre[i] == lista[j]:
            contor[i] += 1

# calculare abatere medie d
medie = float(sum(contor))/len(contor)
d = 0 
for i in range(len(contor)):
    d = d + (contor[i] - medie)**2
d = sqrt(d/10)

contor_valori_mai_mari_decat_abaterea_medie = 0
for i in range(len(contor)):
    if contor[i] >= d:
        contor_valori_mai_mari_decat_abaterea_medie += 1

print(contor_valori_mai_mari_decat_abaterea_medie)
