# n = nr_emotii detectate
n = int(input())

emotii = []
for i in range(n):
	x = input().split()
	emotii.append([x[0], int(x[1])])

mancaruri = []
for i in range(n):
	x = input().split()
	mancaruri.append([x[0], x[1], x[2]])

print(emotii)
print(mancaruri)
