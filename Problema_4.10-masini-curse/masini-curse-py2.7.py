# time = distance/speed

nr_km, nr_masini = [int(i) for i in (raw_input().split())]

class Masina:
    def __init__(self, index_masina, km_inceput, km_h, timp_sosire):
        self.index_masina = index_masina
        self.km_inceput = km_inceput
        self.km_h = km_h
        self.timp_sosire = timp_sosire
        
list_masini = []
timp_tmp = 0
distanta_tmp = 0

for i in range(nr_masini):
    string_km_vit = [int(x) for x in raw_input().split()]

    distanta_tmp = nr_km - string_km_vit[0]
    timp_tmp = float(distanta_tmp) / string_km_vit[1]
    
    list_masini.append(Masina(i+1, string_km_vit[0], string_km_vit[1], timp_tmp))
    
min = 99999999
lista_masini_rapide = []
for i in range(len(list_masini)):
    if list_masini[i].timp_sosire <= min:
        min = list_masini[i].timp_sosire

for i in range(len(list_masini)):
    if list_masini[i].timp_sosire == min:
        lista_masini_rapide.append(list_masini[i])

#### DACA PRINTAM IN ACEST MOD, VOM AVEA FIECARE MASINA PE CATE O LINIE: ####
# for i in range(len(lista_masini_rapide)):
#     print(lista_masini_rapide[i].index_masina)

### VOM PRINTA IN ACEST MOD, dupa modelul: ####
# array = [1, 2, 4]
# print(' '.join(str(x) for x in array))

print(' '.join(str(lista_masini_rapide[i].index_masina) for i in range(len(lista_masini_rapide))))




