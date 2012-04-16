
def print_output(i, x):
    print "Case #%s: %s" % (i, " ".join(x))

def find(C, l, li):
    for i in range(l):
        for j in range(i+1, l):
            if li[i] + li[j] == C:
                return (i+1, j+1)
            

N = int(raw_input())

for i in range(1, N + 1):
    C = int(raw_input())
    l = int(raw_input())
    li = [int(n) for n in raw_input().split()]

    result = find(C, l, li)
    print_output(i, [str(x) for x in result])
