mod = 10 ** 9 + 7

def fact(n):
	res = 1
	while n:
		res = (res * n)
		n -= 1
	return res

k = int(raw_input())
a = [int(raw_input()) for i in xrange(k)]

ans = 1
ball = a[0]
for ai in a[1:]:
	ans = (ans * fact(ball + ai - 1) / fact(ball) / fact(ai - 1)) % mod
	ball += ai
print ans
