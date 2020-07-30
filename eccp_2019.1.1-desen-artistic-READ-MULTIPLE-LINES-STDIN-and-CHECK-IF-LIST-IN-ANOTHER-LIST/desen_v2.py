import sys

n = int(input())
culori = [x for x in input().split()]
lista = sys.stdin.read().splitlines()
lista = [x.split() for x in lista]

if 'red' in culori and 'blue' in culori and 'purple' not in culori:
	culori.append('purple')
if 'yellow' in culori and 'red' in culori and 'orange' not in culori:
	culori.append('orange')
if 'yellow' in culori and 'blue' in culori and 'green' not in culori:
	culori.append('green')
if 'yellow' in culori and 'red' in culori and 'blue' in culori and 'brown' not in culori:
	culori.append('brown')

for i in range(len(lista)):
	if all(x in culori for x in lista[i][2:]):
		print(lista[i][0])
