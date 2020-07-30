class Nr:
    def __init__(self, dec, bin, zeros):
        self.dec = dec
        self.bin = bin
        self.zeros = zeros

###### CITIRE DATE ######
lista = []
nr_numere = int(raw_input())
for i in range(nr_numere):
    tmp_dec = int(raw_input())
    tmp_bin = bin(tmp_dec)[2:].zfill(8)
    
    count = 0
    for j in range(8):
        if '0' == tmp_bin[j]:
            count += 1
    lista.append(Nr(tmp_dec, tmp_bin, count))
    
### (optional) Afisare date citite: ###
# for i in range(len(lista)):
#     print(lista[i].dec, lista[i].bin, lista[i].zeros)
    
###### PRELUCRARE DATEish ######
max = -1
lista_out = []
for i in range(len(lista)):
    if lista[i].zeros >= max:
        max = lista[i].zeros
for i in range(len(lista)):
    if lista[i].zeros == max:
        lista_out.append(lista[i].dec)

###### AFISARE ######
for x in lista_out:
    print(x)
    
    
########################
###### EXPLICATII ######
########################
# * Ce inseamna ceva[2:] ?
# daca avem lista A = [1, 2, 3, 4, 5, 6].. indexul [2:] specifica ca taiem lista si pastram valorile de la 3 incolo (deci dam skip la primele 2 elemente din lista):
#               A[2: ] = [3, 4, 5, 6]
# 
# * print(bin(7)) va afisa "0b111" ... deci folosim [2:] pentru a scapa de "0b"
# * print(bin(7)[2:]) va afisa "111"
# 
# * functia zfill(8) va umple IN STANGA string-ului cu zerouri '0' pana cand len(string) == 8 (8 fiind argumentul functiei zfill(8)
