import re

def print_output(i, x):
    print "Case #%s: %s" % (i, x)

[L, D, N] = [int(n) for n in raw_input().split()]

words = []
for i in range(D):
    words.append(raw_input())

for i in range(1, N + 1):
    regex = raw_input().replace('(', '[').replace(')', ']')
    result = sum([1 for word in words if re.match(regex, word)])
    print_output(i, result)
