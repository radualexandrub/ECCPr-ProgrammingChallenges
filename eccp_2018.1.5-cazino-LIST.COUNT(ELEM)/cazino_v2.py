### CITIRE DATE ###
nr_carti = int(raw_input())
lista = []
for i in range(nr_carti):
    lista.append(raw_input())

### PRELUCRARE DATE ###
index = -1
for i in range(nr_carti):
    if lista.count(lista[i]) >= 3:
        index = i
        break

if index != -1:
    print(lista[index])
else:
    print("JOC OK")
    
### HAHAAHAHA ASTA INSEAMNA SA NU TE COMPLICI 