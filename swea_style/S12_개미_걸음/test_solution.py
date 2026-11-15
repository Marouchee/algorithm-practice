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
    for n, k, r, c, d, g in cases:
        lines += ["%d %d" % (n, k), "%d %d %d" % (r, c, d)]
        lines += [" ".join(map(str, row)) for row in g]
    return "\n".join(lines) + "\n"


def reference(cases):
    """방향을 (dr, dc) 벡터 회전으로, 검은 칸은 set으로 (풀이와 다른 표현)"""
    out = []
    for tc, (n, k, r, c, d, g) in enumerate(cases, 1):
        black = {(i, j) for i in range(n) for j in range(n) if g[i][j]}
        vec = [(-1, 0), (0, 1), (1, 0), (0, -1)][d]
        pos, gone = (r, c), False
        for _ in range(k):
            dr, dc = vec
            if pos in black:
                vec = (-dc, dr)
                black.remove(pos)
            else:
                vec = (dc, -dr)
                black.add(pos)
            pos = (pos[0] + vec[0], pos[1] + vec[1])
            if not (0 <= pos[0] < n and 0 <= pos[1] < n):
                gone = True
                break
        out.append("#%d %d %d %d" % (tc, len(black), -1 if gone else pos[0], -1 if gone else pos[1]))
    return "\n".join(out) + "\n"


def rand_case(n, k, p):
    g = [[1 if random.random() < p else 0 for _ in range(n)] for _ in range(n)]
    return n, k, random.randrange(n), random.randrange(n), random.randrange(4), g


if __name__ == "__main__":
    sample = [(3, 4, 1, 1, 0, [[0] * 3 for _ in range(3)]),
              (4, 6, 2, 1, 0, [[1, 0, 0, 1], [0, 0, 0, 0], [0, 1, 0, 0], [1, 0, 0, 1]]),
              (2, 10, 0, 0, 0, [[0, 0], [0, 0]])]
    assert run(to_input(sample)) == "#1 4 1 1\n#2 7 3 0\n#3 3 -1 -1\n"
    assert run(to_input([(3, 5, 1, 1, 0, [[0] * 3 for _ in range(3)])])) == "#1 3 1 0\n"
    assert run(to_input([(1, 1, 0, 0, 0, [[0]])])) == "#1 1 -1 -1\n"            # 마지막 걸음에서 떠남
    assert run(to_input([(5, 1, 4, 2, 3, [[0] * 5 for _ in range(4)] + [[0, 0, 1, 0, 0]])])) == "#1 0 -1 -1\n"

    random.seed(0)
    for _ in range(200):
        cases = [rand_case(random.randint(1, 7), random.randint(1, 60), random.choice([0.0, 0.3, 0.6]))
                 for _ in range(random.randint(1, 10))]
        text = to_input(cases)
        assert run(text) == reference(cases), text

    big = [(100, 100000, 50, 50, 0, [[0] * 100 for _ in range(100)])]
    big += [rand_case(100, 100000, random.choice([0.0, 0.1, 0.5])) for _ in range(9)]
    start = time.time()
    out = run(to_input(big))
    print(f"최대 입력(T=10, N=100, K=100000): {time.time() - start:.2f}s")
    assert out == reference(big)
    print("all tests passed")
