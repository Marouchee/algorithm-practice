"""S10 섬 세기: problem.md

접근: 모든 칸을 돌다가 아직 안 간 땅(1)을 만나면 섬 개수 +1, 그 칸에서 스택 DFS를 시작한다.
      재귀 대신 스택(deque의 오른쪽 pop)으로 반복한다. 전부 땅인 100×100이면 재귀 깊이가 10000까지 가기 때문이다.
      스택에 넣을 때 칸을 -1로 바꿔 방문 표시하고 넓이 +1. DFS가 끝나면 넓이로 최댓값을 갱신한다.
시간 복잡도: O(T · N · M)
"""
from collections import deque
T = int(input())

for num in range(T):
    N,M = map(int, input().split())
    graph = []
    count = 0
    max_val = 0
    n_list = [(1,0), (-1,0), (0,1), (0,-1)]

    for _ in range(N):
        graph.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                q = deque([(i,j)])
                graph[i][j] = -1
                temp_val = 1
                count += 1
                while q:
                    x,y = q.pop()
                    for a,b in n_list:
                        nx = x+a
                        ny = y+b
                        if nx<0 or ny<0 or nx>N-1 or ny>M-1:
                            continue
                        if graph[nx][ny] != 1:
                            continue
                        q.append((nx,ny))
                        graph[nx][ny] = -1
                        temp_val += 1
                if temp_val > max_val:
                    max_val = temp_val
    
    print(f"#{num+1} {count} {max_val}")
