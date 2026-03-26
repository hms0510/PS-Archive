from collections import deque
N,M = map(int,input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int,input().split())))
    
dx = [-1,0,1,0]
dy = [0,-1,0,1]

visit = [[0 for _ in range(M)] for _ in range(N)]
landNum = 0 # 땅의 개수

# 땅 번호 표시 - bfs
for i in range(N):
    for j in range(M):
        if not lst[i][j] or visit[i][j]:
            continue
        q = deque([(i,j)])
        visit[i][j] = 1
        landNum += 1
        lst[i][j] = landNum
        while q:
            x,y = q.popleft()
            for dir in range(4):
                nx,ny = x+dx[dir],y+dy[dir]
                if not (0 <= nx < N and 0 <= ny < M) or visit[nx][ny]:
                    continue
                if not lst[nx][ny]:
                    continue
                lst[nx][ny] = landNum
                visit[nx][ny] = 1
                q.append((nx,ny))
    
check = {} # 쉽게 접근하여 최소 경로 갱신하기 위해 딕셔너리로 저장
for i in range(N):
    for j in range(M):
        if not lst[i][j] or lst[i][j] == landNum:
            continue
        
        cur = lst[i][j] # 현재 땅 번호
        for dir in range(4): # 네 방향 다 일자로 탐색
            dst = 0
            x,y = i,j
            pivot = False
            while True: 
                x,y = x+dx[dir],y+dy[dir]
                if not (0 <= x < N and 0 <= y < M) or pivot:
                    break
                dst += 1
                if lst[x][y] == cur: # 같은 땅이라면
                    break
                elif lst[x][y]: # 다른 땅이라면 
                    if dst == 2: # 다리 길이가 1이면 continue
                        break
                    first,second = min(cur,lst[x][y]),max(cur,lst[x][y]) # 번호 크기 순으로 경로 저장
                    if (first,second) in check: # 이미 경로가 존재한다면 최소값 갱신
                        check[(first,second)] = min(check[(first,second)],dst-1)
                        pivot = True
                    else: # 경로가 존재하지 않다면 초기화
                        check[(first,second)] = dst-1
                        pivot = True
                        
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 노드 합치기 (사이클 여부 반환)
def union(parent, size, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    # 같은 루트면 사이클 발생
    if rootA == rootB:
        return True
    
    # 더 작은 쪽을 부모로
    if size[rootA] < size[rootB]:
        rootA, rootB = rootB, rootA

    parent[rootB] = rootA
    size[rootA] += size[rootB]

    return False

parent = [i for i in range(landNum+1)]
size = [1] * (landNum+1)

# edges 리스트에 check에 저장했던 경로 옮기기
edges = []
for key, value in check.items():
    a,b = key
    edges.append((value,a,b))
edges.sort()

res = 0
cnt = 0

# 크루스칼 알고리즘 적용
for cost,a,b in edges:
    if union(parent,size,a,b): # 사이클 발생하면 continue
        continue
    
    res += cost
    cnt += 1
    if cnt == landNum-1:
        break
    
if res:
    print(res)
else:
    print(-1)
