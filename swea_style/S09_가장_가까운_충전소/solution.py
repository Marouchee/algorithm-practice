"""S09 가장 가까운 충전소: problem.md

접근: R에서 BFS로 가까운 칸부터 거리를 매긴다. dist를 -1로 채워 두고, -1이 아니면 이미 방문한 칸으로 본다.
      칸을 큐에 넣을 때 dist를 적으므로(방문 표시) 각 칸은 한 번만 들어간다.
      이웃이 충전소면 그 거리가 가장 가까운 충전소까지의 거리다(BFS는 거리 순서로 칸을 넓혀 가므로). 큐가 비면 -1.
시간 복잡도: O(T · N · M)
"""
from collections import deque
T = int(input())

for num in range(T):
    N,M = map(int, input().split())
    graph = []
    dist = [[-1 for _ in range(M)] for _ in range(N)]
    n_list = [(1,0), (0,1), (-1,0), (0,-1)]

    for _ in range(N):
        graph.append(list(input()))
    
    flag = False
    anx_x = ''
    ans_y = ''
    q = deque([])
    for i in range(N):
        if flag:
            break
        for j in range(M):
            if graph[i][j] == 'R':
                q.append((i,j))
                dist[i][j] = 0
                flag = True
                break
    
    flag = False
    while q:
        if flag:
            break
        x,y = q.popleft()
        for a,b in n_list:
            nx = x+a
            ny = y+b
            if nx<0 or ny<0 or nx>N-1 or ny>M-1:
                continue
            if dist[nx][ny] != -1:
                continue
            if graph[nx][ny] == '#':
                continue
            if graph[nx][ny] == 'C':
                dist[nx][ny] = dist[x][y] + 1
                ans_x = nx
                ans_y = ny
                flag = True
                break
            else:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))
    
    if flag:
        print(f"#{num+1} {dist[ans_x][ans_y]}")
    else:
        print(f"#{num+1} -1")
