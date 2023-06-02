import sys
input = sys.stdin.readline

N = int(input())

dot = 2
for _ in range(N):
    dot = dot+(dot-1)
print(dot**2)