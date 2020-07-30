class Film:
    def __init__(self, minute, pret, nume):
        self.minute = minute
        self.pret = pret
        self.nume = nume

    def __repr__(self):
        return "{}".format(self.nume)


###### CITIRE DATE & PRELUCRARE DATE ######
tmp = [int(x) for x in raw_input().split(':')]
# vom transforma orele:minutele in minute adunate pt a fi mai usor
minute_sosire = tmp[0] * 60 + tmp[1]

nr_filme = int(raw_input())

lista = []
# in timp ce citim filmele, vom cauta ora (minima) la care incepe filmul imediat dupa ce am ajuns la cinema
minim = 9999
for i in range(nr_filme):
    tmp = raw_input().split()
    tmp[0] = tmp[0].split(':')
    minute = int(tmp[0][0]) * 60 + int(tmp[0][1])
    pret = int(tmp[1])
    nume = tmp[2]

    if minute_sosire < minute:
        lista.append(Film(minute, pret, nume))
        if minute < minim:
            minim = minute

# dupa ce am obtinut ora minima (filmul care incepe cel mai devreme), vom pune intr-o lista separata toate filmele care incep la aceea ora
lista2 = []
for i in range(len(lista)):
    if lista[i].minute == minim:
        lista2.append(lista[i])

minim_pret = 9999  # daca sunt mai multe filme care incep la aceeasi ora minima, vom alege filmul cu cel mai mic pret
index = 0
for i in range(len(lista2)):
    if lista2[i].pret < minim_pret:
        minim_pret = lista2[i].pret
        index = i

print(lista2[index])
