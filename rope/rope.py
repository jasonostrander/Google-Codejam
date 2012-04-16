from itertools import combinations

def print_output(i, x):
    print "Case #%s: %s" % (i, x)

T = int(raw_input())

for i in range(1, T + 1):
    N = int(raw_input())
    wires = []
    for j in range(N):
        wires.append([int(x) for x in raw_input().split()])
    
    result = 0
    for x,y in combinations(wires, 2):
        if (x[0] > y[0] and x[1] < y[1]) or (x[0] < y[0] and x[1] > y[1]):
            result += 1
    print_output(i, result)
