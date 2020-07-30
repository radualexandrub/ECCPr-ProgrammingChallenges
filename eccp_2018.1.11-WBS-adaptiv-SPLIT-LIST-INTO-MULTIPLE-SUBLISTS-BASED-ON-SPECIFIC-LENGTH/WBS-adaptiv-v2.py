# Varianta aceasta este putin mai complicata (am luat sirurile ca int, nu ca string => mai mult cod)
# N = nr elemente din sir
# n = nr elemente din fiecare bloc ce va fi codat
N = int(input())
n = int(input())
sir_tmp = []
for i in range(N):
    sir_tmp.append(int(input()))

# Split list into sublists of a specific n length
sir = []
for i in range(0, len(sir_tmp), n):
    sir.append(sir_tmp[i:i + n])

# Codare bazata pe ignorarea blocurilor compuse numai din biti 0
sir_1 = []
for i in range(len(sir)):
    if all(x == 0 for x in sir[i]) and len(sir[i]) == n:
        sir_1.append([0])
    else:
        tmp = [1]
        for x in sir[i]:
            tmp.append(x)
        sir_1.append(tmp)
sirr_1 = [0]
for i in range(len(sir_1)):
    for j in range(len(sir_1[i])):
        sirr_1.append(sir_1[i][j])
raport_1 = round(N / float(len(sirr_1)), 2)

# Codare bazata pe ignorarea blocurilor compuse numai din biti 1
sir_2 = []
for i in range(len(sir)):
    if all(x == 1 for x in sir[i]) and len(sir[i]) == n:
        sir_2.append([1])
    else:
        tmp = [0]
        for x in sir[i]:
            tmp.append(x)
        sir_2.append(tmp)
sirr_2 = [1]
for i in range(len(sir_2)):
    for j in range(len(sir_2[i])):
        sirr_2.append(sir_2[i][j])
raport_2 = round(N / float(len(sirr_2)), 2)

# Afisare
if raport_1 >= raport_2:
    print(raport_1)
    for x in sirr_1:
        print(x)
elif raport_1 < raport_2:
    print(raport_2)
    for x in sirr_2:
        print(x)
