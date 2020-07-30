# PS = Putere Scut, PF = Putere Faza
# !!! Atentie, nava proprie/inamica inca supravietuieste si POATE SA ATACE chiar daca are viatza scutului == 0 in acel moment.
class Nava:
    def __init__(self, PS, PF):
        self.PS = PS
        self.PF = PF

##### CITIRE DATE #################################
PS_propriu, PF_propriu = [int(x) for x in raw_input().split()]
nava_proprie = Nava(PS_propriu, PF_propriu)

nr_nave_inamice = int(raw_input())
nave_inamice = []
for i in range(nr_nave_inamice):
    citire_temp = [int(x) for x in raw_input().split()]
    nave_inamice.append( Nava(citire_temp[0], citire_temp[1]) )
    
#### (OPTIONAL) Afisare continut lista si restul datelor ###
# print("Nava proprie", "scut: ", nava_proprie.PS, "faza: ", nava_proprie.PF)
# print("Nr. nave inamice: ", nr_nave_inamice)
# print("Nave inamice: ")
# for i in range(nr_nave_inamice):
#     print(nave_inamice[i].PS, nave_inamice[i].PF)

### PRELUCRARE DATE ##############################
contor_win = 0

for i in range(nr_nave_inamice):
    
    while nave_inamice[i].PS >= 0 and nava_proprie.PS >= 0:
        if nave_inamice[i].PS >= 0:
            nava_proprie.PS = nava_proprie.PS - nave_inamice[i].PF
        if nava_proprie.PS >= 0:
            nave_inamice[i].PS = nave_inamice[i].PS - nava_proprie.PF
        
    #print("iesit din bucla")
    
    if nave_inamice[i].PS < 0 and nava_proprie.PS >= 0:
        contor_win += 1

    #resetare viata lol - respawn:
    nava_proprie.PS = PS_propriu

print(contor_win)


