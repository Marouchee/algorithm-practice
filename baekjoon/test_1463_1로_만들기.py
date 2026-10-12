"""1463 풀이를 표준 입력으로 실행해, 연산 그래프를 BFS로 탐색한 최솟값과 비교한다."""
import random
import subprocess
import sys
import time
from collections import deque
from pathlib import Path

SOLUTION = Path(__file__).parent / "1463_1로_만들기.py"


def run(n: int) -> int:
    out = subprocess.run([sys.executable, str(SOLUTION)], input=f"{n}\n",
                         capture_output=True, text=True, check=True).stdout
    return int(out)


def bfs(n: int) -> int:
    dist = {n: 0}
    q = deque([n])
    while q:
        x = q.popleft()
        if x == 1:
            return dist[x]
        nexts = [x - 1]
        if x % 2 == 0:
            nexts.append(x // 2)
        if x % 3 == 0:
            nexts.append(x // 3)
        for y in nexts:
            if y not in dist:
                dist[y] = dist[x] + 1
                q.append(y)


if __name__ == "__main__":
    assert run(1) == 0      # 반복 0번, dp[1] 그대로
    assert run(2) == 1
    assert run(3) == 1
    assert run(10) == 3     # 그리디(10 5 4 2 1)면 4

    random.seed(0)
    for n in random.sample(range(4, 5000), 200):
        assert run(n) == bfs(n), n

    start = time.time()
    assert run(1_000_000) == bfs(1_000_000)
    print(f"N=1,000,000: {time.time() - start:.2f}s")
    print("all tests passed")
