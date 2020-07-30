###### CITIRE DATE ######
N_biti = int(raw_input())
n = int(raw_input()) # numarul de biti dintr-un bloc

biti = ""
for i in range(N_biti):
    biti = biti + raw_input()

grupe = []
for i in range(0, N_biti, n):
    grupe.append( biti[i:i+n] ) ## !!! Split list into multiple sublists based on specific length of sublist !!!
    
###### PRELUCRARE DATE ######
### CODARE BAZATA PE IGNORAREA BLOCURILOR NULE: '000' devine '0', pentru restul se adauga un '1' in fatza
cod_nul = "0"
for i in range(len(grupe)):
    if all(x == '0' for x in grupe[i]):
        cod_nul = cod_nul + '0'
    else:
        cod_nul = cod_nul + '1' + grupe[i]
raport_nul = round(float(N_biti)/len(cod_nul), 2)


### CODARE BAZATA PE IGNORAREA BLOCURILOR DE 1: '11111' devine '1', pentru restul se adauga un '0' in fatza
cod_unu = "1"
for i in range(len(grupe)):
    if len(grupe[i]) != 1 and all(x == '1' for x in grupe[i]):
        cod_unu = cod_unu + '1'
    else:
        cod_unu = cod_unu + '0' + grupe[i]
raport_unu = round(float(N_biti)/len(cod_unu), 2)

#### Afisare finala:
if raport_nul > raport_unu:
    print(raport_nul)
    for i in range(len(cod_nul)):
        print(cod_nul[i])
elif raport_unu > raport_nul:
    print(raport_unu)
    for i in range(len(cod_unu)):
        print(cod_unu[i])
elif raport_unu == raport_nul:
    print(raport_nul)
    for i in range(len(cod_nul)):
        print(cod_nul[i])
