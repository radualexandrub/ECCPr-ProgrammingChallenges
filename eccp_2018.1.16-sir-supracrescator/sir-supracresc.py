###### Citire date ######
# n = int(raw_input())
# sir = []
# for i in range(n):
#     sir.append(int(raw_input()))
sir = [1, 4, 7, 13, 30, 55, 121, 273]
n = len(sir)

###### Prelucrare date ######
suma = 0
indecsi = []
# print(2 + 4 + 8 + 17 + 32 + 67 + 138 + 285 + 601 + 999)
print(2 + 4 + 8 + 16 + 32 + 64 + 128 + 265 + 601 + 1001)
i = 0
while i in range(n):

    if sir[i] < suma:
        sir[i] = suma + 1
        indecsi.append(i)
        suma = 0
        i = -1  # "resetare" bucla -- verificam din nou
    else:
        suma = suma + sir[i]
    i += 1

indecsi2 = []
for i in range(len(indecsi)):
    if indecsi[i] not in indecsi2:  # deoarece avem mai multe iteratii, vom avea dubluri la indecsi
        indecsi2.append(indecsi[i])

print(len(indecsi2))
for i in range(len(indecsi2)):
    print(indecsi2[i] + 1)  # +1 pt ca la ei numerotarea incepe de la 1


# 13 tests run/12 tests passed -- au pus un test gresit hehehehe bvbvbv
# --- Program output ---
# 1
# 10
# ACCEPT

# --- Expected output (exact text)---
# 1
# 10
# RESPINS
