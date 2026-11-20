"""solution.py를 표준 입력으로 실행해 출력 전체를 비교한다"""
import os
import random
import subprocess
import sys
import time

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


MOVE = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
TURN = {'/': {0: 1, 1: 0, 2: 3, 3: 2}, '\\': {0: 3, 1: 2, 2: 1, 3: 0}}


def reference(cases):
    """밝혀진 칸을 set으로 모은다 (풀이와 다른 표현)"""
    out = []
    for tc, g in enumerate(cases, 1):
        n, m = len(g), len(g[0])
        starts = [(i, 0, 1) for i in range(n)] + [(i, m - 1, 3) for i in range(n)]
        starts += [(0, j, 2) for j in range(m)] + [(n - 1, j, 0) for j in range(m)]
        best = 0
        for r, c, d in starts:
            lit = set()
            while 0 <= r < n and 0 <= c < m and g[r][c] != '#':
                lit.add((r, c))
                d = TURN.get(g[r][c], {}).get(d, d)
                r, c = r + MOVE[d][0], c + MOVE[d][1]
            best = max(best, len(lit))
        out.append("#%d %d" % (tc, best))
    return "\n".join(out) + "\n"


def rand_grid(n, m, pm, pw):
    rows = []
    for _ in range(n):
        row = ""
        for _ in range(m):
            x = random.random()
            row += random.choice("/\\") if x < pm else ("#" if x < pm + pw else ".")
        rows.append(row)
    return rows


def zigzag(n, m):
    g = [['.'] * m for _ in range(n)]
    for i in range(0, n - 1, 2):
        g[i][m - 1], g[i + 1][m - 1] = '\\', '/'
        if i + 2 < n:
            g[i + 1][0], g[i + 2][0] = '/', '\\'
    return ["".join(r) for r in g]


if __name__ == "__main__":
    sample = [[".\\..", "....", ".\\./"], ["#"], [".#./.", "..\\#."]]
    assert run(to_input(sample)) == "#1 8\n#2 0\n#3 3\n"
    edge = [["."], ["/"], ["#"], ["\\"], ["..\\", "...", ".\\/"],      # 같은 칸을 두 번 지남 → 7
            ["###", "#/#", "###"], zigzag(6, 5)]
    assert run(to_input(edge)) == reference(edge)
    assert reference([["..\\", "...", ".\\/"]]) == "#1 7\n"

    random.seed(0)
    for _ in range(200):
        cases = [rand_grid(random.randint(1, 7), random.randint(1, 7), random.choice([0.2, 0.5, 0.8]),
                           random.choice([0, 0.1, 0.3])) for _ in range(random.randint(1, 10))]
        assert run(to_input(cases)) == reference(cases), cases

    big = [zigzag(50, 50), ["." * 50] * 50, ["\\/" * 25] * 50] + [rand_grid(50, 50, 0.3, 0.01) for _ in range(7)]
    start = time.time()
    out = run(to_input(big))
    print(f"최대 입력(T=10, 50×50): {time.time() - start:.2f}s")
    assert out == reference(big)
    print("all tests passed")
