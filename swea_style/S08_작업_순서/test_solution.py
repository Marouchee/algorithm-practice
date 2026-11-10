"""solution.py를 표준 입력으로 실행해 출력 전체를 비교한다"""
import os
import random
import subprocess
import sys
import time
from itertools import permutations

HERE = os.path.dirname(os.path.abspath(__file__))
SOLUTION = os.path.join(HERE, "solution.py")


def run(text):
    return subprocess.run([sys.executable, SOLUTION], input=text, capture_output=True,
                          text=True, check=True).stdout


def to_input(cases):
    lines = [str(len(cases))]
    for g in cases:
        lines.append(str(len(g)))
        lines += [" ".join(map(str, row)) for row in g]
    return "\n".join(lines) + "\n"


def reference(cases):
    """모든 순서를 itertools로 만들어 합을 비교한다 (가지치기 없음)"""
    out = []
    for tc, g in enumerate(cases, 1):
        n = len(g)
        best = min(sum(g[p[k]][p[k + 1]] for k in range(n - 1)) for p in permutations(range(n)))
        out.append("#%d %d" % (tc, best))
    return "\n".join(out) + "\n"


def mat(n, lo, hi):
    return [[0 if a == b else random.randint(lo, hi) for b in range(n)] for a in range(n)]


if __name__ == "__main__":
    sample = [[[0, 5, 2], [3, 0, 7], [4, 1, 0]], [[0]],
              [[0, 8, 3, 9], [4, 0, 6, 2], [7, 5, 0, 1], [6, 3, 8, 0]]]
    assert run(to_input(sample)) == "#1 3\n#2 0\n#3 7\n"
    assert run(to_input([[[0, 4, 1], [2, 0, 6], [5, 3, 0]]])) == "#1 3\n"
    assert run(to_input([[[0, 9], [4, 0]]])) == "#1 4\n"                       # N = 2: 1 → 0
    assert run(to_input([[[0 if a == b else 5 for b in range(5)] for a in range(5)]])) == "#1 20\n"  # 모두 같음

    random.seed(0)
    for _ in range(200):
        cases = [mat(random.randint(1, 6), 1, 20) for _ in range(random.randint(1, 10))]
        text = to_input(cases)
        assert run(text) == reference(cases), text

    big = [mat(9, 1, 100) for _ in range(10)]
    start = time.time()
    out = run(to_input(big))
    print(f"최대 입력(T=10, N=9): {time.time() - start:.2f}s")
    assert out == reference(big)
    print("all tests passed")
