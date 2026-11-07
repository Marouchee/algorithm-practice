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
    for m, g in cases:
        lines.append("%d %d" % (len(g), m))
        lines += [" ".join(map(str, row)) for row in g]
    return "\n".join(lines) + "\n"


def reference(cases):
    """2차원 누적 합으로 자리마다 O(1)에 합을 구한다"""
    out = []
    for tc, (m, g) in enumerate(cases, 1):
        n = len(g)
        s = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                s[i + 1][j + 1] = g[i][j] + s[i][j + 1] + s[i + 1][j] - s[i][j]
        sums = [s[i + m][j + m] - s[i][j + m] - s[i + m][j] + s[i][j]
                for i in range(n - m + 1) for j in range(n - m + 1)]
        best = max(sums)
        out.append("#%d %d %d" % (tc, best, sums.count(best)))
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    assert run("2\n4 2\n1 3 0 2\n2 0 5 1\n4 1 1 3\n0 2 2 0\n5 3\n2 0 1 0 2\n1 1 1 1 1\n0 2 0 2 0\n1 1 1 1 1\n2 0 1 0 2\n") == "#1 10 1\n#2 10 1\n"
    assert run(to_input([(2, [[1, 2, 0], [3, 1, 2], [0, 4, 1]])])) == "#1 8 2\n"   # 같은 최댓값 두 자리
    assert run(to_input([(1, [[0, 0], [0, 0]])])) == "#1 0 4\n"                    # 모두 0
    assert run(to_input([(1, [[7]])])) == "#1 7 1\n"                               # 1×1
    assert run(to_input([(3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])])) == "#1 45 1\n"  # M = N

    random.seed(0)
    for _ in range(200):
        cases = []
        for _ in range(random.randint(1, 10)):
            n = random.randint(1, 8)
            cases.append((random.randint(1, n), [[random.randint(0, 3) for _ in range(n)] for _ in range(n)]))
        text = to_input(cases)
        assert run(text) == reference(cases), text

    big = [(25, [[random.randint(0, 30) for _ in range(50)] for _ in range(50)]) for _ in range(10)]
    start = time.time()
    assert run(to_input(big)) == reference(big)
    print(f"최대 입력(T=10, N=50, M=25): {time.time() - start:.2f}s")
    print("all tests passed")
