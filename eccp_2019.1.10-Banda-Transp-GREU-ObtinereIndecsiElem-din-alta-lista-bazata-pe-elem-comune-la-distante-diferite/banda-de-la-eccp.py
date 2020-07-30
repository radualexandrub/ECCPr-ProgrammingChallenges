# n = nr_esantioane (pentru senzor stanga apoi dreapta)
# Citire date
n = int(input())
senzor_L = []
senzor_R = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    senzor_L.append(tmp)
for i in range(n):
    tmp = [int(x) for x in input().split()]
    senzor_R.append(tmp)

L = "".join(str(senzor_L[i][1]) for i in range(0, n))
R = "".join(str(senzor_R[i][1]) for i in range(0, n))

# Prelucrare date
# print(senzor_L)
# print(senzor_R)
i = 0
viteze = []
detectari = 0
while i in range(n):
    index1 = i
    if L[i] == "0":
        i += 1
    elif L[i] == "1":
        # ~ Vedem cat de lunga e secventa de 1 pe care o cautam in al doilea senzor
        lungime_secv = 1
        for j in range(i + 1, n):
            if L[j] == '1':
                lungime_secv += 1
            else:
                break
        # ~
        for j in range(i + 1, n):
            if R[j] == "1":
                index2 = j
                break
            else:
                pass

        ms = abs(senzor_L[index1][0] - senzor_R[index2][0])
        viteza = 20 / ms * 10
        detectari += 1
        viteze.append(viteza)
        i += lungime_secv


viteza_medie = int(round(sum(viteze) / len(viteze)))
print(viteza_medie, detectari)
