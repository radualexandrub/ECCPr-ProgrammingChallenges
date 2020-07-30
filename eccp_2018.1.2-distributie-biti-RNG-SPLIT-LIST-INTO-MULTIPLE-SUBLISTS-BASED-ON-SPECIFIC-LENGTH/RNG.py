# n = nr biti generati
n = int(raw_input())
biti = raw_input()

lista = []
for i in range(0, n, 2):
    lista.append(biti[i:i+2]) ## impartim lista in subliste de cate 2 biti

#### PRELUCRARE DATE ####
#### RAPORT 1
contor = [0, 0, 0, 0] # pentru '00', '01', '10', '11'
for i in range(len(lista)):
    if lista[i] == '00':
        contor[0] += 1
    elif lista[i] == '01':
        contor[1] += 1
    elif lista[i] == '10':
        contor[2] += 1
    elif lista[i] == '11':
        contor[3] += 1

raport1 = round(float(max(contor)) / min(contor), 2)

#### RAPORT 2
contor_biti = [0, 0] # pentru biti de '0' sau '1'
for i in range(n):
    if biti[i] == '0':
        contor_biti[0] += 1
    elif biti[i] == '1':
        contor_biti[1] += 1

raport2 =  round(float(max(contor_biti)) / min(contor_biti), 2)

#### AFISARE ####
print("{:.2f}".format(raport1) + " " + "{:.2f}".format(raport2))

if raport1 <= 1.1 and raport2 <= 1.1:
    print(1)
else:
    print(0)