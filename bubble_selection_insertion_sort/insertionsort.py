




def insertionsort(l):
    for i in range(1, len(l)):
        pos = i
        while pos > 0 and l[pos] < l[pos - 1]:
            l[pos], l[pos - 1] = l[pos - 1], l[pos]
            pos = pos - 1


def insertionsort2(l):
    for i in range(1, len(l)):
        pos = i
        x = l[i]
        while pos > 0 and x < l[pos - 1]:
            l[pos] = l[pos - 1]
            pos = pos - 1
        if pos != i:
            l[pos] = x
