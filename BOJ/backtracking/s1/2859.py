import sys
sys.stdin = open("input.txt")

K = int(input())
inequality = input().split()

number = [i for i in range(10)]
bit = [0]*10

max_num = '0'
min_num = '9999999999'

def backtracking(depth,num_list):
    global max_num, min_num
    print(num_list)
    if depth == (K+1):
        max_num = max(max_num,''.join(s for s in num_list))
        min_num = min(min_num,''.join(s for s in num_list))            
        return
    
    for i in range(10):
        if bit[i] == 0:
            if inequality[depth-1] == '<' and num_list[depth-1] > str(i):
                continue

            if inequality[depth-1] == '>' and num_list[depth-1] < str(i):
                continue

            num_list.append(str(i))
            bit[i] = 1
            backtracking(depth+1,num_list)
            num_list.pop()
            bit[i] = 0

for i in range(10):
    bit[i] = 1
    backtracking(1,[str(i)])
    bit[i] = 0
print(max_num,min_num)