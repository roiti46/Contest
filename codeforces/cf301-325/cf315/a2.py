# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T, S, q = map(int, raw_input().split())
ans = 0
while S < T:
    S *= q
    ans += 1
print ans

