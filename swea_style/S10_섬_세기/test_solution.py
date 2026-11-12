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
        lines += [" ".join(map(str, row)) for row in g]
    return "\n".join(lines) + "\n"


def reference(cases):
    """유니온파인드로 섬을 묶어 센다 (DFS와 다른 방법)"""
    out = []
    for tc, g in enumerate(cases, 1):
        n, m = len(g), len(g[0])
        parent = list(range(n * m))

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        for i in range(n):
            for j in range(m):
                if g[i][j]:
                    if i + 1 < n and g[i + 1][j]:
                        parent[find(i * m + j)] = find((i + 1) * m + j)
                    if j + 1 < m and g[i][j + 1]:
                        parent[find(i * m + j)] = find(i * m + j + 1)
        size = {}
        for i in range(n):
            for j in range(m):
                if g[i][j]:
                    r = find(i * m + j)
                    size[r] = size.get(r, 0) + 1
        out.append("#%d %d %d" % (tc, len(size), max(size.values()) if size else 0))
    return "\n".join(out) + "\n"


def rand_grid(n, m, land):
    return [[1 if random.random() < land else 0 for _ in range(m)] for _ in range(n)]


def snake(n, m):
    g = [[1] * m for _ in range(n)]
    for i in range(1, n, 2):
        g[i] = [0] * m
        g[i][m - 1 if (i // 2) % 2 == 0 else 0] = 1
    return g


if __name__ == "__main__":
    sample = [[[1, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 1, 0, 0], [1, 1, 1, 0, 1]],
              [[0, 0, 0]] * 3, [[1, 1, 1], [1, 1, 1]]]
    assert run(to_input(sample)) == "#1 4 4\n#2 0 0\n#3 1 6\n"
    assert run(to_input([[[1, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1]]])) == "#1 3 4\n"
    assert run(to_input([[[1]], [[0]], [[1, 0], [0, 1]]])) == "#1 1 1\n#2 0 0\n#3 2 1\n"   # 대각선은 다른 섬

    random.seed(0)
    for _ in range(200):
        cases = [rand_grid(random.randint(1, 8), random.randint(1, 8), random.choice([0.3, 0.5, 0.7]))
                 for _ in range(random.randint(1, 10))]
        text = to_input(cases)
        assert run(text) == reference(cases), text

    big = [[[1] * 100 for _ in range(100)], snake(100, 100),
           [[(i + j) % 2 for j in range(100)] for i in range(100)]] + [rand_grid(100, 100, 0.55) for _ in range(7)]
    start = time.time()
    out = run(to_input(big))
    print(f"최대 입력(T=10, 100×100, 전부 땅·뱀 모양·체스판 포함): {time.time() - start:.2f}s")
    assert out == reference(big)
    print("all tests passed")
