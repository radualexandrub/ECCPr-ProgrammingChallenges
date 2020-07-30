litere = sorted("0QWERTYUIOPASDFGHJKLZXCVBNM")
numere_2cifre = [str(x) for x in range(10,27)]
numere_1cifra = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
numere_1cifra_ = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

sir = raw_input()

i = 0
s = ""
while i in range(len(sir)):
    
    if i != len(sir)-1 and sir[i] + sir[i+1] in numere_2cifre:
        #print(litere[int(sir[i] + sir[i+1])])
        s = s + litere[int(sir[i] + sir[i+1])]
        i += 1
        
    elif i != len(sir)-1 and sir[i] + sir[i+1] in numere_1cifra:
        #print(litere[int(sir[i+1])])
        s = s + litere[int(sir[i+1])]
        i += 1
        
    elif sir[i] in numere_1cifra_:
        s = s + litere[int(sir[i])]
        
    elif i != len(sir)-1 and sir[i] + sir[i+1] == '00':
        #print(" ")
        s = s + " "
        i += 1
        
    i += 1

print(s)

# 26|7|15|13|15|20|00|01|12|02 
# Z |G|O |M |O |T |_ |A |L |B

# 19|5|3|18|5|20
# S |E|C|R |E|T