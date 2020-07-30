stiva = []
index = -1
nr_instr = int(raw_input())

for i in range(nr_instr):
    tmp = raw_input().split()
    if len(tmp) == 2: # iload <val>
        stiva.append(int(tmp[1]))
        
    elif tmp[0] == "iadd":
        if len(stiva) == 1:
            index = i + 1
        else:
            adunare = stiva[-1] + stiva[-2]
            stiva.pop()
            stiva[-1] = adunare
        
    elif tmp[0] == "imul":
        mul = stiva[-1] * stiva[-2]
        stiva.pop()
        stiva[-1] = mul
        
    elif tmp[0] == "dup":
        duplicat = stiva[-1]
        stiva.append(duplicat)
 
if index == -1:      
    print(len(stiva))          
    for i in range(len(stiva)-1, -1, -1):
        print(stiva[i])
else:
    print("Exception: line {}".format(index))
        
