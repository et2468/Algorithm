import sys
sys.stdin = open('input.txt')

    
N = int(input())
answer = 0

DP = [1]*10
DP[0] = 0

for _ in range(N-1):
    temp = DP[:]
    for i in range(10):
        if i == 0:
            DP[i] = temp[1]
        elif i == 9:
            DP[i] = temp[8]
        else:
            DP[i] = temp[i-1] + temp[i+1]

print(sum(DP)%1000000000)