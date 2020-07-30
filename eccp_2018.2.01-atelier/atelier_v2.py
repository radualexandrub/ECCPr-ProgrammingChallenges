# carcasă, tastatură, placă de bază, ecran, procesor, memorie și SSD
# Pentru ca un laptop să funcționeze corect, trebuie să aibă câte una din fiecare din componente
# n = nr_laptopuri

# Citire date
stoc = [int(_) for _ in input().split()]
n = int(input())
laptops = []
for _ in range(n):
	x = [int(_) for _ in input().split()]
	laptops.append(x)

# Prelucrare date
nr_reparate = 0
for i in range(len(laptops)):
	# Daca laptopul e deja functional
	if all(x == 1 for x in laptops[i]):
		nr_reparate += 1

	# Daca laptopul nu se poate repara (nu exista stoc pt a repara)
	elif any(laptops[i][j] == 0 and stoc[j] == 0 for j in range(len(stoc))):
		# Dezmembrez laptop si adun orice componenta 1 a lui la stoc:
		for j in range(len(stoc)):
			if laptops[i][j] == 1:
				stoc[j] += 1

	# Daca laptopul se poate repara (avem in stoc componentele respective)
	elif any(laptops[i][j] == 0 and stoc[j] > 0 for j in range(len(stoc))):
		for j in range(len(stoc)):
			if laptops[i][j] == 0:
				laptops[i][j] += 1
				stoc[j] -= 1
		nr_reparate += 1

print(nr_reparate)
