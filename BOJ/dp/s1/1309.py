import sys
sys.stdin = open("input.txt")

N = int(input())
DP = [1]*3
for i in range(1,N):
    t = [0]*3
    t[0] = (DP[1]+DP[2])//9901
    t[1] = (DP[0]+DP[2])//9901
    t[2] = (DP[0]+DP[1]+DP[2])//9901
    DP = t[:]
print(sum(DP)//9901)   