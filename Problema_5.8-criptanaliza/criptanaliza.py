def isPrime(nr):
    return nr > 1 and all(nr % i for i in range(2,nr))

nr_numere, prag = [int(x) for x in raw_input().split()]
numere = [int(x) for x in raw_input().split()]
numere_prime = [x for x in numere if isPrime(x)]

lista = []
for i in numere_prime:
    if i >= prag:
        lista.append(i)

if len(lista) != 0:
    print min(lista)
else:
    print(-1)


