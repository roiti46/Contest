a1,b1 = map(int,raw_input().split())
a2,b2 = map(int,raw_input().split())
ab1,ab2,n,m = a1*b1,a2*b2,0,0
ans = 0
while ab1%3 == 0: ab1 /= 3; n += 1
while ab2%3 == 0: ab2 /= 3; m += 1
ans += abs(n-m)

for divide in range(n-m):
    if   a1%3 == 0: a1 = 2*a1/3
    else: b1 = 2*b1/3
for divide in range(m-n):
    if   a2%3 == 0: a2 = 2*a2/3
    else: b2 = 2*b2/3
    
ab1,ab2,n,m = a1*b1,a2*b2,0,0
while ab1%2 == 0: ab1 /= 2; n += 1
while ab2%2 == 0: ab2 /= 2; m += 1
ans += abs(n-m)
for divide in range(n-m):
    if   a1%2 == 0: a1 /= 2
    else: b1 /= 2
for divide in range(m-n):
    if   a2%2 == 0: a2 /= 2
    else: b2 /= 2

if a1*b1 == a2*b2:
    print ans
    print a1,b1
    print a2,b2
else:
    print -1
