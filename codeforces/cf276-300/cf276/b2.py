n = int(raw_input())
xy = [map(int,raw_input().split()) for _ in range(n)]
x,y = [x for x,y in xy], [y for x,y in xy]
a = max((max(x)-min(x)),(max(y)-min(y)))
print a*a
