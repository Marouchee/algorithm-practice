import random
import time

from solution import all_paths, solution


def make_case(r, c, wall, m):
    while True:
        grid = ["".join("#" if random.random() < wall else "." for _ in range(c)) for _ in range(r)]
        cells = [(i, j) for i in range(r) for j in range(c) if grid[i][j] == "."]
        if len(cells) >= m:
            pts = random.sample(cells, m)
            return grid, [[i + 1, j + 1] for i, j in pts]


def test_examples():
    assert solution(["...", "...", "..."], [[1, 1], [3, 3]], 8) == 12
    assert solution(["...", ".#.", "..."], [[1, 1], [1, 3], [3, 3]], 8) == 1
    assert solution(["...", "...", "..."], [[1, 1], [3, 3]], 4) == 6      # 최단 경로만 남음


def test_edges():
    assert solution(["..", ".."], [[1, 1], [1, 2]], 1) == 1               # 바로 옆, K = 1
    assert solution(["..", ".."], [[1, 1], [2, 2]], 2) == 2               # 해제가 없으면 1
    assert solution(["....", "....", "...."], [[1, 1], [3, 4]], 2) == 0   # K 부족
    # 앞 구간이 밟은 칸 때문에 뒤 구간 경로가 줄어듦: 구간별 곱은 1 × 2 = 2
    assert solution(["..", ".."], [[1, 1], [1, 2], [2, 2]], 3) == 1
    grid = ["....", ".##.", ".##.", "...."]
    assert solution(grid, [[1, 1], [4, 4], [1, 4]], 15) == 1              # 왼쪽 아래로 돌아야만 함


def test_random_against_all_paths():
    random.seed(0)
    for _ in range(2000):
        r, c = random.randint(2, 4), random.randint(2, 4)
        grid, cps = make_case(r, c, random.choice([0, 0.1, 0.25]), random.randint(2, min(5, r * c)))
        k = random.randint(1, r * c)
        assert solution(grid, cps, k) == all_paths(grid, cps, k), (grid, cps, k)


def test_largest():
    grid = ["....", "....", "....", "...."]
    start = time.time()
    assert solution(grid, [[1, 1], [4, 4]], 16) == all_paths(grid, [[1, 1], [4, 4]], 16)
    assert solution(grid, [[i, j] for i in range(1, 5) for j in (range(1, 5) if i % 2 else range(4, 0, -1))], 16) == 1
    assert time.time() - start < 1.0


if __name__ == "__main__":
    test_examples()
    test_edges()
    test_random_against_all_paths()
    test_largest()
    print("all tests passed")
