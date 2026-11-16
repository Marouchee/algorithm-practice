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
    for n, m, cap, r, c, d, g, cmd in cases:
        lines += ["%d %d %d" % (n, m, cap), "%d %d %d" % (r, c, d)] + g + [cmd]
    return "\n".join(lines) + "\n"


def reference(cases):
    """방향을 (dr, dc) 벡터 회전으로, 택배는 set으로 (풀이와 다른 표현)"""
    out = []
    for tc, (n, m, cap, r, c, d, g, cmd) in enumerate(cases, 1):
        wall = {(i, j) for i in range(n) for j in range(m) if g[i][j] == '#'}
        parcel = {(i, j) for i in range(n) for j in range(m) if g[i][j] == 'P'}
        dock = {(i, j) for i in range(n) for j in range(m) if g[i][j] == 'D'}
        vec = [(-1, 0), (0, 1), (1, 0), (0, -1)][d]
        pos, carry, done = (r - 1, c - 1), 0, 0
        for ch in cmd:
            if ch == 'R':
                vec = (vec[1], -vec[0])
            elif ch == 'L':
                vec = (-vec[1], vec[0])
            else:
                nxt = (pos[0] + vec[0], pos[1] + vec[1])
                if not (0 <= nxt[0] < n and 0 <= nxt[1] < m) or nxt in wall:
                    vec = (-vec[0], -vec[1])
                    continue
                pos = nxt
                if pos in parcel and carry < cap:
                    parcel.remove(pos)
                    carry += 1
                elif pos in dock:
                    done += carry
                    carry = 0
        out.append("#%d %d %d %d %d" % (tc, pos[0] + 1, pos[1] + 1, done, len(parcel)))
    return "\n".join(out) + "\n"


def make(n, m, cap, length, pw=0.2, pp=0.15, pd=0.05):
    g = []
    for _ in range(n):
        row = ""
        for _ in range(m):
            x = random.random()
            row += '#' if x < pw else 'P' if x < pw + pp else 'D' if x < pw + pp + pd else '.'
        g.append(row)
    r, c = random.randrange(n), random.randrange(m)
    g[r] = g[r][:c] + '.' + g[r][c + 1:]
    return (n, m, cap, r + 1, c + 1, random.randrange(4), g, "".join(random.choices("LRF", weights=(1, 1, 3), k=length)))


if __name__ == "__main__":
    sample = [(4, 5, 2, 1, 1, 1, [".PP.#", ".#P..", ".D...", "P...D"], "FFFRFFRFFLF"),
              (1, 3, 5, 1, 2, 3, ["P.D"], "FFFF")]
    assert run(to_input(sample)) == "#1 4 2 2 2\n#2 1 3 1 0\n"
    assert run(to_input([(1, 1, 1, 1, 1, 0, ["."], "FFFRF")])) == "#1 1 1 0 0\n"                 # 1×1
    assert run(to_input([(1, 7, 1, 1, 1, 1, [".PPP.D."], "FFFFFFFFFFFFFFFFFF")])) == "#1 1 5 1 1\n"  # 용량 1: 꽉 차면 지나감
    assert run(to_input([(1, 3, 2, 1, 1, 1, [".PP"], "FF")])) == "#1 1 3 0 0\n"                   # 들고 있는 건 안 셈

    random.seed(0)
    for _ in range(200):
        cases = [make(random.randint(1, 6), random.randint(1, 6), random.randint(1, 3), random.randint(1, 40),
                      random.choice([0, 0.2]), random.choice([0.2, 0.5]), random.choice([0.05, 0.2]))
                 for _ in range(random.randint(1, 10))]
        text = to_input(cases)
        assert run(text) == reference(cases), text

    big = [make(50, 50, random.randint(1, 10), 1000, random.choice([0.1, 0.3]), 0.3, 0.03) for _ in range(10)]
    start = time.time()
    out = run(to_input(big))
    print(f"최대 입력(T=10, 50×50, 명령 1000): {time.time() - start:.2f}s")
    assert out == reference(big)
    print("all tests passed")
