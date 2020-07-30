m_lin = int(raw_input())
n_col = int(raw_input())

v1 = []
for i in range(m_lin):
    for j in range(n_col):
        v1.append(int(raw_input()))

numere = [x for x in range(1,256)]

v2 = []
for numar in numere:
    if numar in v1:
        v2.append( [numar, v1.count(numar)] )

print(len(v1) - len(v2)*2)