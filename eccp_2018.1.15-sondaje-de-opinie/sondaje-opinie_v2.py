# P_partide = Nr de partide politice
# S_sondaje = nr de sondaje
# Urmatoarele P linii: Np = numele partidului, S = mai multe procente obtinute de partid la cele S sondaje

# ### Citire date si selectare partid care a avut ascendenta continua
nr_partide, nr_sondaje = [int(_) for _ in input().split()]

partide = []
partide_ascendente = []
for i in range(nr_partide):
	nume, *sondaje = [_ for _ in input().split()]
	sondaje = [int(_) for _ in sondaje]
	partide.append([nume, sondaje])

	# Verifica daca partidul a avut ascendenta continua si pune in noua lista
	if all(sondaje[i + 1] - sondaje[i] >= 0 for i in range(len(sondaje) - 1)):
		partide_ascendente.append(nume)

if len(partide_ascendente) > 0:
	print(*partide_ascendente)
else:
	print("Nu exista")

# ### Prelucrare date: Selectare partid care a castigat cel mai mult electorat
# adica are diferenta procent[0] - procent[ultim] maxima
maxim = 0
index = 0
for i in range(len(partide)):
	if partide[i][1][-1] - partide[i][1][0] >= maxim:
		maxim = partide[i][1][-1] - partide[i][1][0]
		index = i
print("{} {}%".format(partide[index][0], maxim))
