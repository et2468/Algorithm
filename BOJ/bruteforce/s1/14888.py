import sys
sys.stdin = open('input.txt')

N = int(input())
num_list = list(map(int,input().split()))
operaters = ['+','-','*','//']
operater_cnt = list(map(int,input().split()))

max_answer = -(10**9)
min_answer = 10**9

def bruteforce(depth, result):
    global max_answer, min_answer
    if depth == N:
        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)
        return
    for i in range(4):
        if operater_cnt[i]:
            temp = result
            if operaters[i] == '+':
                result += num_list[depth]
            elif operaters[i] == '-':
                result -= num_list[depth]
            elif operaters[i] == '*':
                result *= num_list[depth]
            else:
                if result >= 0:
                    result //= num_list[depth]
                else:
                    result = -((-result) // num_list[depth])
            
            operater_cnt[i] -= 1
            bruteforce(depth+1,result)
            operater_cnt[i] += 1
            result = temp
            
bruteforce(1,num_list[0])
print(max_answer)
print(min_answer)