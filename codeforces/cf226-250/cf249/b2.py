a,k = raw_input().split()
a = map(int,list(a))
k = int(k)
for i in range(len(a)-1):
    m = a[i]
    p = 0
    for j in range(i+1,min(i+k+1,len(a))):
        if a[j] > m:
            m = a[j]
            p = j
    if p > 0:
        a[i:p+1] = [a[p]]+a[i:p]
        k -= p-i
    if k == 0: break
print "".join(map(str,a))
