"""프로그래머스 Lv.3 등굣길 (DP)
https://school.programmers.co.kr/learn/courses/30/lessons/42898

접근: dp[i][j] = 집 (0, 0)에서 (i, j)까지 가는 최단 경로 수 = 위 (i-1, j) + 왼쪽 (i, j-1). 웅덩이는 0.
      첫 행·첫 열은 1로 채우되, 첫 행에 웅덩이가 있으면 그 열부터 오른쪽 끝까지, 첫 열에 있으면 그 행부터 아래 끝까지 0.
      m은 열, n은 행, 웅덩이 [a, b]는 [열, 행]이다. 칸마다 1,000,000,007로 나눈 나머지를 저장한다.
      (첫 행·첫 열을 지우는 range 시작값에 행·열 좌표를 바꿔 넣어 80점이 두 번 나왔다)
시간 복잡도: O(m · n). 칸마다 덧셈 한 번. 웅덩이 처리는 웅덩이(최대 10개)마다 최대 max(m, n)번
"""
import random
import time

MOD = 1_000_000_007


def solution(m, n, puddles):
    answer = 0
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        dp[0][i] = 1
    for i in range(n):
        dp[i][0] = 1

    for item in puddles:
        dp[item[1]-1][item[0]-1] = 0
        if item[1] == 1:
            for i in range(item[0]-1,m):
                dp[0][i] = 0
        if item[0] == 1:
            for i in range(item[1]-1,n):
                dp[i][0] = 0

    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] == 0:
                continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1_000_000_007
    answer = dp[n-1][m-1] % 1_000_000_007
    return answer


def by_padding(m, n, puddles):
    """한 칸씩 여백을 둔 (n+1) × (m+1) 표로 첫 행·첫 열 예외를 없애는 방식 (비교용)"""
    wet = {(b, a) for a, b in puddles}
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if (r, c) == (1, 1) or (r, c) in wet:
                continue
            dp[r][c] = (dp[r - 1][c] + dp[r][c - 1]) % MOD
    return dp[n][m]


def all_paths(m, n, puddles):
    """오른쪽·아래로만 움직이는 경로를 재귀로 전부 센다 (작은 입력 검증용)"""
    wet = {(b - 1, a - 1) for a, b in puddles}

    def go(r, c):
        if r >= n or c >= m or (r, c) in wet:
            return 0
        if (r, c) == (n - 1, m - 1):
            return 1
        return go(r + 1, c) + go(r, c + 1)

    return go(0, 0) % MOD


if __name__ == "__main__":
    assert solution(4, 3, [[2, 2]]) == 4
    assert solution(3, 2, [[2, 1]]) == 1      # 첫 행 가운데 웅덩이
    assert solution(3, 2, [[3, 1]]) == 2      # 첫 행 오른쪽 끝 웅덩이: 그 왼쪽 칸은 살아 있어야 함
    assert solution(2, 3, [[1, 3]]) == 2      # 첫 열 맨 아래 웅덩이
    assert solution(3, 3, [[2, 1], [1, 2]]) == 0   # 집에서 나가는 두 칸이 모두 웅덩이
    assert solution(1, 1, []) == 1
    assert solution(100, 100, []) == by_padding(100, 100, [])   # 나머지 연산 필요한 크기

    random.seed(0)
    for _ in range(3000):
        m, n = random.randint(1, 7), random.randint(1, 7)
        cells = [(a, b) for a in range(1, m + 1) for b in range(1, n + 1) if (a, b) not in ((1, 1), (m, n))]
        puddles = [list(c) for c in random.sample(cells, min(len(cells), random.randint(0, 10)))]
        assert solution(m, n, puddles) == by_padding(m, n, puddles) == all_paths(m, n, puddles), (m, n, puddles)

    big_cells = [(a, b) for a in range(1, 101) for b in range(1, 101) if (a, b) not in ((1, 1), (100, 100))]
    big_puddles = [list(c) for c in random.sample(big_cells, 10)]
    start = time.time()
    assert solution(100, 100, big_puddles) == by_padding(100, 100, big_puddles)
    print(f"100x100: {time.time() - start:.3f}s")
    print("all tests passed")
