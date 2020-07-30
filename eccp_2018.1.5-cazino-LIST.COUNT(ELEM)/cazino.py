class Carte:
    def __init__(self, nr, semn, aparitii):
        self.nr = nr
        self.semn = semn
        self.aparitii = aparitii
    def __repr__(self):
        return "{} {}".format(self.nr, self.semn)

#### CITIRE DATE ####
n = int(raw_input())
lista = []
for i in range(n):
    tmp = raw_input().split()
    lista.append( Carte(int(tmp[0]), tmp[1], 0) )

#### PRELUCRARE DATE ####
lista_aparitii = []
index = 0
for i in range(len(lista)):
    if (lista[i].nr, lista[i].semn) not in ((x.nr, x.semn) for x in lista_aparitii): # Daca cartea nu se afla in lista noua cu carti, adaug-o
        lista_aparitii.append(lista[i])
else:                                                   # Altfel, daca cartea exista in noua lista (lista care nu va avea repetitii),
    index2 = 0                                          # Cauta cartea respectiva in noua lista (gaseste-i indexul),
        for j in range(len(lista_aparitii)):            # si o data ce am gasit-o, incrementeaza-i numarul de aparitii
            if (lista[i].nr, lista[i].semn) == (lista_aparitii[j].nr, lista_aparitii[j].semn):
                index2 = j
                break
        lista_aparitii[index2].aparitii += 1
        
        if lista_aparitii[index2].aparitii == 2:        # Daca cartea respectiva deja are un numar de de 2 (3 aparitii dar numaratoarea incepe de la 0)  
            break                                       # Atunci opreste-te din cautat carti care se repeta...

#### AFISARE ####
index3 = -1                                             # Cautam in lista noua de carti(fara repetitii) o carte care sa aiba nr de aparitii == 2
for i in range(len(lista_aparitii)):                    # Daca exista, printeaz-o (functia __repr__ din interiorul clasei face printarea in formatul respectiv)
    if lista_aparitii[i].aparitii == 2:                 # Daca nu exista, indexul a ramas neschimbat (-1) si printeaza "JOC OK"
        index3 = i
if index3 != -1:
    print(lista_aparitii[index3])
else:
    print("JOC OK")

