# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split())

mx, mn, cnt = coll.defaultdict(int), coll.defaultdict(int), coll.defaultdict(int)
for i in xrange(n):
    if mn[a[i]] == 0: mn[a[i]] = i + 1
    mx[a[i]] = i + 1
    cnt[a[i]] += 1

l, r = 1, n + 1 
occur = max(v for v in cnt.values())
for k, v in cnt.items():
    if v == occur:
        ll, rr = mn[k], mx[k]
        if (rr - ll) < (r- l):
            l, r = ll, rr
print l, r

