f,s = 0,0
fa,sa = [],[]
n = input()
for roop in range(n):
    a = raw_input()
    if a[0] != "-":
        f += int(a)
        fa.append(int(a))
    else:
        s += int(a[1:])
        sa.append(int(a[1:]))
else:
    last = a

ans = ""
if f > s  : ans = "first"
elif f < s: ans = "second"
else:
    for i,j in zip(fa,sa):
        if   i > j: ans = "first"
        elif i < j: ans = "second"
        if ans: break
    else:
        if   len(fa) > len(sa): ans = "first"
        elif len(fa) < len(sa): ans = "second"
        else:
            if last[0] != "-": ans = "first"
            else: ans = "second"
print ans
