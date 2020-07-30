# 1
# 2 3
# 4 5 6
# 7 n
# P = nr de pagini al cartii
# n = indexul maxim al problemei
# determinare C = nr total de cifre care au fost utilizate in numerotarea problemelor
P, n = [int(x) for x in input().split()]
n2 = n

k = 1
i = 1
lista = []
while i in range(1, 999) and n != 0:
    j = 1
    lst = []
    while j in range(1, i + 1) and n != 0:
        lst.append(k)
        k += 1
        n -= 1
        j += 1
    lista.append(lst)
    i += 1

if len(lista) <= P:
    sir = [i for i in range(1, n2 + 1)]
    print(len(''.join(str(x) for x in sir)))
else:
    print(0)
