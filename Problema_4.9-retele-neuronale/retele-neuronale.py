###### CITIRE DATE ######
# m = nr neuroni din stratul de intrare: I
# n = nr neuroni din stratul de iesire: O -> iesirile neuronilor iesire vor fi Y
# p = nr neuroni din stratul ascuns: H -> iesirile neuronilor ascunsi vor fi S
m, n, p = [int(x) for x in raw_input().split()]

# ponderile vij sub forma unei matrice de numere intregi cu m linii si n coloane, separate prin spatiu (ponderea conexiunii Ii - Hj)
ponderi_v = []
for i in range(m):
    tmp = [int(x) for x in raw_input().split()]
    ponderi_v.append(tmp)

# ponderile wjk sub forma unei matrice de numere intregi cu n linii si p coloane, separate prin spatiu (ponderea conexiunii Hj - 0k)
ponderi_w = []
for i in range(n):
    tmp = [int(x) for x in raw_input().split()]
    ponderi_w.append(tmp)
    
# vectorul de parametri de intrare Xi sub forma unui sir de m numere intregi separate prin spatiu
X = [int(x) for x in raw_input().split()]

###### PRELUCRARE DATE ######
#### ETAPA 1: Calcularea valorilor pentru iesirile neuronilor din stratul ascuns
S = []
for j in range(n):
    s = 0
    for i in range(m):
        s = s + X[i] * ponderi_v[i][j]
    S.append(s)

#### ETAPA 2: Calcularea valorilor pentru iesirile neuronilor din stratul de iesire
Y = []
for j in range(p):
    y = 0
    for i in range(n):
        y = y + S[i] * ponderi_w[i][j]
    Y.append(y)

#### ETAPA 3: Gasirea indexului valorii Yk maxime
max = -1
index = 0
for i in range(len(Y)):
    if Y[i] > max:
        max = Y[i]
        index = i + 1
print(index)

# print(Y.index(max(Y))+1)