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
    for k, a in cases:
        lines += ["%d %d" % (len(a), k), " ".join(map(str, a))]
    return "\n".join(lines) + "\n"


def reference(cases):
    """재귀로 카드마다 넣는다/뺀다를 정해 모든 합을 모은다 (빈 집합 제외)"""
    out = []
    for tc, (k, a) in enumerate(cases, 1):
        sums = []

        def go(i, s, picked):
            if i == len(a):
                if picked:
                    sums.append(s)
                return
            go(i + 1, s + a[i], True)
            go(i + 1, s, picked)

        go(0, 0, False)
        diffs = [abs(s - k) for s in sums]
        best = min(diffs)
        out.append("#%d %d %d" % (tc, best, diffs.count(best)))
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    sample = [(10, [3, 5, 6, 8]), (6, [1, 2, 3]), (100, [7]), (7, [1, 2, 3, 4, 5])]
    assert run(to_input(sample)) == "#1 1 3\n#2 0 1\n#3 93 1\n#4 0 3\n"
    assert run(to_input([(5, [2, 4, 6])])) == "#1 1 3\n"
    assert run(to_input([(1, [100])])) == "#1 99 1\n"              # 빈 집합(차이 K)을 세면 틀림
    assert run(to_input([(5, [10])])) == "#1 5 1\n"                # 빈 집합과 차이가 같은 경우
    assert run(to_input([(6, [3, 3, 3])])) == "#1 0 3\n"           # 같은 수의 카드도 다른 카드
    assert run(to_input([(1600, [100] * 16)])) == "#1 0 1\n"       # 전부 고르기

    random.seed(0)
    for _ in range(200):
        cases = [(random.randint(1, 60), [random.randint(1, 15) for _ in range(random.randint(1, 8))])
                 for _ in range(random.randint(1, 10))]
        text = to_input(cases)
        assert run(text) == reference(cases), text

    big = [(random.randint(1, 1600), [random.randint(1, 100) for _ in range(16)]) for _ in range(10)]
    start = time.time()
    out = run(to_input(big))
    print(f"최대 입력(T=10, N=16): {time.time() - start:.2f}s")
    assert out == reference(big)
    print("all tests passed")
