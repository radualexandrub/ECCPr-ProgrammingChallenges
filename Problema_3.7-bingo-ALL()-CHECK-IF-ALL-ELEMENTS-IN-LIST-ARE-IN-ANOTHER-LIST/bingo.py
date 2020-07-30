_, _ = [int(x) for x in raw_input().split()] #nu avem nevoie de dimensiunea "matricii" si nici de numarul de numere strigate #pythonic
numere_bunica = [int(x) for x in raw_input().split()]
numere_strigate = [int(x) for x in raw_input().split()]

count = 0
if all(x in numere_strigate for x in numere_bunica):
    print("BINGO!")
else: 
    for x in numere_bunica:
        if x not in numere_strigate:
            count += 1
    print(count)