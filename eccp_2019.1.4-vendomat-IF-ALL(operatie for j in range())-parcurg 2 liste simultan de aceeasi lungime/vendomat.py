# aprovizionare = toate valorile citite sun nule, si se va aproviziona fiecare
# categorie (stocul) cu cate 10 unitati
# vanzare = cel putin o valoare nenula, se va scadea numerele respective din stoc

# Citire date
nr_categorii = int(input())
stoc_produse = [int(x) for x in input().split()]
nr_operatii = int(input())

lista_op = []
for i in range(nr_operatii):
    tmp = [int(x) for x in input().split()]
    lista_op.append(tmp)

# Prelucrare date
nr_aprovizionari = 0
nr_vanzari_nereusite = 0
for i in range(nr_operatii):
    # daca este aprovizionare, marim stocul cu 10 pt fiecare categorie
    if all(item == 0 for item in lista_op[i]):
        nr_aprovizionari += 1
        for j in range(nr_categorii):
            stoc_produse[j] += 10
    else:  # daca este vanzare
        # daca este o vanzare reusita:
        if all(stoc_produse[j] - lista_op[i][j] >= 0 for j in range(nr_categorii)):
            for j in range(nr_categorii):
                stoc_produse[j] -= lista_op[i][j]
        # daca este o vanzare nereusita:
        else:
            nr_vanzari_nereusite += 1

print(nr_vanzari_nereusite)
print(nr_aprovizionari)
# print(stoc_produse)
