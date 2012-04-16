from itertools import combinations

def print_output(i, x):
    print "Case #%s: %s" % (i, x)

def find(N, M, a, b):
    # construct trie
    d = {}
    for folder in a:
        temp = d
        for f in folder.strip('/').split('/'):
            if not temp.has_key(f):
                temp[f] = {}
            temp = temp[f]

    result = 0
    for folder in b:
        temp = d
        for f in folder.strip('/').split('/'):
            if not temp.has_key(f):
                result += 1
                temp[f] = {}
            temp = temp[f]
    return result

T = int(raw_input())

for i in range(1, T + 1):
    [N, M] = [int(x) for x in raw_input().split()]
    a,b = [], []
    for j in range(N):
        a.append(raw_input())
    for j in range(M):
        b.append(raw_input())
    result = find(N, M, a, b)
    print_output(i, result)
