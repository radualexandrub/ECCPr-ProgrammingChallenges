numar_lot = int(input())
lot_nr_comp = []
nr_utile = 0
max_comp = 0

for i in range(numar_lot):
    lot_nr = int(input())
    if lot_nr != 0:
        lot_nr_comp.append(lot_nr)
        lot_comp = input().split()
        nr_R = 0
        nr_C = 0
        nr_T = 0
        
        for j in range(len(lot_comp)):
            if lot_comp[j] == 'R':
                nr_R = nr_R + 1
            if lot_comp[j] == 'C':
                nr_C = nr_C + 1
            if lot_comp[j] == 'T':
                nr_T = nr_T + 1
                
        if max_comp < len(lot_comp):
                max_comp = len(lot_comp)
        
        if nr_C >= nr_T and nr_R >= nr_C and nr_T >= 1 and nr_C >=1 and nr_R >= 1:
            nr_utile = nr_utile + 1
            
print(nr_utile, max_comp)