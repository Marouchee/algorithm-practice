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


def snail(n, m):
    g = [[0] * m for _ in range(n)]
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    x = y = d = 0
    for v in range(1, n * m + 1):
        g[x][y] = v
        nx, ny = x + dirs[d][0], y + dirs[d][1]
        if not (0 <= nx < n and 0 <= ny < m) or g[nx][ny]:
            d = (d + 1) % 4
            nx, ny = x + dirs[d][0], y + dirs[d][1]
        x, y = nx, ny
    return g


def to_input(cases):
    lines = [str(len(cases))]
    for n, m, qs in cases:
        lines += ["%d %d" % (n, m), str(len(qs))] + ["%d %d" % q for q in qs]
    return "\n".join(lines) + "\n"


def reference(cases):
    out = []
    for tc, (n, m, qs) in enumerate(cases, 1):
        g = snail(n, m)
        out.append(" ".join(["#%d" % tc] + [str(g[r - 1][c - 1]) for r, c in qs]))
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    assert run(to_input([(3, 4, [(1, 1), (2, 1), (2, 3)]), (5, 3, [(3, 2), (5, 1)])])) == "#1 1 10 12\n#2 14 9\n"
    every = [(r, c) for r in range(1, 5) for c in range(1, 4)]
    assert run(to_input([(4, 3, every[:10])])) == "#1 1 2 3 10 11 4 9 12 5 8\n"
    assert run(to_input([(1, 1, [(1, 1)])])) == "#1 1\n"                         # 1×1
    assert run(to_input([(1, 5, [(1, 5), (1, 1)])])) == "#1 5 1\n"               # 한 줄
    assert run(to_input([(5, 1, [(5, 1), (3, 1)])])) == "#1 5 3\n"               # 한 열

    random.seed(0)
    for _ in range(200):
        cases = []
        for _ in range(random.randint(1, 10)):
            n, m = random.randint(1, 9), random.randint(1, 9)
            cases.append((n, m, [(random.randint(1, n), random.randint(1, m)) for _ in range(random.randint(1, 10))]))
        text = to_input(cases)
        assert run(text) == reference(cases), text

    big = [(100, 100, [(random.randint(1, 100), random.randint(1, 100)) for _ in range(10)]) for _ in range(10)]
    start = time.time()
    assert run(to_input(big)) == reference(big)
    print(f"최대 입력(T=10, 100×100): {time.time() - start:.2f}s")
    print("all tests passed")
