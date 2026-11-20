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
    return "\n".join([str(len(cases))] + ["%s %d" % (s, k) for s, k in cases]) + "\n"


def reference(cases):
    """펼치지 않고 정규식으로 (글자, 횟수)를 읽으며 길이를 누적 (풀이와 다른 방법)"""
    import re
    out = []
    for tc, (s, k) in enumerate(cases, 1):
        total, ans = 0, ""
        for ch, num in re.findall(r"([a-z])(\d*)", s):
            cnt = int(num) if num else 1
            if not ans and total + cnt >= k:
                ans = ch
            total += cnt
        out.append("#%d %d %s" % (tc, total, ans))
    return "\n".join(out) + "\n"


def build(max_len, letters, nums):
    parts, length, total = [], 0, 0
    while True:
        ch, num = random.choice(letters), random.choice(nums)
        piece = ch + ("" if num is None else str(num))
        if length + len(piece) > max_len:
            break
        parts.append(piece)
        length += len(piece)
        total += 1 if num is None else num
    if not parts:
        return "a", 1
    return "".join(parts), total


if __name__ == "__main__":
    sample = [("a3bc12d", 5), ("x", 1), ("k10m2k", 12)]
    assert run(to_input(sample)) == "#1 17 c\n#2 1 x\n#3 13 m\n"
    edge = [("a", 1), ("z999", 999), ("a12b3", 12), ("a12b3", 13), ("a1b1c1", 2), ("a10a100b", 111), ("abcde", 5)]
    assert run(to_input(edge)) == reference(edge)

    random.seed(0)
    for _ in range(200):
        cases = []
        for _ in range(random.randint(1, 10)):
            s, total = build(random.randint(1, 15), "abc", [None, None, 1, 2, 9, 10, 12, 100, 101])
            cases.append((s, random.randint(1, total)))
        assert run(to_input(cases)) == reference(cases), cases

    big = []
    for _ in range(10):
        s, total = build(1000, "abcdefghijklmnopqrstuvwxyz", [999, 998, 100, None])
        big.append((s, random.choice([1, total, random.randint(1, total)])))
    start = time.time()
    out = run(to_input(big))
    print(f"최대 입력(T=10, |S|=1000): {time.time() - start:.2f}s")
    assert out == reference(big)
    print("all tests passed")
