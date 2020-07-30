# Citire date
nr_ingrediente = int(input())
stoc = [int(x) for x in input().split()]

nr_cereri = int(input())
comenzi = []
for i in range(nr_cereri):
	comenzi.append([int(x) for x in input().split()])

# Prelucrare date
nr_onorate = 0
nr_aproviz = 0
for i in range(nr_cereri):
	# Daca este aprovizionare
	if all(comenzi[i][j] == 0 for j in range(nr_ingrediente)):
		nr_aproviz += 1
		for j in range(nr_ingrediente):
			stoc[j] += 15

	# Daca cererea poate fi onorata:
	elif all(stoc[j] - comenzi[i][j] >= 0 for j in range(nr_ingrediente)):
		nr_onorate += 1
		for j in range(nr_ingrediente):
			stoc[j] -= comenzi[i][j]

print(nr_onorate)
print(nr_aproviz)

# In mod dubios mai intai trebuie verificat daca e aprovizionare si apoi daca 
# poti onora comanda... adica inversate if-urile exact in ordinea asta
# invers nu merge...

# AAAAA pentru ca altfel s-ar putea onora si comenzile care practic au ZERO LOL... 
# da are sens... conteaza ordinea in care verifici !!!!