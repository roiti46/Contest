n,k = map(int,raw_input().split())
a = map(int,raw_input().split())
ans = []
for ope in xrange(k):
    if max(a) == min(a):
        print 0,ope
        for line in ans:
            print line[0],line[1]
        break
    i,j = a.index(max(a)),a.index(min(a))
    ans.append([i+1,j+1])
    a[i] -= 1; a[j] += 1
else:
    print max(a)-min(a),ope+1
    for line in ans:
        print line[0],line[1]
