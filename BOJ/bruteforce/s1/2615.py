import sys
sys.stdin = open('input.txt')
from itertools import combinations
n = int(input())
S = list(map(int,input().split()))
bit = [0]*(sum(S)+2)

for i in range(n+1):
    for sub_set in combinations(S,i):
        bit[sum(sub_set)] = 1
for i in range(sum(S)+2):
    if bit[i] == 0:
        print(i)
        break