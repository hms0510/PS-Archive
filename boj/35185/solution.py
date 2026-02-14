def simulation(start, N, L, visit):
    idx = start
    for i in range(L):
        if command[i] == "L" and idx != 0:
            idx -= 1
        elif command[i] == "R" and idx != N-1:
            idx += 1
        
        if i != L-1:
            visit[idx] = True
    
    return idx
N,L = map(int,input().split())
command = input()

# case1 - 가장 왼쪽에서 시작
visit = [False for _ in range(N)]
visit[0] = True
idx = simulation(0, N, L, visit)
if not visit[idx]:
    print("WIN")
    print(1, idx+1)
    exit()
    
#case2 - 가장 오른쪽에서 시작
visit = [False for _ in range(N)]
visit[N-1] = True
idx = simulation(N-1, N, L, visit)
if not visit[idx]:
    print("WIN")
    print(N, idx+1)
    exit()
    
#case3 - case1, case2 모두 명령어의 마지막 수행으로 도달한 위치가 이미 도달했던 위치인 경우
print("DEFEAT")
