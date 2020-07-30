class Partid:
	def __init__(self, nume, sondaje, evolutie, castig):
		self.nume = nume
		self.sondaje = sondaje
		self.evolutie = evolutie
		self.castig = castig


# ##### CITIRE SI PRELUCRARE DATE ######
nr_partide, nr_sondaje = [int(x) for x in raw_input().split()]
lista = []
for i in range(nr_partide):
	tmp = raw_input().split()

	nume = tmp[0]
	sondaje = []
	evolutie = True
	for j in range(1, nr_sondaje + 1):
		sondaje.append(int(tmp[j]))

	for j in range(len(sondaje)):
		if j != 0 and sondaje[j] < sondaje[j - 1]:
			evolutie = False
	castig = sondaje[-1] - sondaje[0]

	lista.append(Partid(nume, sondaje, evolutie, castig))

# ##### AFISARE DATE ######
# pe prima linie: partidele care au avut evolutie succesiva
s = ""
if all(x.evolutie is False for x in lista):
	print("Nu exista")
else:
	for partid in lista:
		if partid.evolutie is True:
			s = s + partid.nume + " "
print(s)

# pe a doua linie: partidul care a castigat cel mai mult electorat
max = 0
index = 0
for i, partid in enumerate(lista):
	if partid.castig > max:
		index = i
		max = partid.castig
print(lista[index].nume + " " + str(lista[index].castig) + "%")


# Afisare lista cu partide:
# for i in range(nr_partide):
#     print(lista[i].nume, lista[i].sondaje, lista[i].evolutie, lista[i].castig)
