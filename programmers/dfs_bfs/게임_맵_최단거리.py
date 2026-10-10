"""프로그래머스 Lv.2 게임 맵 최단거리 (BFS)
https://school.programmers.co.kr/learn/courses/30/lessons/1844

접근: BFS는 가까운 칸부터 꺼내므로 처음 도착한 거리가 최단거리다. dist를 -1(미방문)로 채우고 시작 칸을 1로 둔 뒤,
      범위 안이고 벽이 아니며 아직 방문하지 않은 이웃만 dist = 현재 거리 + 1로 큐에 넣는다.
      도착 칸에 못 가면 dist가 -1로 남으므로 그대로 리턴한다.
시간 복잡도: O(n · m). 각 칸은 큐에 한 번만 들어간다
"""
import random
import time
from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    n_list = [(1,0), (-1,0), (0,1), (0,-1)]

    dist = [[-1 for _ in range(m)] for _ in range(n)]
    q = deque([(0,0)])
    dist[0][0] = 1

    while q:
        a, b = q.popleft()
        for x,y in n_list:
            na = a + x
            nb = b + y
            if na < 0 or na > n-1 or nb < 0 or nb > m-1:
                continue
            if maps[na][nb] == 0:
                continue
            if dist[na][nb] != -1:
                continue
            dist[na][nb] = dist[a][b] + 1
            q.append((na,nb))

    return dist[n-1][m-1]


def relax_until_stable(maps):
    """BFS 없이, 더 짧은 거리가 나오지 않을 때까지 전체 칸을 반복 갱신한다 (비교용)"""
    n, m = len(maps), len(maps[0])
    INF = float("inf")
    d = [[INF] * m for _ in range(n)]
    d[0][0] = 1
    changed = True
    while changed:
        changed = False
        for r in range(n):
            for c in range(m):
                if maps[r][c] == 0 or d[r][c] == INF:
                    continue
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] and d[r][c] + 1 < d[nr][nc]:
                        d[nr][nc] = d[r][c] + 1
                        changed = True
    return -1 if d[n-1][m-1] == INF else d[n-1][m-1]


if __name__ == "__main__":
    ex1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    ex2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
    assert solution(ex1) == 11
    assert solution(ex2) == -1                       # 도착 칸이 막힘
    assert solution([[1, 0, 1], [1, 1, 1], [0, 0, 1]]) == 5
    assert solution([[1, 1]]) == 2                   # 1행
    assert solution([[1], [0], [1]]) == -1           # 1열, 중간이 벽

    random.seed(0)
    for _ in range(3000):
        n, m = random.randint(1, 7), random.randint(1, 7)
        if n == m == 1:
            continue
        mp = [[1 if random.random() < 0.7 else 0 for _ in range(m)] for _ in range(n)]
        mp[0][0] = mp[n-1][m-1] = 1
        assert solution(mp) == relax_until_stable(mp), mp

    big = [[1] * 100 for _ in range(100)]
    start = time.time()
    assert solution(big) == 199
    print(f"100x100: {time.time() - start:.3f}s")
    print("all tests passed")
