n,k,x = map(int,raw_input().split())
C = map(int,raw_input().split())
sps = []
for i in range(n-1):
    if C[i] == C[i+1] == x:
        sps.append(i)
ans = 0
for sp in sps:
    c = C[:sp] + C[sp+2:]
    while c:
        cur = c[0]
        s = L = 0
        for i in range(len(c)):
            if c[i] == cur:
                L += 1
            else:
                if L > 2: break
                L = 1
                s = i
                cur = c[i]
        if L < 3: break
        else:
            c = c[:s] + c[s+L:]
    ans = max(ans,n - len(c))
print ans
