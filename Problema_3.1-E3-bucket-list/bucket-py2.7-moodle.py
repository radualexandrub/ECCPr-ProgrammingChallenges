nr_numere = int(raw_input())
sir_nr = [int(i) for i in raw_input().split()]
contoare = [0 for i in range(19)]

for i in range(nr_numere):
    if sir_nr[i] >= 0 and sir_nr[i] <= 9:
        contoare[0] += 1
    elif sir_nr[i] >= 10 and sir_nr[i] <= 99:
        contoare[1] += 1
    elif sir_nr[i] >= 100 and sir_nr[i] <= 999:
        contoare[2] += 1
    elif sir_nr[i] >= 1000 and sir_nr[i] <= 9999:
        contoare[3] += 1
    elif sir_nr[i] >= 10000 and sir_nr[i] <= 99999:
        contoare[4] += 1
    elif sir_nr[i] >= 100000 and sir_nr[i] <= 999999:
        contoare[5] += 1
    elif sir_nr[i] >= 1000000 and sir_nr[i] <= 9999999:
        contoare[6] += 1
    elif sir_nr[i] >= 10000000 and sir_nr[i] <= 99999999:
        contoare[7] += 1
    elif sir_nr[i] >= 100000000 and sir_nr[i] <= 999999999:
        contoare[8] += 1
    elif sir_nr[i] >= 1000000000 and sir_nr[i] <= 9999999999:
        contoare[9] += 1
    elif sir_nr[i] >= 10000000000 and sir_nr[i] <= 99999999999:
        contoare[10] += 1
    elif sir_nr[i] >= 100000000000 and sir_nr[i] <= 999999999999:
        contoare[11] += 1
    elif sir_nr[i] >= 1000000000000 and sir_nr[i] <= 9999999999999:
        contoare[12] += 1
    elif sir_nr[i] >= 10000000000000 and sir_nr[i] <= 99999999999999:
        contoare[13] += 1
    elif sir_nr[i] >= 100000000000000 and sir_nr[i] <= 999999999999999:
        contoare[14] += 1
    elif sir_nr[i] >= 1000000000000000 and sir_nr[i] <= 9999999999999999:
        contoare[15] += 1
    elif sir_nr[i] >= 10000000000000000 and sir_nr[i] <= 99999999999999999:
        contoare[16] += 1
    elif sir_nr[i] >= 100000000000000000 and sir_nr[i] <= 99999999999999999:
        contoare[17] += 1
    else:
        contoare[18] += 1

if contoare[0] != 0:
    print(1, contoare[0])
if contoare[1] != 0:
    print(2, contoare[1])
if contoare[2] != 0:
    print(3, contoare[2])
if contoare[3] != 0:
    print(4, contoare[3])
if contoare[4] != 0:
    print(5, contoare[4])
if contoare[5] != 0:
    print(6, contoare[5])
if contoare[6] != 0:
    print(7, contoare[6])
if contoare[7] != 0:
    print(8, contoare[7])
if contoare[8] != 0:
    print(9, contoare[8])
if contoare[9] != 0:
    print(10, contoare[9])
if contoare[10] != 0:
    print(11, contoare[10])
if contoare[11] != 0:
    print(12, contoare[11])
if contoare[12] != 0:
    print(13, contoare[12])
if contoare[13] != 0:
    print(14, contoare[13])
if contoare[14] != 0:
    print(15, contoare[14])
if contoare[15] != 0:
    print(16, contoare[15])
if contoare[16] != 0:
    print(17, contoare[16])
if contoare[17] != 0:
    print(18, contoare[17])
if contoare[18] != 0:
    print(19, contoare[18])
