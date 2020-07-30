nr_lin = int(raw_input())
nr_col = int(raw_input())

def isPrime(nr):
    return nr > 1 and all(nr % i for i in range(2,nr))

matrice = []
for i in range(nr_lin):
    linie = []
    for j in range(nr_col):
        linie.append(int(raw_input()))
    matrice.append(linie)

count = 0
for i in range(nr_lin):
    for j in range(nr_col):
        if isPrime(matrice[i][j]):
            matrice[i][j] = 0
        else:
            matrice[i][j] = 1
            count += 1

print(count)