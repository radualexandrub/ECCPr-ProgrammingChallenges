### Citire Date
nr_ingrediente = int(input())
stoc = [int(x) for x in input().split()]
nr_operatii = int(input())
lista = []

for i in range(nr_operatii):
    lista.append( [int(x) for x in input().split()] )

### Prelucrare date
solicitari_reusite = 0
aprovizionari = 0

for i in range(len(lista)):
    ## daca este aprovizionare:
    if all(lista[i][j] == 0 for j in range(nr_ingrediente)):
        aprovizionari += 1
        for j in range(nr_ingrediente):
            stoc[j] += 15
    
    ## altfel daca este solicitare reusita:
    elif all(stoc[j] - lista[i][j] >= 0 for j in range(nr_ingrediente)):
        solicitari_reusite += 1
        for j in range(nr_ingrediente):
            stoc[j] -= lista[i][j]

print(solicitari_reusite)
print(aprovizionari)
# print(stoc)