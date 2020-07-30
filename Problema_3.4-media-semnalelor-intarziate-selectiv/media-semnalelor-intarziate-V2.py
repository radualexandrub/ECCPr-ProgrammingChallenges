### CITIRE DATE
nr_microfoane = int(raw_input())
lista_orig = []
for i in range(nr_microfoane):
    tmp = [int(x) for x in raw_input().split()]
    lista_orig.append(tmp)

##############################################################    
### PRIMA MEDIERE: D1 = D2 = D3 = 0
lista_med_total = []
lista_med = []
for i in range(10):
    tmp = 0.0
    for j in range(nr_microfoane):
        tmp = tmp + lista_orig[j][i]
    tmp = round(tmp / nr_microfoane, 2)
    lista_med.append(tmp)

lista_med_total.append(lista_med)

##############################################################
### A DOUA MEDIERE: D1 = 0, D2 = 1, D3 = 2[, D4 = 3, D5 = 4]
lista_med = []
lista_intarziat = []
# intarziem primul semnal
lista_intarziat.append(lista_orig[0])
# intarziem al doilea semnal
tmp = [0]
for i in range(len(lista_orig[1])-1):
    tmp.append(lista_orig[1][i])
lista_intarziat.append(tmp)

if nr_microfoane >= 3:
    # intarziem al treilea semnal
    tmp = [0, 0]
    for i in range(len(lista_orig[2])-2):
        tmp.append(lista_orig[2][i])
    lista_intarziat.append(tmp)
    
if nr_microfoane >= 4:
    # intarziem al patrulea semnal
    tmp = [0, 0, 0]
    for i in range(len(lista_orig[3])-3):
        tmp.append(lista_orig[3][i])
    lista_intarziat.append(tmp)

if nr_microfoane >= 5:
    # intarziem al 5-lea semnal
    tmp = [0, 0, 0, 0]
    for i in range(len(lista_orig[3])-4):
        tmp.append(lista_orig[4][i])
    lista_intarziat.append(tmp)


# calculam media semnalelor:
for i in range(10):
    tmp = 0.0
    for j in range(nr_microfoane):
        tmp = tmp + lista_intarziat[j][i]
    tmp = round(tmp / nr_microfoane, 2)
    lista_med.append(tmp)

lista_med_total.append(lista_med)


##############################################################
### A TREIA MEDIERE: D1 = 0, D2 = 2, D3 = 4[, D4 = 6, D5 = 8]
lista_med = []
lista_intarziat = []
# intarziem primul semnal
lista_intarziat.append(lista_orig[0])

# intarziem al doilea semnal
tmp = [0, 0]
for i in range(len(lista_orig[1])-2):
    tmp.append(lista_orig[1][i])
lista_intarziat.append(tmp)

if nr_microfoane >= 3:
    # intarziem al treilea semnal D3 = 4
    tmp = [0, 0, 0, 0]
    for i in range(len(lista_orig[2])-4):
        tmp.append(lista_orig[2][i])
    lista_intarziat.append(tmp)
    
if nr_microfoane >= 4:
    # intarziem al patrulea semnal D4 = 6
    tmp = [0, 0, 0, 0, 0, 0]
    for i in range(len(lista_orig[3])-6):
        tmp.append(lista_orig[3][i])
    lista_intarziat.append(tmp)

if nr_microfoane >= 5:
    # intarziem al 5-lea semnal D5 = 9
    tmp = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(lista_orig[4])-8):
        tmp.append(lista_orig[4][i])
    lista_intarziat.append(tmp)
    
# calculam media semnalelor:
for i in range(10):
    tmp = 0.0
    for j in range(nr_microfoane):
        tmp = tmp + lista_intarziat[j][i]
    tmp = round(tmp / nr_microfoane, 2)
    lista_med.append(tmp)

lista_med_total.append(lista_med)

#########################################################
##### AFISARE:
for i in range(len(lista_med_total)):
    s = ""
    for j in range(len(lista_med_total[i])):
        s = s + "%.2f" % lista_med_total[i][j] + " "
    print(s)