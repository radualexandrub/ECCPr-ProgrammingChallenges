class Dreptunghi:
    def __init__(self, nume, x1, y1, x2, y2, arie):
        self.nume = nume
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.arie = arie

###### Citire  si prelucrare date ######
nr_dreptunghiuri = int(raw_input())
lista = []
for i in range(nr_dreptunghiuri):
    tmp = raw_input().split()
    
    nume, x1, y1, x2, y2 = tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3]), int(tmp[4])
    lat1 = x2 - x1
    lat2 = y2 - y1
    arie = lat1 * lat2
    
    lista.append( Dreptunghi(nume, x1, y1, x2, y2, arie) )

### Cautare max si stocare intr-un index ###
max = -1
i = 0
for j in range(len(lista)):
    if lista[j].arie > max:
        max = lista[j].arie
        i = j

print(lista[i].nume + " " + str(lista[i].x1) + " " + str(lista[i].y1) + " " + str(lista[i].x2) + " " + str(lista[i].y2) + " " + str(lista[i].arie))