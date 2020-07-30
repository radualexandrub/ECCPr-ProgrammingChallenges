stoc_componente = [int(x) for x in raw_input().split()]

nr_laptops = int(raw_input())

class laptop:
    componente = []

    def __init__(obj, componente):
        obj.componente = componente


# ########## CITIRE DATE #####################
obj_laptops = []
for i in range(nr_laptops):
    componenteX = raw_input().split()
    for j in range(7):
        componenteX[j] = int(componenteX[j])
    obj_laptops.append(laptop(componenteX))

# ########## PRELUCRARE DATE #####################
nr_laptop_reparate = 0

for i in range(nr_laptops):
    # verificare reparabil (pt fiecare laptop)
    reparabil = True
    for j in range(7):
        if obj_laptops[i].componente[j] == 0 and stoc_componente[j] == 0:
            reparabil = False

    if reparabil is False:
        # dezasamblez laptop
        for j in range(7):
            if obj_laptops[i].componente[j] == 1:
                stoc_componente[j] += 1
    else:
        for j in range(7):
            if obj_laptops[i].componente[j] == 0:
                stoc_componente[j] -= 1
                obj_laptops[i].componente[j] = 1
        nr_laptop_reparate += 1


# print("reparabil? ", reparabil)
# print("nr laptops reparate: ", nr_laptop_reparate)
print(nr_laptop_reparate)

# verificam mai intai daca laptopul e reparabil:
# LAPTOPUL ESTE REPARABIL DACA: PENTRU FIECARE COMPONENTA DEFECTA A LAPTOPULUI, EXISTA COMPONENTA RESPECTIVA IN STOC =>
#                   => atunci cand intalnim o componenta defecta a laptoplui care nu e in stoc => reparabil = False
#
# - daca laptop nu este reparabil -> dezasamblam laptop => schimbam val componente in 0? (opt) -> crestem stocul cu componentele respective
# - daca laptop este reparabil -> (OPTIONAL:schimbam valorile componentelor din zero in 1) -> scadem din stoc componentele respective
#                   => incrementam nr_laptops_repate


# ~ Afisare stoc ~
# print(stoc_componente)
# ~ Afisare laptops ~
# for i in range(nr_laptops):
#    print(obj_laptops[i].componente)
