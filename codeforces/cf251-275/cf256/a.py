# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

a1, a2, a3 = map(int, raw_input().split())
b1, b2, b3 = map(int, raw_input().split())
n = int(raw_input())

m = (a1 + a2 + a3 + 4) / 5 + (b1 + b2 + b3 + 9) / 10
print "YES" if m <= n else "NO"
