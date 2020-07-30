nr_zaruri = int(raw_input())
fetze = [1, 2, 3, 4, 5, 6]
sum = 0

for i in range(nr_zaruri):
    fetze_zar = [int(x) for x in raw_input().split()]
    for j in fetze:
        if j not in fetze_zar:
            sum += j
            
print sum