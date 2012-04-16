
N = int(raw_input())

for i in range(N):
    line = raw_input()
    print "Case #" + str(i+1) + ": " + " ".join(line.split()[::-1])
