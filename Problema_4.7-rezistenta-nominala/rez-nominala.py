import math

# S = suma(R[i] - medie_R)^2 = suma(R[i]^2 - 2*R[i]*medie_R + medie_R^2) = suma1(R[i]^2) - suma2(2*R[i]*medie_R) + suma3(medie_R^2)
nr_rez = int(raw_input())
lista_rez = [float(i) for i in raw_input().split()]

medie_R = sum(lista_rez) / float(nr_rez)
suma1, suma2, suma3 = 0, 0, 0

for i in range(nr_rez):
    suma1 = suma1 + lista_rez[i]**2
    suma2 = suma2 + 2*lista_rez[i]*medie_R
suma3 = nr_rez*medie_R**2

S = math.sqrt((suma1 - suma2 + suma3)/nr_rez)

count = 0
for i in range(nr_rez):
    if medie_R-S <= lista_rez[i] <= medie_R+S:
        count += 1
        
procent = round(float(count)/nr_rez * 100, 2) # limitare la 2 decimale dupa virgula
# ## daca numarul este intreg, 'facem in asa fel' sa afisam doua zerouri dupa virgula:
# if str(procent)[-1] == '0':
#     procent = str(procent) + '0'
# print(procent)

### ~~~ sau folosim:
print("{:.2f}".format(procent))
    