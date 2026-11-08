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


def rotate(g):
    """시계 방향 90도: 왼쪽 열을 아래에서 위로 읽은 것이 새 첫 행"""
    return [list(row) for row in zip(*g[::-1])]


def to_input(cases):
    lines = [str(len(cases))]
    for a, b in cases:
        lines.append(str(len(a)))
        lines += [" ".join(map(str, row)) for row in a + b]
    return "\n".join(lines) + "\n"


def reference(cases):
    out = []
    for tc, (a, b) in enumerate(cases, 1):
        ans, cur = -1, a
        for k in range(4):
            if cur == b:
                ans = k
                break
            cur = rotate(cur)
        out.append("#%d %d" % (tc, ans))
    return "\n".join(out) + "\n"


def case(n, hi):
    a = [[random.randint(0, hi) for _ in range(n)] for _ in range(n)]
    b = a
    for _ in range(random.randint(0, 3)):
        b = rotate(b)
    b = [row[:] for row in b]
    if random.random() < 0.3:
        i, j = random.randrange(n), random.randrange(n)
        b[i][j] = (b[i][j] + 1) % (hi + 1)
    return a, b


if __name__ == "__main__":
    g3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sample = [(g3, [[9, 8, 7], [6, 5, 4], [3, 2, 1]]), ([[1, 0], [0, 1]], [[0, 1], [1, 0]]),
              ([[1, 2], [3, 4]], [[2, 4], [1, 3]]), ([[1, 2], [3, 4]], [[1, 2], [4, 3]])]
    assert run(to_input(sample)) == "#1 2\n#2 1\n#3 3\n#4 -1\n"
    assert rotate(g3) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert run(to_input([([[5]], [[5]])])) == "#1 0\n"                                  # N = 1
    assert run(to_input([([[5]], [[6]])])) == "#1 -1\n"
    plus = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    assert run(to_input([(plus, plus)])) == "#1 0\n"                                    # 대칭: 가장 작은 횟수 0
    assert run(to_input([(g3, [[3, 6, 9], [2, 5, 8], [1, 4, 7]])])) == "#1 3\n"         # 반시계 1번 = 시계 3번

    random.seed(0)
    for _ in range(200):
        cases = [case(random.randint(1, 6), random.choice([1, 9])) for _ in range(random.randint(1, 10))]
        text = to_input(cases)
        assert run(text) == reference(cases), text

    big = [case(50, 9) for _ in range(10)]
    start = time.time()
    assert run(to_input(big)) == reference(big)
    print(f"최대 입력(T=10, N=50): {time.time() - start:.2f}s")
    print("all tests passed")
