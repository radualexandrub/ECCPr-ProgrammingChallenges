# dim1, dim2 = dimensiune vector 1, 2
dim1 = int(raw_input())
lista1 = []
for i in range(dim1):
    lista1.append(int(raw_input()))

dim2 = int(raw_input())
lista2 = []
for i in range(dim2):
    lista2.append(int(raw_input()))

lista = lista1 + lista2
count = 0
lista_repr = []

for i in range(len(lista)):
    count = 0
    for j in range(len(lista)):
        if lista[i] >= lista[j] and lista[i] != lista[j]:
            count += 1
    if count >= 5:
        lista_repr.append(lista[i])

x = (float(sum(lista_repr))/len(lista_repr))

print(str(x) + '0')