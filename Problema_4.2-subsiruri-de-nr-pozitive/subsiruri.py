class Subsir:
    def __init__(self, index, subsir, lungime):
        self.index = index
        self.subsir = subsir
        self.lungime = lungime

### CITIRE DATE ###
lungime_sir = int(raw_input())
sir = [float(x) for x in raw_input().split()]

### PRELUCRARE DATE ###
if all(sir[i] < 0 for i in range(len(sir))): ### Daca toate valorile sirului sunt negative: se printeaza "-1 0"
    print("-1" + "\n" + "0")
else:
    lista = []
    tmp_subsir = []
    tmp_index = 0
    
    for i in range(lungime_sir):
        if sir[i] >= 0:
            tmp_subsir.append(sir[i])
            if sir[i-1] < 0 and i != 0:
                tmp_index = i
        else:
            tmp_subsir = []
            
        if len(tmp_subsir) != 0:
            lista.append( Subsir(tmp_index, tmp_subsir, len(tmp_subsir)) )
            
    index = 0
    max_lungime = -1
    for i in range(len(lista)):
        if lista[i].lungime > max_lungime:
            index = i
            max_lungime = lista[i].lungime
    
    print(str(lista[index].index) + '\n' + str(lista[index].lungime))
