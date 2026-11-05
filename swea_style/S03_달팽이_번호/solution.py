"""S03 달팽이 번호: problem.md

접근: (0, 0)에 1을 적고, 현재 방향(오른쪽 → 아래 → 왼쪽 → 위)으로 다음 칸을 본다.
      판 밖이거나 이미 적힌 칸이면 rol_count를 1 늘려 시계 방향으로 돌고, 돈 뒤에도 갈 곳이 없으면 끝낸다.
      방향 번호는 rol_count % 4. 질문 (r, c)는 1부터 세므로 board[r-1][c-1]을 답한다.
시간 복잡도: O(T · (N · M + Q)). 칸마다 한 번 적고, 질문은 채운 뒤 따로 답한다
"""
from collections import deque

T = int(input())
for num in range(T):
    N,M  = map(int, input().split())
    board = []
    n_list = [(0,1), (1,0), (0,-1), (-1,0)]
    for _ in range(N):
        board.append([-1 for _ in range(M)])
    Q = int(input())

    q = deque([(0,0)])
    board[0][0] = 1
    rol_count = 0
    while q:
        x,y = q.popleft()
        nx = x + n_list[rol_count%4][0]
        ny = y + n_list[rol_count%4][1]
        if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
            rol_count += 1
            temp_nx = x + n_list[rol_count%4][0]
            temp_ny = y + n_list[rol_count%4][1]
            if temp_nx < 0 or temp_ny < 0 or temp_nx > N-1 or temp_ny > M-1:
                break
            elif board[temp_nx][temp_ny] != -1:
                break
            else:
                board[temp_nx][temp_ny] = board[x][y] + 1
                q.append((temp_nx,temp_ny))
                continue
        if board[nx][ny] != -1:
            rol_count += 1
            temp_nx = x + n_list[rol_count%4][0]
            temp_ny = y + n_list[rol_count%4][1]
            if temp_nx < 0 or temp_ny < 0 or temp_nx > N-1 or temp_ny > M-1:
                break
            elif board[temp_nx][temp_ny] != -1:
                break
            else:
                board[temp_nx][temp_ny] = board[x][y] + 1
                q.append((temp_nx,temp_ny))
                continue
        board[nx][ny] = board[x][y] + 1
        q.append((nx,ny))

    q_list = []
    for _ in range(Q):
        r,c = map(int, input().split())
        q_list.append((r,c))
    ans_list = []
    for a,b in q_list:
        ans_list.append(board[a-1][b-1])
    print(f"#{num+1}", *ans_list)
