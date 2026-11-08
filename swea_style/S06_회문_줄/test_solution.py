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
        lines += g
    return "\n".join(lines) + "\n"


def reference(cases):
    """가로 줄과 세로 줄을 모두 글자열로 만들고, 가능한 구간을 전부 검사한다"""
    out = []
    for tc, g in enumerate(cases, 1):
        lines = list(g) + ["".join(col) for col in zip(*g)]
        lengths = [b - a for s in lines for a in range(len(s)) for b in range(a + 2, len(s) + 1)
                   if s[a:b] == s[a:b][::-1]]
        best = max(lengths, default=0)
        out.append("#%d %d %d" % (tc, best, lengths.count(best) if best else 0))
    return "\n".join(out) + "\n"


def grid(n, m, letters):
    return ["".join(random.choice(letters) for _ in range(m)) for _ in range(n)]


if __name__ == "__main__":
    sample = [["ABBA", "CACB", "ABCA"], ["AB", "BA"], ["ABCBA", "BACAB", "CCACC", "BACAB"]]
    assert run(to_input(sample)) == "#1 4 1\n#2 0 0\n#3 5 4\n"
    assert run(to_input([["ABA", "CBC", "ACA"]])) == "#1 3 5\n"
    assert run(to_input([["AAB"]])) == "#1 2 1\n"                 # 길이 2가 줄 맨 앞
    assert run(to_input([["BAA"]])) == "#1 2 1\n"                 # 길이 2가 줄 맨 끝
    assert run(to_input([["A"]])) == "#1 0 0\n"                   # 한 칸
    assert run(to_input([["A", "A", "B"]])) == "#1 2 1\n"         # 한 열
    assert run(to_input([["AAA", "AAA"]])) == "#1 3 2\n"          # 전부 같은 글자: 가로 3이 두 줄

    random.seed(0)
    for _ in range(200):
        cases = [grid(random.randint(1, 7), random.randint(1, 7), random.choice(["AB", "ABC"]))
                 for _ in range(random.randint(1, 10))]
        text = to_input(cases)
        assert run(text) == reference(cases), text

    big = [grid(30, 30, "AB") for _ in range(10)]
    start = time.time()
    assert run(to_input(big)) == reference(big)
    print(f"최대 입력(T=10, 30×30): {time.time() - start:.2f}s")
    print("all tests passed")
