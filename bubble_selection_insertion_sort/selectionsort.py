



def selectionsort(l):
    for i in range(0, len(l) - 1):
        pos = i
        for j in range(i + 1, len(l)):
            if l[pos] > l[j]:
                pos = j
        if pos != i:
            l[i], l[pos] = l[pos], l[i]
