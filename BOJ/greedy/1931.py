import sys
sys.stdin = open("input.txt")

N = int(input())
time_list = []
for _ in range(N):
    start, end = map(int,input().split())
    time_list.append([start, end])
time_list = sorted(time_list, key=lambda x:x[0])
time_list = sorted(time_list, key=lambda x:x[1])
temp, cnt = -1, 0
for i in range(N):
    if temp > time_list[i][0]:
        continue
    temp = time_list[i][1]
    cnt += 1
print(cnt)