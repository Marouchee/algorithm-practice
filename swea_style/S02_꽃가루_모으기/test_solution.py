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


def reference(cases):
    out = []
    for tc, (n, m, g) in enumerate(cases, 1):
        best = 0
        for i in range(n):
            for j in range(m):
                k = g[i][j]
                total = k
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    for step in range(1, k + 1):
                        x, y = i + di * step, j + dj * step
                        if 0 <= x < n and 0 <= y < m:
                            total += g[x][y]
                best = max(best, total)
        out.append("#%d %d" % (tc, best))
    return "\n".join(out) + "\n"


def to_input(cases):
    lines = [str(len(cases))]
    for n, m, g in cases:
        lines.append("%d %d" % (n, m))
        lines.extend(" ".join(map(str, row)) for row in g)
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    sample = [(3, 4, [[1, 0, 2, 1], [3, 1, 0, 4], [0, 2, 1, 1]]),
              (5, 5, [[0, 1, 0, 2, 1], [1, 2, 1, 0, 3], [0, 4, 1, 1, 0], [2, 0, 1, 3, 1], [1, 1, 0, 1, 2]])]
    assert run(to_input(sample)) == "#1 10\n#2 11\n"
    assert run(to_input([(3, 3, [[1, 2, 0], [0, 3, 1], [2, 0, 4]])])) == "#1 8\n"
    assert run(to_input([(1, 1, [[7]])])) == "#1 7\n"                    # 1×1: 자기 칸만
    assert run(to_input([(2, 2, [[0, 0], [0, 0]])])) == "#1 0\n"          # 전부 0
    assert run(to_input([(1, 5, [[9] * 5])])) == "#1 45\n"                # 한 줄, k가 화단보다 큼

    random.seed(0)
    for _ in range(200):
        cases = []
        for _ in range(random.randint(1, 10)):
            n, m = random.randint(1, 8), random.randint(1, 8)
            cases.append((n, m, [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]))
        text = to_input(cases)
        assert run(text) == reference(cases), text

    big = [(100, 100, [[9] * 100 for _ in range(100)]) for _ in range(10)]   # 모든 칸 k = 9: 가장 많이 계산
    start = time.time()
    assert run(to_input(big)) == reference(big)
    print(f"최대 입력(T=10, 100×100, 모두 9): {time.time() - start:.2f}s (CPython, 비교용 풀이 포함)")
    print("all tests passed")
