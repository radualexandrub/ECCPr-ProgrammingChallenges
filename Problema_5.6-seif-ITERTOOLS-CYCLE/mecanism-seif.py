import itertools

numere_seif = [int(i) for i in raw_input().split()]
nr_rotiri = int(raw_input())

numere_iter = itertools.cycle(numere_seif)

for i in range(nr_rotiri):
    rot = [int(x) for x in raw_input().split()]

    # rotire dreapta
    if rot[0] == 1:
        for j in range(rot[1]):
            next(numere_iter)

    # rotire stanga
    else:
        for j in range(len(numere_seif) - rot[1]):
            next(numere_iter)

print(next(numere_iter))
