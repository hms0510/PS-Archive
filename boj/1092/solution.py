import sys
input = sys.stdin.readline

N = int(input())
cranes = list(map(int,input().split()))
M = int(input())
boxes = list(map(int,input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
    exit()
    
cnt = 0
while boxes:
    cnt += 1
    idx = 0
    for crane in cranes:
        while idx < len(boxes):
            if crane >= boxes[idx]:
                boxes.pop(idx)
                break
            else:
                idx += 1
                
print(cnt)
