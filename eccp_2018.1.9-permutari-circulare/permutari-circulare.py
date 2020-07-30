import math

def permutari_circulare(N): 
    """ Function that return a generator of list with all cyclic permutations of a number."""
    
    num = N; 
    n = len(str(N))
    
    while (1): 
        yield int(num)
        
        # Generate a circular permutation of a number
        rem = num % 10
        div = math.floor(num / 10)
        num = ((math.pow(10, n - 1)) * rem + div)
         
        # If all the permutations are checked and we obtain original number exit from loop
        if (num == N):
            break

nr = int(raw_input())
nr = int(bin(nr)[2:])

max = -1
for perm in permutari_circulare(nr):
    if perm > max:
        max = perm
        
print(int(str(max), 2))



### Deci, mi-a picat 2 teste pentru ca:
# 1) NU POTI STOCA TOATE PERMUTARILE INTR-O LISTA DEOARECE NU EXISTA SUFICIENTA MEMORIE RAM (256MB LA DISPOZITIE)
# => SE BLOCHEAZA
# 2) Nu poti itera prin toate permutarile pentru ca dureaza prea mult timp si apare exceptie de time out

# Evident ca se intampla r*haturi de genul acesta daca la intrare se da un numar de 6 cifre care in binar are 20 cifre !!! (20! = 2,432,902,008,176,640,000)
# Cei care ati propus astfel de probleme pentru ECCP (si mai ales teste) ar fi bine sa va lasati de meserie.




# Test 6
# Program timeout
# Incorrect program output
# --- Input ---
# 98765

# --- Program output ---

# --- Expected output (numbers)---
# 118208




# Test 7
# Program timeout
# Incorrect program output
# --- Input ---
# 87381

# --- Program output ---

# --- Expected output (numbers)---
# 109226