nr_valori = int(raw_input())

suma_valori = []
for i in range(nr_valori):

    valori = [int(i) for i in raw_input().split()]
    
    # prima etapa cifrare:
    i = 0
    while i in range(len(valori)-2):
        tmp = valori[i]
        valori[i] = valori[i+1]
        valori[i+1] = tmp
        i = i + 2
    
    # a doua etapa cifrare:
    for i in range(1,len(valori)):
        valori[i] = valori[i] % 2
    suma = sum(valori)
    
    suma_valori.append(suma)
    
print(max(suma_valori))