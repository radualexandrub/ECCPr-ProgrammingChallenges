class BD: #Baza de Date
    def __init__(self, cod, tip, valoare):
        self.cod = cod
        self.tip = tip
        self.valoare = valoare

###################
###### Citire date:
lista_BD = []
nr_BD, nr_produse = [int(x) for x in raw_input().split()]
for i in range(nr_BD):
    temp = [x for x in raw_input().split()]
    lista_BD.append( BD(temp[0],temp[1],float(temp[2])) )
    
cod_produs = [x for x in raw_input().split()]

###### (optional) Afisare date citite:
# print(nr_BD, nr_produse)
# for i in range(nr_BD):
#     print(lista_BD[i].cod, lista_BD[i].tip, lista_BD[i].valoare)
# print(cod_produs)

########################
###### Prelucrare date:
suma = 0.0
reducere = 0.0

for i in range(nr_produse):
    for j in range(nr_BD):
        if cod_produs[i] == lista_BD[j].cod:
            if lista_BD[j].tip == 'p':
                suma += lista_BD[j].valoare
            else:
                reducere += lista_BD[j].valoare

suma = suma - reducere/100*suma
print(round(suma,2))