import bisect
a = input()
A = sorted(map(int,raw_input().split()))
b = input()
B = sorted(map(int,raw_input().split()))
adv = -10**15
pa = pb = 0
for i in range(a):
    d = A[i]-1
    j = bisect.bisect(B,d)
    p1,p2 = 3*(a-i)+2*i,3*(b-j)+2*j
    tmp = p1-p2
    if tmp > adv or (tmp == adv and p1 > pa):
        adv = p1-p2
        pa,pb = p1,p2
p1,p2 = 2*a,2*b
tmp = p1-p2
if tmp > adv or (tmp == adv and p1 > pa):
    pa,pb = p1,p2
print "%s:%s"%(pa,pb)
