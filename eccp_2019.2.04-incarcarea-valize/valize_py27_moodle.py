# o "greutate" are un numar de pachete care au anumite greutati fiecare (fiecare pachet)
kg_valiza, nr_greutati = raw_input().split()
kg_valiza = int(kg_valiza)
nr_greutati = int(nr_greutati)

# pun toate pachetele intr-o singura lista
total_pachete = []
for i in range(nr_greutati):
    nr_pachete_si_kg = raw_input().split()
    nr_pachete = int(nr_pachete_si_kg[0])
    kg_pachet = int(nr_pachete_si_kg[1])
    while nr_pachete != 0:
        total_pachete.append(kg_pachet)
        nr_pachete -= 1

# mutare pachete in cate o valiza (lista de elemente), mutare valize in lista(=> lista de lista de elemente)
nr_valize = []
o_valiza = []
pachete_finalizat = 0

while pachete_finalizat != len(total_pachete):
    temp_kg = kg_valiza
    pachete_finalizat = 0
    o_valiza = []

    for j in range(len(total_pachete)):
        if temp_kg - total_pachete[j] >= 0 and total_pachete[j] != 0:
            o_valiza.append(total_pachete[j])
            temp_kg = temp_kg - total_pachete[j]
            total_pachete[j] = 0

    nr_valize.append(o_valiza)

    for j in range(len(total_pachete)):
        if total_pachete[j] == 0:
            pachete_finalizat += 1
        else:
            break

# afisare lista de liste
for i in range(len(nr_valize)):
    s = ""
    for j in range(len(nr_valize[i])):
        s = s + str(nr_valize[i][j]) + " "
    print(s)
