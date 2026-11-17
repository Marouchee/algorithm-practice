"""solution.py와 solution_minutes.py를 표준 입력으로 실행해 출력 전체를 비교한다"""
import os
import random
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SOLUTIONS = [os.path.join(HERE, name) for name in ("solution.py", "solution_minutes.py")]


def run_one(path, text):
    return subprocess.run([sys.executable, path], input=text, capture_output=True,
                          text=True, check=True).stdout


def run(text):
    """두 풀이를 모두 실행하고 출력이 같은지 확인한다"""
    outs = [run_one(path, text) for path in SOLUTIONS]
    assert outs[0] == outs[1], text
    return outs[0]


def hm(t):
    return "%02d:%02d" % (t // 60, t % 60)


def to_input(cases):
    lines = [str(len(cases))]
    for g in cases:
        lines.append(str(len(g)))
        lines += ["%s %s %d" % (hm(a), hm(b), p) for a, b, p in g]
    return "\n".join(lines) + "\n"


def reference(cases):
    """분 단위 차분 배열로 누적 (풀이와 다른 방법)"""
    out = []
    for tc, g in enumerate(cases, 1):
        diff = [0] * 1441
        for a, b, p in g:
            diff[a] += p
            diff[b] -= p
        cur, best, best_t = 0, -1, 0
        for t in range(1440):
            cur += diff[t]
            if cur > best:
                best, best_t = cur, t
        out.append("#%d %d %s" % (tc, best, hm(best_t)))
    return "\n".join(out) + "\n"


def rand_group(lo, hi, pmax):
    a = random.randint(lo, hi - 1)
    return (a, random.randint(a + 1, hi), random.randint(1, pmax))


if __name__ == "__main__":
    sample = [[(540, 690, 3), (600, 630, 5), (690, 720, 4), (615, 720, 2)], [(0, 1439, 7)],
              [(480, 540, 5), (720, 780, 2), (750, 765, 3)]]
    assert run(to_input(sample)) == "#1 10 10:15\n#2 7 00:00\n#3 5 08:00\n"
    assert run(to_input([[(600, 630, 5), (630, 660, 5), (660, 690, 5)]])) == "#1 5 10:00\n"   # 꼬리 물기
    assert run(to_input([[(1438, 1439, 100)], [(5, 6, 1)] * 3])) == "#1 100 23:58\n#2 3 00:05\n"

    random.seed(0)
    for _ in range(200):
        cases = []
        for _ in range(random.randint(1, 10)):
            lo = random.choice([0, 600])
            hi = random.choice([lo + 10, lo + 120, 1439])
            cases.append([rand_group(lo, hi, random.choice([3, 100])) for _ in range(random.randint(1, 12))])
        text = to_input(cases)
        assert run(text) == reference(cases), text

    big = [[(t, t + 1, 100) for t in range(1000)]] + [[rand_group(0, 1439, 100) for _ in range(1000)] for _ in range(9)]
    start = time.time()
    out = run(to_input(big))
    print(f"최대 입력(T=10, N=1000): {time.time() - start:.2f}s")
    assert out == reference(big)
    print("all tests passed")
