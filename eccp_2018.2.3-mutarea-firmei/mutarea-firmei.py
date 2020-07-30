''' Problema asta este exact la fel ca Biblioteca, am scris acolo mai multe comentarii. (practic, puteam sa dau copy paste la cod) '''

# ##### CITIRE DATE ######
# D = volumul masinilor exprimat in cm^3
# k = numarul de seturi de cutii cu dimensiuni diferite... fiecare set are 'n' cutii, cutiile au fiecare la randul lor 'p' cm^3
D, k = [int(x) for x in raw_input().split()]

lista = []
for i in range(k):
    n, p = [int(x) for x in raw_input().split()]
    while n != 0:
        lista.append(p)
        n -= 1

# ##### PRELUCRARE DATE ######
for i in range(len(lista)):
    D_volum = D
    s = ""

    for i in range(len(lista)):
        if D_volum > 0 and lista[i] != 0 and lista[i] <= D_volum:
            s = s + str(lista[i]) + ' '
            D_volum -= lista[i]
            lista[i] = 0
    print(s)
