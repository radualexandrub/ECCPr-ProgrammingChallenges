nr_autobuze = [i for i in range(1, int(raw_input()) + 1)]
autobuze = [int(i) for i in raw_input().split()]
autobuze_lipsa = [i for i in nr_autobuze if i not in autobuze]
print(sum(autobuze_lipsa))
