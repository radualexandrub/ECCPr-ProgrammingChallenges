# n = nr_zaruri
n = int(input())
toate = [1, 2, 3, 4, 5, 6]
zaruri = []
for i in range(n):
	zaruri.append([int(x) for x in input().split()])
	
suma = 0
for i in range(len(zaruri)):
	for fatza in toate:
		if fatza not in zaruri[i]:
			suma += fatza

print(suma)