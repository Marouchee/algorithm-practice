"""solution.py를 표준 입력으로 실행해 출력 전체를 비교한다"""
import os
import random
import subprocess
import sys
import time
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))
SOLUTION = os.path.join(HERE, "solution.py")


def run(text):
    return subprocess.run([sys.executable, SOLUTION], input=text, capture_output=True,
                          text=True, check=True).stdout


def to_input(cases):
    lines = [str(len(cases))]
    for g in cases:
        lines.append("%d %d" % (len(g), len(g[0])))
        lines += g
    return "\n".join(lines) + "\n"


def reference(cases):
    """모든 충전소에서 동시에 BFS를 돌려 R까지의 거리를 본다 (풀이와 반대 방향)"""
    out = []
    for tc, g in enumerate(cases, 1):
        n, m = len(g), len(g[0])
        dist = [[-1] * m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if g[i][j] == 'C':
                    dist[i][j] = 0
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != '#' and dist[nx][ny] < 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        r = [(i, j) for i in range(n) for j in range(m) if g[i][j] == 'R'][0]
        out.append("#%d %d" % (tc, dist[r[0]][r[1]]))
    return "\n".join(out) + "\n"


def rand_grid(n, m, wall, chargers):
    cells = [(i, j) for i in range(n) for j in range(m)]
    random.shuffle(cells)
    g = [['#' if random.random() < wall else '.' for _ in range(m)] for _ in range(n)]
    g[cells[0][0]][cells[0][1]] = 'R'
    for i, j in cells[1:1 + chargers]:
        g[i][j] = 'C'
    return ["".join(row) for row in g]


def snake(n, m):
    """홀수 행은 벽이고 끝 한 칸만 뚫린 긴 길. R은 왼쪽 위, C는 길 끝"""
    g = [['.'] * m for _ in range(n)]
    for i in range(1, n, 2):
        g[i] = ['#'] * m
        g[i][m - 1 if (i // 2) % 2 == 0 else 0] = '.'
    g[0][0] = 'R'
    last = n - 1 if (n - 1) % 2 == 0 else n - 2
    g[last][m - 1 if (last // 2) % 2 == 1 else 0] = 'C'
    return ["".join(row) for row in g]


if __name__ == "__main__":
    sample = [["R..#.", ".#.#C", ".#...", "...#."], ["R#C", "##.", "..."], ["C..R", "...C"]]
    assert run(to_input(sample)) == "#1 7\n#2 -1\n#3 1\n"
    assert run(to_input([["R.#C", ".#..", "...."]])) == "#1 7\n"
    assert run(to_input([["RC"], ["C", "R"], ["R#C"], ["C.R.C"]])) == "#1 1\n#2 1\n#3 -1\n#4 2\n"
    assert run(to_input([["R#", "#C"]])) == "#1 -1\n"                          # 대각선은 못 감

    random.seed(0)
    for _ in range(200):
        cases = []
        for _ in range(random.randint(1, 10)):
            n, m = random.randint(1, 8), random.randint(2, 8)
            cases.append(rand_grid(n, m, random.choice([0.2, 0.35]), random.randint(1, 3)))
        text = to_input(cases)
        assert run(text) == reference(cases), text

    big = [snake(100, 100), snake(99, 100)] + [rand_grid(100, 100, 0.1, 1) for _ in range(8)]
    start = time.time()
    out = run(to_input(big))
    print(f"최대 입력(T=10, 100×100, 긴 길 포함): {time.time() - start:.2f}s")
    assert out == reference(big)
    print("all tests passed")
