"""프로그래머스 Lv.2 리코쳇 로봇 (BFS)
https://school.programmers.co.kr/learn/courses/30/lessons/169199

접근: 로봇이 멈추는 칸을 BFS의 노드로 본다. 칸마다 네 방향으로 벽이나 D를 만날 때까지 미끄러지고,
      넘어간 한 칸을 되돌린 자리가 다음 노드다. 처음 도착한 칸의 dist가 최소 이동 횟수이고, G에 못 가면 -1.
      (모의고사 때는 출발 칸을 `ny = x + b`로 쓰고, 미끄러질 때 `nx = x + a`로 매번 출발점 옆으로 돌아가 틀렸다)
시간 복잡도: O(N · M · max(N, M)). 칸 N·M개마다 네 방향 × 최대 max(N, M)칸을 미끄러진다. 100×100이면 약 400만 번
"""
import random
import time
from collections import deque


def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    dist = [[-1 for _ in range(m)] for _ in range(n)]
    n_list = [(1,0), (-1,0), (0,1), (0,-1)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                red = (i,j)
            if board[i][j] == 'G':
                green = (i,j)

    q = deque([red])
    dist[red[0]][red[1]] = 0
    while q:
        x,y = q.popleft()
        for a,b in n_list:
            nx = x + a
            ny = y + b
            for _ in range(max(n,m)):
                if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                    nx = nx - a
                    ny = ny - b
                    break
                if board[nx][ny] == 'D':
                    nx = nx - a
                    ny = ny - b
                    break
                nx = nx + a
                ny = ny + b
            if dist[nx][ny] != -1:
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx,ny))

    answer = dist[green[0]][green[1]]
    return answer


def by_while_slide(board):
    """다음 칸이 막혔는지 먼저 보고 while로 미끄러지는 방식 (비교용)"""
    n, m = len(board), len(board[0])
    start = next((r, c) for r in range(n) for c in range(m) if board[r][c] == "R")
    seen = {start}
    q = deque([(start, 0)])
    while q:
        (r, c), d = q.popleft()
        if board[r][c] == "G":
            return d
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r, c
            while 0 <= nr + dr < n and 0 <= nc + dc < m and board[nr + dr][nc + dc] != "D":
                nr += dr
                nc += dc
            if (nr, nc) not in seen:
                seen.add((nr, nc))
                q.append(((nr, nc), d + 1))
    return -1


def make_board(n, m, wall):
    grid = [["D" if random.random() < wall else "." for _ in range(m)] for _ in range(n)]
    (r1, c1), (r2, c2) = random.sample([(r, c) for r in range(n) for c in range(m)], 2)
    grid[r1][c1], grid[r2][c2] = "R", "G"
    return ["".join(row) for row in grid]


if __name__ == "__main__":
    assert solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]) == 7
    assert solution([".D.R", "....", ".G..", "...D"]) == -1
    assert solution(["RG"]) == 1                              # 바로 옆이 G이고 그 뒤가 벽
    assert solution(["R.G"]) == 1                             # 끝까지 미끄러져 벽 앞 G에서 멈춤
    assert solution(["R.G."]) == -1                           # G 위를 지나가기만 하고 멈추지 못함
    assert solution(["R", ".", "G"]) == 1                     # n > m (세로로 긴 판)
    assert solution(["R...D", "....G"]) == 2                  # 아래로 내려간 뒤 오른쪽 끝 G까지

    random.seed(0)
    for _ in range(3000):
        n, m = random.randint(1, 8), random.randint(1, 8)
        if n * m < 2:
            continue
        b = make_board(n, m, random.choice([0.1, 0.2, 0.4]))
        assert solution(b) == by_while_slide(b), b

    big = make_board(100, 100, 0.05)
    start = time.time()
    assert solution(big) == by_while_slide(big)
    print(f"100x100: {time.time() - start:.3f}s")
    print("all tests passed")
