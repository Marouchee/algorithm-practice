"""프로그래머스 Lv.2 미로 탈출 (BFS)
https://school.programmers.co.kr/learn/courses/30/lessons/159993

접근: S, L, E 위치를 찾은 뒤 BFS를 두 번 한다. S에서 시작한 BFS로 L까지 거리, dist를 새로 만들어 L에서 시작한 BFS로 E까지 거리를 구한다.
      둘 중 하나라도 -1(도달 불가)이면 -1, 아니면 두 거리의 합을 리턴한다. 벽(X)만 막히고 E는 레버 전에도 지나갈 수 있다.
시간 복잡도: O(n · m). BFS 두 번, 각 칸은 BFS마다 한 번만 큐에 들어간다
"""
import random
import time
from collections import deque


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dist = [[-1 for _ in range (m)] for _ in range(n)]
    n_list = [(1,0), (-1,0), (0,-1), (0,1)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'L':
                leber = (i,j)
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i,j)
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'E':
                exit = (i,j)

    q = deque([start])
    dist[start[0]][start[1]] = 0
    while q:
        x, y = q.popleft()
        for a,b in n_list:
            nx = x + a
            ny = y + b
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            if maps[nx][ny] == 'X':
                continue
            if dist[nx][ny] != -1:
                continue
            q.append((nx,ny))
            dist[nx][ny] = dist[x][y] + 1

    start_to_leber = dist[leber[0]][leber[1]]

    dist = [[-1 for _ in range (m)] for _ in range(n)]
    q = deque([leber])
    dist[leber[0]][leber[1]] = 0
    while q:
        x, y = q.popleft()
        for a,b in n_list:
            nx = x + a
            ny = y + b
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            if maps[nx][ny] == 'X':
                continue
            if dist[nx][ny] != -1:
                continue
            q.append((nx,ny))
            dist[nx][ny] = dist[x][y] + 1

    leber_to_exit = dist[exit[0]][exit[1]]

    if start_to_leber == -1 or leber_to_exit == -1:
        answer = -1
    else:
        answer = start_to_leber + leber_to_exit

    return answer


def by_state_bfs(maps):
    """(행, 열, 레버 당겼는지)를 한 상태로 보고 BFS 한 번으로 푼다 (비교용)"""
    n, m = len(maps), len(maps[0])
    sr, sc = next((r, c) for r in range(n) for c in range(m) if maps[r][c] == "S")
    seen = {(sr, sc, False)}
    q = deque([(sr, sc, False, 0)])
    while q:
        r, c, pulled, d = q.popleft()
        if pulled and maps[r][c] == "E":
            return d
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] != "X":
                state = (nr, nc, pulled or maps[nr][nc] == "L")
                if state not in seen:
                    seen.add(state)
                    q.append((*state, d + 1))
    return -1


def make_maps(n, m, wall):
    grid = [["X" if random.random() < wall else "O" for _ in range(m)] for _ in range(n)]
    cells = random.sample([(r, c) for r in range(n) for c in range(m)], 3)
    for (r, c), ch in zip(cells, "SLE"):
        grid[r][c] = ch
    return ["".join(row) for row in grid]


if __name__ == "__main__":
    assert solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]) == 16
    assert solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]) == -1     # S가 벽에 갇힘
    assert solution(["SEOOL"]) == 7                                         # 레버 전에 E를 지나감 (4 + 3)
    assert solution(["SOL", "XXX", "OOE"]) == -1                            # L까지는 가지만 E로 못 감
    assert solution(["LSE"]) == 3                                           # 왔던 길을 되돌아감 (1 + 2)

    random.seed(0)
    for _ in range(3000):
        n, m = random.randint(1, 7), random.randint(1, 7)
        if n * m < 3:
            continue
        mp = make_maps(n, m, random.choice([0.1, 0.3, 0.5]))
        assert solution(mp) == by_state_bfs(mp), mp

    big = ["S" + "O" * 98 + "L"] + ["O" * 100] * 98 + ["E" + "O" * 99]
    start = time.time()
    assert solution(big) == 99 + 198
    print(f"100x100: {time.time() - start:.3f}s")
    print("all tests passed")
