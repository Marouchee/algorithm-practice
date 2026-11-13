"""solution.py를 표준 입력으로 실행해 출력 전체를 비교한다"""
import os
import random
import subprocess
import sys
import time
from bisect import bisect_right

HERE = os.path.dirname(os.path.abspath(__file__))
SOLUTION = os.path.join(HERE, "solution.py")


def run(text):
    return subprocess.run([sys.executable, SOLUTION], input=text, capture_output=True,
                          text=True, check=True).stdout


def to_input(cases):
    lines = [str(len(cases))]
    for c in cases:
        lines.append(str(len(c)))
        lines += ["%d %d" % iv for iv in c]
    return "\n".join(lines) + "\n"


def reference(cases):
    """DP + 이분탐색: dp[k] = 끝 순으로 앞 k개에서 고를 수 있는 최대 개수 (그리디와 다른 방법)"""
    out = []
    for tc, c in enumerate(cases, 1):
        iv = sorted(c, key=lambda x: x[1])
        ends = [e for _, e in iv]
        dp = [0] * (len(iv) + 1)
        for k in range(1, len(iv) + 1):
            s = iv[k - 1][0]
            dp[k] = max(dp[k - 1], dp[bisect_right(ends, s, 0, k - 1)] + 1)
        out.append("#%d %d" % (tc, dp[-1]))
    return "\n".join(out) + "\n"


def rand_iv(n, tmax, lmax):
    out = []
    for _ in range(n):
        s = random.randint(0, tmax - 1)
        out.append((s, min(tmax, s + random.randint(1, lmax))))
    return out


if __name__ == "__main__":
    sample = [[(1, 4), (3, 5), (0, 6), (5, 7), (8, 9)], [(1, 10), (2, 3), (4, 5)],
              [(1, 3), (3, 5), (5, 7), (2, 6)]]
    assert run(to_input(sample)) == "#1 3\n#2 2\n#3 3\n"
    assert run(to_input([[(0, 4), (3, 6), (5, 9)]])) == "#1 2\n"
    assert run(to_input([[(3, 7)], [(2, 5)] * 4, [(0, 1)]])) == "#1 1\n#2 1\n#3 1\n"   # N=1, 전부 같음, 시작 0
    assert run(to_input([[(0, 100), (0, 10), (10, 20), (20, 30)]])) == "#1 3\n"         # 큰 하나가 덮음

    random.seed(0)
    for _ in range(200):
        cases = [rand_iv(random.randint(1, 12), random.choice([10, 20, 50]), random.choice([3, 8, 20]))
                 for _ in range(random.randint(1, 10))]
        text = to_input(cases)
        assert run(text) == reference(cases), text

    big = [rand_iv(10000, 1000000, random.choice([50, 5000, 300000])) for _ in range(8)]
    big += [[(i, i + 1) for i in range(10000)], [(0, 1000000)] + [(i * 100, i * 100 + 150) for i in range(9999)]]
    start = time.time()
    out = run(to_input(big))
    print(f"최대 입력(T=10, N=10000): {time.time() - start:.2f}s")
    assert out == reference(big)
    print("all tests passed")
