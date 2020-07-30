###### CITIRE DATE ######
# D = dimensiunea rafturilor exprimata in numar pagini
# k = numar de seturi de carti cu dimensiuni diferite gen => fiecare din cele 'k' seturi carti are 'n' carti cu 'p' pagini
D, k = [int(x) for x in raw_input().split()]

lista_carti = []
for i in range(k):
    n, p = [int(x) for x in raw_input().split()]
    while n != 0:
        lista_carti.append(p) # Aici am desfasurat toate seturile cu 'n' carti intr-o singura lista (e inutil sa ma complic cu liste de liste)
        n -= 1

###### PRELUCRARE DATE ######
for i in range(len(lista_carti)):
    D_raft = D
    s = "" # Fiecare raft va fi un string pe care il printez direct dupa ce completez raftul
            # Parcurg lista asta cu carti pana cand toate elementele din lista vor fi zero (asta inseamna ca lista e 'epuizata'/are toate elementele sterse)
            # E mult mai greu sa stergi elemente din lista in timp ce iterezi spre deosebire de a inlocui cu zero si sa ignori elementul daca e zero la urmatorea iteratie
    
    # Parcurg din nou lista pana cand raftul e plin (sau nu mai incape nicio carte cu 'p' pagini in el),
    # ma asigur ca, cartea din lista a fost 'epuizata'/stearsa din lista (inlocuita cu zero) si ca dimensiunea ei e mai mica ca dimensiunea raftului (mereu actualizata)
    for j in range(len(lista_carti)):
        if D_raft > 0 and lista_carti[j] != 0 and lista_carti[j] <= D_raft:
                s = s + str(lista_carti[j]) + ' '
                D_raft -= lista_carti[j]
                lista_carti[j] = 0
    print(s)

# Acel moment cand iti vine o idee la panarama, scrii dintr-o data tot codul fara sa testezi absolut nimic pe parcurs, 
# si la prima verificare iti ia toate testele din prima... LOL I'm so cool. (ma jur ca dupa maxim 1 zi nu mai stiu ce am facut aici
# deci ia sa scriu mai bine niste comentarii)
