nr_zile = int(raw_input())

lista = []
for i in range(nr_zile):
    tmp = [x for x in raw_input().split('-')] # NU TREBUIE CA LUNA, ZIUA SA FIE TIP INT, MERGE DIRECT CU STRING !!
    tmp[0], tmp[1] = tmp[1], tmp[0] # swap zi-luna -> luna-zi... desi puteam sa fac swap-ul direct in lambda la sortare..
    tmp = tuple(tmp)
    if tmp not in lista: # 'elimin' dublurile
        lista.append(tmp)

lista.sort(key = lambda c: (c[0], c[1]))
for i in range(len(lista)):
    print("{}-{}".format(lista[i][1],lista[i][0]))