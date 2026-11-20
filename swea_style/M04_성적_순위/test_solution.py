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
    for sc, k in cases:
        lines.append("%d %d" % (len(sc), k))
        lines += ["%d %d %d" % row for row in sc]
    return "\n".join(lines) + "\n"


def reference(cases):
    """정렬 없이 앞선 학생 수를 직접 세어 순위를 정한다 O(N²) (풀이와 다른 방법)"""
    out = []
    for tc, (sc, k) in enumerate(cases, 1):
        keys = [(a + b + c, c, b, -i) for i, (a, b, c) in enumerate(sc, 1)]
        for i, key in enumerate(keys, 1):
            if sum(1 for other in keys if other > key) == k - 1:
                out.append("#%d %d %d" % (tc, i, key[0]))
                break
    return "\n".join(out) + "\n"


def scores(n, lo, hi):
    return [(random.randint(lo, hi), random.randint(lo, hi), random.randint(lo, hi)) for _ in range(n)]


if __name__ == "__main__":
    sample = [([(80, 90, 70), (95, 60, 85), (70, 70, 70), (100, 100, 100), (60, 90, 90)], 2),
              ([(0, 0, 0)], 1), ([(50, 60, 70), (90, 50, 40), (60, 50, 70), (100, 10, 70)], 3)]
    assert run(to_input(sample)) == "#1 5 240\n#2 1 0\n#3 4 180\n"
    tie = [(90, 80, 70), (70, 80, 90), (80, 90, 70), (80, 70, 90)]     # 총점 같음 → 수학 → 영어
    same = [(50, 50, 50)] * 6                                         # 완전 동점 → 번호 순
    edge = [(tie, k) for k in range(1, 5)] + [(same, k) for k in (1, 4, 6)]
    assert run(to_input(edge)) == reference(edge)

    random.seed(0)
    for _ in range(200):
        cases = []
        for _ in range(random.randint(1, 10)):
            n = random.randint(1, 12)
            cases.append((scores(n, *random.choice([(0, 100), (0, 3), (98, 100)])), random.randint(1, n)))
        assert run(to_input(cases)) == reference(cases), cases

    big = [(scores(1000, *[(0, 100), (99, 100)][t % 2]), random.randint(1, 1000)) for t in range(10)]
    start = time.time()
    out = run(to_input(big))
    print(f"최대 입력(T=10, N=1000): {time.time() - start:.2f}s")
    assert out == reference(big)
    print("all tests passed")
