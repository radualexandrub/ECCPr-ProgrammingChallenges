class Concert:
    def __init__(self, oras, zi, luna, pret, distanta, pret_total):
        self.oras = oras
        self.zi = zi
        self.luna = luna
        self.pret = pret
        self.distanta = distanta
        self.pret_total = pret_total
    def __repr__(self):
       return "{} {}".format(self.oras, "%.2f" % self.pret_total) 

######## CITIRE DATE ######## 
nr_concerte, pret_benz, consum = [float(x) for x in raw_input().split()]
nr_concerte = int(nr_concerte)

zi_inc, luna_inc, zi_sf, luna_sf = [int(x) for x in raw_input().split()] # perioada in care sunt plecat (concertul nu trebuie sa se afle intre aceste date)

lista = []
for i in range(nr_concerte):
    tmp = raw_input().split()
    oras = tmp[0]
    zi = int(tmp[1])
    luna = int(tmp[2])
    pret = int(tmp[3])
    distanta = int(tmp[4])
    
    #if luna_inc <= luna <= luna_sf and zi_inc <= zi <= zi_sf: --- NU MERGE ASA !!!!!!!!!
    ## DACA VREI SA VEZI DACA O DATA SE AFLA INTRE 2 DATE, TREBUIE SA LE CONVERTESTI IN TUPLURI SI SA FACI COMPARATIA ASTFEL:
    if (luna_inc, zi_inc) <= (luna, zi) <= (luna_sf, zi_sf):
        pass
    else:
        pret_total = pret + (2 * distanta * pret_benz * consum) / 3
        lista.append( Concert(oras, zi, luna, pret, distanta, pret_total) )

min = 99999.9
index = 0
for i in range(len(lista)):
    if lista[i].pret_total < min:
        min = lista[i].pret_total
        index = i
print(lista[index])

