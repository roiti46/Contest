p,q,l,r = map(int,raw_input().split())
ab = [map(int,raw_input().split()) for i in range(p)]
cd = [map(int,raw_input().split()) for i in range(q)]
ans = 0

zon = [0]*2002
for a,b in ab:
    zon[a:b+1] = [1]*(b-a+1)
for t in range(l,r+1):
    xon = [0]*1001
    for c,d in cd:
        xon[c+t:d+t+1] = [1]*(d-c+1)
    ans += min(1,sum([xon[i]*zon[i] for i in range(1001)]))

print ans
