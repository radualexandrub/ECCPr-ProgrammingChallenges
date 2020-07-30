class Forma:
    def __init__(self, forma, lat, arie):
        self.forma = forma
        self.lat = lat
        self.arie = arie

############################
# CITIRE SI PRELUCARE DATE 
nr_forme = int(raw_input())
lista = []
for i in range(nr_forme):
    tmp = raw_input().split()
    if tmp[0] == "patrat":
        forma = tmp[0]
        lat = float(tmp[1])
        arie = round(lat**2, 2)
        lista.append( Forma(forma, lat, arie) )
    if tmp[0] == 'cerc':
        forma = tmp[0]
        lat = float(tmp[1])
        arie = round(3.14*(lat**2), 2)
        lista.append( Forma(forma, lat, arie) )
    if tmp[0] == "dreptunghi":
        forma = tmp[0]
        lat = [float(tmp[1]), float(tmp[2])]
        arie = round(lat[0]*lat[1], 2)
        lista.append( Forma(forma, lat, arie) )

max = -1
index = 0
for i in range(len(lista)):
    if lista[i].arie > max:
        max = lista[i].arie
        index = i

###########################################        
# AFISARE cu doua zecimale dupa virgula:
# Numarul poate fi de lungime variabila (poate fi 9.4 sau 99.4, care trebuie afisate ca 9.40, 99.40)
# Folosim la afisare:
# print(string_nume + " %.2f" % float_numar)
if lista[index].forma == "cerc" or lista[index].forma == "patrat":
        print(lista[index].forma + ' %.2f' % lista[index].lat)
elif lista[index].forma == "dreptunghi":
        print(lista[index].forma + ' %.2f' % lista[index].lat[0] + ' %.2f' % lista[index].lat[1])