nr_biti = int(raw_input())
sir = raw_input()

aparitii = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #aparitii de 1bit, 2biti, 3biti, 4biti etc..
i = 0
max_count = -1
while i < nr_biti:
    count = 0
    if sir[i] == '1':
        count = 1
        j = i+1
        while j < nr_biti:
            if sir[j] == '1':
                count += 1
                j += 1
            else:
                break
        
    if count > max_count:
        max_count = count
        
    if count == 0:
        i += 1
    if count == 1:
        aparitii[0] += 1
        i += 1
    if count == 2:
        aparitii[1] += 1
        i += 2
    if count == 3:
        aparitii[2] += 1
        i += 3
    if count == 4:
        aparitii[3] += 1
        i += 4
    if count == 5:
        aparitii[4] += 1
        i += 5
    if count == 6:
        aparitii[5] += 1
        i += 6
    if count == 7:
        aparitii[6] += 1
        i += 7
    if count == 8:
        aparitii[7] += 1
        i += 8
    if count == 9:
        aparitii[8] += 1
        i += 9
    if count == 10:
        aparitii[9] += 1
        i += 10
    if count == 11:
        aparitii[10] += 1
        i += 11
    if count == 12:
        aparitii[11] += 1
        i += 12

s = ""
for i in range(max_count):
    if aparitii[i] != 0:
        s = s + str(aparitii[i]) + ' '
    else:
        s = s + '0' + ' '
print(s)

if aparitii[0] >= aparitii[1] >= aparitii[2] >= aparitii[3] >= aparitii[4] >= aparitii[5] >= aparitii[6] >= aparitii[7] >= aparitii[8] >= aparitii[9] >= aparitii[10] >= aparitii[11]:
    print(1)
else:
    print(0)
        