#... problema e grea si cred ca m-am complicat atat de tare incat nici eu nu inteleg ce am facut.. desi am avut idei mijto dar ma mir ca mi-a reusit.
from math import sqrt

nr_planete = int(raw_input())
class Planeta:
    def __init__(self, x, y, z, vizitata, distanta):
        self.x = x
        self.y = y
        self.z = z
        self.vizitata = vizitata
        self.distanta = distanta

###############################################################################################################
##### Citire date (in loc de lista de liste de coordonate, facem o lista de obiecte care contin coordonatele)
lista = []
for i in range(nr_planete):
    temp = [int(x) for x in raw_input().split()]
    lista.append(Planeta(temp[0], temp[1], temp[2], False, 0.0))

# Pe ultima linie se afla coordonatele pozitiei de start a navei
temp = [int(x) for x in raw_input().split()]
nava_start = Planeta(temp[0], temp[1], temp[2], False, 0.0) # tratez pozitia navei (care se va schimba mereu) ca pe un obiect separat

#######################
##### Prelucrare date:
distanta_totala = 0.0

def recalculare_dist(lista):
    """ O data ce ne vom deplasa cu nava pe o planeta, va trebui sa recalculam toate distantele 
        astfel incat sa alegem sa ne deplasam pe urmatoarea planeta care se afla la distanta cea mai mica.
        
        apelarea functiei se face astfel:
        recalculare_dist(lista) """
    for i in range(len(lista)):
        if lista[i].vizitata == False:
            dist1 = sqrt( (nava_start.x-lista[i].x)**2 + (nava_start.y-lista[i].y)**2 + (nava_start.z-lista[i].z)**2 )
            lista[i].distanta = dist1

# recalculare_dist(lista)
# for i in range(len(lista)):
#     print(lista[i].distanta)

for i in range(nr_planete):
    recalculare_dist(lista)
    
    #### verificam daca toate planetele sunt la distanta egala.. CHECK IF ALL ELEMENTS IN A LIST ARE THE SAME -> all(...):
    #### Daca sunt la distante egale, ne deplasam la prima planeta
    # (pentru a ne deplasa la prima planeta, parcurgem iar toate planetele si NE OPRIM/BREAK la prima planeta NEvizitata)
    # Dupa ce am parcurs o planeta, vom schimba "vizitata" = True 
    # (astfel incat sa nu ne mai complicam sa facem de fiecare data alta lista care sa nu contina aceea planeta ..)
    if all(lista[i].distanta == lista[0].distanta for i in range(len(lista)) if lista[i].vizitata == False):
        for j in range(nr_planete):
            if lista[j].vizitata == False:
                nava_start.x, nava_start.y, nava_start.z = lista[j].x, lista[j].y, lista[j].z
                lista[j].vizitata = True
                distanta_totala += lista[j].distanta
                break
    
    #### Altfel, daca distantele nu sunt egale, calculam distanta minima din locul unde ne aflam si ne deplasam catre acea planeta
    # (distanta minima o aflam parcurgand din nou planetele NEvizitate si comparand/atribuind minime)
    else:
        index = 0
        min = 9999
        for j in range(nr_planete):
            if lista[j].distanta < min and lista[j].vizitata == False:
                min = lista[j].distanta
                index = j
        
        nava_start.x, nava_start.y, nava_start.z = lista[index].x, lista[index].y, lista[index].z
        lista[index].vizitata = True
        distanta_totala += lista[index].distanta

#############################################################################################################
###### AFISARE: astia iar cer afisare de doua zecimale chiar daca avem numar intreg (ex: 9.00 SAU CHIAR 9.10)      
# z = str((round(distanta_totala, 2)))
# if z[-1] == '0':
#     z = z+'0' # 9.0 devine 9.00
# elif z[-1] !='0' and len(z) == 4:
#     z = z+'0' # 9.1 devine 9.10
# print(z)
# ~~~~ ups, aia e metoda veche de afisare, mai bine asa:
print("{:.2f}".format(distanta_totala))










        