def gcd(a,b):
    while b: a,b = b,a%b
    return a

n,x,y = map(int,raw_input().split())
g = gcd(x,y)
x,y = y/g,x/g
at = sorted([x*i for i in range(1,y)]+[y*i for i in range(1,x)])
at = [0 if ele%x == 0 else 1 for ele in at] + [2,2]
l = len(at)
for roop in range(n):
    a = int(raw_input())
    print ["Vanya","Vova","Both"][at[(a-1)%l]]
