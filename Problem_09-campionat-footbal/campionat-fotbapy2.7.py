class Echipa:
    def __init__(self, nume, puncte, gol_inscris, gol_primit):
        self.nume = nume
        self.puncte = puncte
        self.gol_inscris = gol_inscris
        self.gol_primit = gol_primit

nr_echipe = int(raw_input())
nr_meciuri = int(raw_input())

echipe = []
input = []
for i in range(nr_meciuri):
    string = raw_input().split()
    input.append(string)
    if string[0] not in echipe:
        echipe.append(string[0])
    if string[4] not in echipe:
        echipe.append(string[4])

echipe_obj = []
for i in range(len(echipe)):
    echipe_obj.append(Echipa(echipe[i],0,0,0))
    
###################################################################################################
# (doar pentru verificare)
# Pentru a cauta daca numele unui obiect se afla intr-o lista de obiecte, vom folosi functia any()  
# Functia any care returneaza True daca numele/cifra/orice se afla intr-o lista
#
# print( any(i for i in echipe_obj if i.nume == "Romania") ) => va returna True in acest caz
# print( any(i for i in echipe_obj if i.nume == "Rdsadaaz") ) => va returna False in acest caz

###################################################################################################
# Totodata, pentru a sti carui obiect echipa ii adaugam scorul, iar echipele fiind intr-o lista,
# avem nevoie ca, o data ce am identificat obiectul in lista de echipe, sa aflam indexul echipei din lista
# => 
# Finding the index of an item given a list containing it
#
# for index, obj in enumerate(['foo', 'bar', 'baz']):
#     if obj == 'bar':
#         print(index)
# sau
#
# [i for i, j in enumerate(['foo', 'bar', 'baz']) if j == 'bar']


for i in range(len(input)):
    ## caz 1: Meci egal ##
    if int(input[i][1]) == int(input[i][3]):
        for index, obj in enumerate(echipe_obj):
            if obj.nume == input[i][0]:
                obj.puncte += 1
                obj.gol_inscris += int(input[i][1])
                obj.gol_primit += int(input[i][3])
            if obj.nume == input[i][4]:
                obj.puncte += 1
                obj.gol_inscris += int(input[i][3])
                obj.gol_primit += int(input[i][1])
                
    ## caz 2: Meci echipa1 > echipa2 ##
    if int(input[i][1]) > int(input[i][3]):
        for index, obj in enumerate(echipe_obj):
            if obj.nume == input[i][0]:
                obj.puncte += 3
                obj.gol_inscris += int(input[i][1])
                obj.gol_primit += int(input[i][3])
            if obj.nume == input[i][4]:
                obj.puncte += 0
                obj.gol_inscris += int(input[i][3])
                obj.gol_primit += int(input[i][1])

    ## caz 3: Meci echipa1 < echipa2 ##
    if int(input[i][1]) < int(input[i][3]):
        for index, obj in enumerate(echipe_obj):
            if obj.nume == input[i][0]:
                obj.puncte += 0
                obj.gol_inscris += int(input[i][1])
                obj.gol_primit += int(input[i][3])
            if obj.nume == input[i][4]:
                obj.puncte += 3
                obj.gol_inscris += int(input[i][3])
                obj.gol_primit += int(input[i][1])
                
### Sortare echipe dupa scor
echipe_obj.sort(key = lambda c: c.puncte, reverse = True)

### Afisare echipe
for i in range(len(echipe_obj)):
    print(str(echipe_obj[i].nume)+' '+str(echipe_obj[i].puncte)+' '+str(echipe_obj[i].gol_inscris)+' '+str(echipe_obj[i].gol_primit))

