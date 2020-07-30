# 5, 15, 25 bani, 1, 3, 5 lei
# set util =
# !) 8 <= nr total monede din set <= 20;
# 2) valoare max 29 lei;
# 3) majoritatea monedelor au valori mai mici de 1 leu
# 4) contine TOATE tipurile de valori
# n = nr_seturi, k = nr_monede_din_set

# Citire
seturi = []
n = int(input())
for i in range(n):
    k = int(input())
    numere = [int(x) for x in input().split()]
    seturi.append(numere)

# Prelucrare
toate_val = [5, 15, 25, 100, 300, 500]
s = []
for i in range(len(seturi)):
    count_mici = 0
    count_mari = 0
    for j in range(len(seturi[i])):
        if seturi[i][j] < 100:
            count_mici += 1
        else:
            count_mari += 1

    val = True
    for x in toate_val:
        if x not in seturi[i]:
            val = False

    if 8 <= len(seturi[i]) <= 20 and sum(seturi[i]) <= 2900 and count_mici > count_mari and val:
        s.append(1)
    else:
        s.append(0)

print(' '.join(str(x) for x in s))
print("{0:.2f}".format(s.count(0) / len(s)))
