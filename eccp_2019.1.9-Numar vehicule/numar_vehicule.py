# Problema: Obtinere Indecsi Elem-din-alta-lista-bazata-pe-elem-comune-la-distante-diferite. Ex:

# n = nr_esantioane
# s1 s2 = senzor stanga dreapta, fiecare contine amprenta timp si 1/0 daca s-a activat sau nu

# Citire date
n = int(input())
s1 = []
s2 = []

s1x = ''
s2x = ''
for i in range(n):
	tmp = [int(_) for _ in input().split()]
	s1.append([tmp[0], tmp[1]])
	s1x += str(tmp[1])
for i in range(n):
	tmp = [int(_) for _ in input().split()]
	s2.append([tmp[0], tmp[1]])
	s2x += str(tmp[1])

# print(s1x)
# print(s2x)

# Prelucrare date
# Cautam primul index de 1 in fiecare din cele 2 liste
indecsi1 = []
indecsi2 = []

nr_vehicule = 0

i = 0
i2 = 1
while i in range(len(s1x)):
	if s1x[i] == '1':
		indecsi1.append(i)

		# Cat de lunga e secv de 1 gasita? (trb sa sar dupa cu contorul)
		j = i + 1
		lung = 1
		while j < len(s1x) and s1x[j] == '1':
			lung += 1
			j += 1

		# Cauta in sir2 secventa de 1 de aceeasi lungime lung
		# O sa restrang cautarea doar la o zona de aceeasi lungime lung
		de_cautat = lung * '1'
		j = i2
		while j in range(len(s2x)):
			if de_cautat in s2x[j:j + lung]:
				indecsi2.append(j)
				i2 = j + lung
				break
			else:
				j += 1

		i += lung
		nr_vehicule += 1
	else:
		i += 1

# print(indecsi1)
# print(indecsi2)

# Avand indecsii la dispozitie, putem calcula fiecare viteza in parte
viteze = []
for i in range(len(indecsi1)):
	vit = (1 / ((s1[indecsi1[i]][0] - s2[indecsi2[i]][0]) * 0.001)
		   ) * 3.6  # m/s -> km/h

	viteze.append(abs(vit))
medie = int(round(sum(viteze) / len(viteze)))

# print(viteze)

print(medie, nr_vehicule)
