class Zi:
    def __init__(self, pret, aroma):
        self.pret = pret
        self.aroma = aroma


#### CITIRE DATE ####
nr_zile = int(raw_input())
bani_per_zi = [int(x) for x in raw_input().split()]
lista = []
for i in range(nr_zile):
    pret, aroma = [int(x) for x in raw_input().split()]
    lista.append(Zi(pret, aroma))

#### PRELUCRARE DATE ####
buget = 0
fericire = 0
max_aroma = 0

for i in range(nr_zile):
    buget += bani_per_zi[i]

    if lista[i].pret <= buget:
        buget -= lista[i].pret
        fericire += lista[i].aroma
        if lista[i].aroma >= max_aroma:
            max_aroma = lista[i].aroma

    elif lista[i].aroma >= max_aroma:
        fericire -= lista[i].aroma

print(fericire)
