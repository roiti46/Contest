# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split())

print max(0, 2 * sum(a) - 1 - sum(a[i] == a[i + 1] == 1 for i in xrange(n - 1)))

