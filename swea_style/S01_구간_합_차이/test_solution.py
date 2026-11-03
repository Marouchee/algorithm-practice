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
    for k, (n, m, a) in enumerate(cases, 1):
        sums = [sum(a[i:i + m]) for i in range(n - m + 1)]
        out.append("#%d %d" % (k, max(sums) - min(sums)))
    return "\n".join(out) + "\n"


def to_input(cases):
    lines = [str(len(cases))]
    for n, m, a in cases:
        lines.append("%d %d" % (n, m))
        lines.append(" ".join(map(str, a)))
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    sample = [(5, 3, [1, 2, 3, 4, 5]), (10, 4, [3, 8, 1, 9, 2, 7, 4, 6, 5, 10])]
    assert run(to_input(sample)) == "#1 6\n#2 6\n"
    assert run(to_input([(5, 2, [4, 1, 3, 5, 2])])) == "#1 4\n"
    assert run(to_input([(1, 1, [7])])) == "#1 0\n"                          # N = M = 1
    assert run(to_input([(4, 4, [1, 2, 3, 4])])) == "#1 0\n"                 # M = N: 묶음 1개
    assert run(to_input([(1000, 1000, [10000] * 1000)])) == "#1 0\n"         # 묶음 합 최댓값 10^7

    random.seed(0)
    for _ in range(200):
        cases = []
        for _ in range(random.randint(1, 10)):
            n = random.randint(1, 30)
            cases.append((n, random.randint(1, n), [random.randint(1, 20) for _ in range(n)]))
        text = to_input(cases)
        assert run(text) == reference(cases), text

    big = [(1000, 500, [random.randint(1, 10000) for _ in range(1000)]) for _ in range(10)]
    start = time.time()
    assert run(to_input(big)) == reference(big)
    print(f"최대 입력(T=10, N=1000, M=500): {time.time() - start:.2f}s")
    print("all tests passed")
