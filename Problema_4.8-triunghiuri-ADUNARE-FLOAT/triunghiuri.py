import math
nr_triunghi = int(raw_input())

class Triunghi:
    def __init__(self, index, laturi, supr, arie, raport):
        self.index = index
        self.laturi = laturi
        self.supr = supr
        self.arie = arie
        self.raport = raport
        
lista = []
for i in range(nr_triunghi):
    latura = [float(x) for x in raw_input().split()]

    # este triunghi? (fiecare latura strict mai mica ca suma celorlalte doua)
    ### !!!! VEZI CA DACA ADUNI 4.4 + 4.7 VEI OBTINE 9.100000000000001 CARE ESTE MAI MARE CA 9.1 => SE RESPECTA CONDITIA STRICT MAI MICA 
    ###                                                                                 CEEA CE NU TREBUIA SA SE INTAMPLE !!!!
    ###                                                                                 REZOLVAM CU ROUND(x,1)
    if latura[0] < round(latura[1] + latura[2],1) and latura[1] < round(latura[0] + latura[2],1) and latura[2] < round(latura[1] + latura[0],1):
        
        # este isoscel? (isoscel = are doua laturi egale)
        if (latura[0] == latura[1] or latura[0]==latura[2] or latura[1]==latura[2]) == False:
            
            # este dreptunghic? (respecta Th. Pitagora)
            latura.sort(reverse = True)
            if (latura[0]**2 == latura[1]**2 + latura[2]**2) == False:
                
                ## Calculez suprafata triunghiului oarecare:
                s = latura[0]+latura[1]+latura[2]
                s2 = s / 2
                ## Calculez aria:
                arie = math.sqrt( s2*(s2-latura[0])*(s2-latura[1])*(s2-latura[2]))
                
                raport =  round(arie / s, 3)
                
                lista.append(Triunghi(i, latura, s, arie, raport))


# sortez dupa raport descrescator
lista.sort(key = lambda c: c.raport, reverse = True)
print(str(lista[0].index)+' '+str(lista[0].raport))

