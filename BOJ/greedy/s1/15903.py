import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
card_list = list(map(int,input().split()))
for _ in range(M):
    card_list.sort()
    card_list[0], card_list[1] = card_list[0] + card_list[1], card_list[0] + card_list[1]
print(sum(card_list))