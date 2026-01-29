import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
goods = list(map(int,input().split()))
M = int(input())
boxes = list(map(int,input().split()))

goods.sort(reverse=True)
boxes.sort(reverse=True)

#boxes = deque()
#for i in boxes_input:
#    boxes.append(i)
    
cnt = 0
if goods[0] < boxes[0]:
    print(-1)
    exit()

check = 0
while check != M:
    cnt += 1
    for i in range(N):
        for j in range(M):
            if boxes[j] != -1 and goods[i] >= boxes[j]:
                check += 1
                boxes[j] = -1
                break
print(cnt)
