## probleme la afisare => 2 teste nu sunt trecute ..

nr_linii = int(raw_input())

sir = []
for y in range(nr_linii):
    date = [int(i) for i in raw_input().split(',')]
    #### cod pentru o singura linie ###
    sir_linie = []
    sir_tuplu = []
    contor_zero = 0
    for i in range(len(date)-1):
        contor_zero = 0
        sir_tuplu = []
        
        if date[i] != 0 and date[i+1] != 0:
            sir_linie.append(date[i])
        if date[i] != 0 and date[i+1] == 0:
            # numar zerourile dupa
            for j in range(i+1,len(date)):
                if date[j] == 0:
                    contor_zero += 1
                else:
                    break
            sir_tuplu = [date[i], contor_zero]
            sir_linie.append(sir_tuplu)
    if date[-1] != 0:
        sir_linie.append(date[-1])
    sir.append(sir_linie)
    #### cod pentru o singura linie ###
    
# print(sir) #lista care contine liste care contina lista(de 2 elemente: nr si nr_zerouri dupa)
# printam lista de liste cu lista pe rand separat
# print(sir)
for i in range(len(sir)):
    s = ""
    for j in range(len(sir[i])):
        ### Verificare ultim element pentru a pune sau nu virgula
        if sir[i][j] != sir[i][-1]:
            s1 = ""
            if isinstance(sir[i][j], list):
                s1 = '('+str(sir[i][j][0])+','+str(sir[i][j][1])+')'
            else:
                s1 = str(sir[i][j])
            s = s + s1 + ","
        
        ### Verificare ultim element pentru a pune sau nu virgula else 
        else:
            s1 = ""
            if isinstance(sir[i][j], list):
                s1 = '('+str(sir[i][j][0])+','+str(sir[i][j][1])+')'
            else:
                s1 = str(sir[i][j])
            s = s + s1
    print(s)

    






















