def print_output(i, x):
    print "Case #%s: %s" % (i, x)

def find2(l, a, b):
    a.sort()
    b.sort()
    return sum([x*y for x,y in zip(a,b[::-1])])

N = int(raw_input())

for i in range(1, N + 1):
    l = int(raw_input())
    a = [int(n) for n in raw_input().split()]
    b = [int(n) for n in raw_input().split()]

    result = find2(l, a, b)
    print_output(i, result)
