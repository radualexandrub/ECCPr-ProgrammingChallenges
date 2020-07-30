class Elev:
    def __init__(self, nume, prenume, timp):
        self.nume = nume
        self.prenume = prenume
        self.timp = timp
    def __repr__(self):
        return "{} {} {}".format(self.nume, self.prenume, self.timp) # e mai elegant sa printez obiectele astfel ...**

######## CITIRE DATE ########
nr_elevi = int(raw_input())
lista = []
for i in range(nr_elevi):
    tmp = raw_input().split()
    lista.append( Elev(tmp[0], tmp[1], int(tmp[2])) )

## De. ce. trebuia. sa. puna variabila 'barem timp' la final, dupa ce am citit lista? Sa parcurg de sapte ori, nu?? :) :) :)
# cand puteam sa elimin elevii sub barem in timp ce citeam datele la intrare
barem = int(raw_input())

######## PRELUCRARE DATE ########
lista2 = []
for i in range(nr_elevi):
    if lista[i].timp <= barem:
        lista2.append( Elev(lista[i].nume, lista[i].prenume, lista[i].timp))

lista2.sort(key = lambda c: c.timp)

######## AFISARE ########
if len(lista2) != 0:
    print len(lista2)
    for i in range(len(lista2)):
        print(lista2[i]) # **... in loc sa le convertesc in strings si sa le printez concatenate, gen: 
                         # print(lista2[i].nume + " " + lista2[i].prenume + " " + str(lista2[i].timp)) 
else:
    print 0