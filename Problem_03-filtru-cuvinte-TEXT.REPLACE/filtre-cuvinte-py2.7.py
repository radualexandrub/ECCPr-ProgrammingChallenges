text = raw_input()
nr_cuv = int(raw_input())
cuvinte = raw_input().split()

for i in cuvinte:
    if i in text:
        stelute = ''
        for j in range(len(i)):
            stelute = stelute + '*'
        text = text.replace(i, stelute)

print(text)