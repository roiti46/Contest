n,m,k = map(int,raw_input().split())
A = [[0]*(m+2) for i in xrange(n+2)]
for step in xrange(k):
    y,x = map(int,raw_input().split())
    A[y][x] = 1
    if max(sum(A[y][x-1:x+1])+sum(A[y-1][x-1:x+1]), sum(A[y][x:x+2])+sum(A[y-1][x:x+2]),
            sum(A[y][x-1:x+1])+sum(A[y+1][x-1:x+1]), sum(A[y][x:x+2])+sum(A[y+1][x:x+2])) == 4:
        print step+1
        break
else:
    print 0
