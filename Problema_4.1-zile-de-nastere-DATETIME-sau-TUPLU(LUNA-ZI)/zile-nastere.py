import datetime

nr_zile = int(raw_input())

## elimin duplicatele, pun zilele-lunile intr-o noua lista de liste
zile_out = []
for i in range(nr_zile):
    x = raw_input().split('-')
    if [x[0], x[1]] not in zile_out:
        zile_out.append([x[0], x[1]])

## schimb lista de liste [dd-ll] intr-o lista simpla ['dd-ll']
## nu puteam pune zilele-lunile direct intr=o lista cu strings => apareau dubluri
zile_out2 = []
for i in range(len(zile_out)):
    zile_out2.append(str(zile_out[i][0])+'-'+str(zile_out[i][1]))

## sortare dupa zi-luna folosind modulul datetime
zile_out2.sort(key = lambda c: datetime.datetime.strptime(c, '%d-%m'))

## afisare
for i in range(len(zile_out2)):
    print(zile_out2[i])