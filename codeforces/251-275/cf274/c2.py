N = int(raw_input())
ab = sorted([map(int,raw_input().split()) for i in xrange(N)])
day = 0
for a,b in ab:
    if b >= day:
        day = b
    else:
        day = a
print day
