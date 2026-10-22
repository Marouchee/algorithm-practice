"""003. 순찰 로봇 (백트래킹) — 문제: problem.md

접근: dfs(x, y, idx, moves)가 "지금 (x, y)에서 idx번 체크포인트를 찾는 중이고 moves번 움직였을 때 끝까지 갈 수 있는 경로 수"를 반환한다.
      방문 표시 → 재귀 → 해제로 한 경로를 끝까지 따라간 뒤 되돌아온다. 목표 체크포인트 칸에 들어서면 idx + 1, 차례가 아닌 체크포인트 칸은 건너뛴다.
      (처음에는 등굣길의 격자 DP를 가져왔고, 다음에는 체크포인트 구간마다 따로 세어 곱했다. 앞 구간이 밟은 칸에 따라 뒤 구간의 경로 수가 달라져 곱할 수 없다)
시간 복잡도: 상한 O(4 · 3^(L-1)), L = min(K, R·C - 1). 4×4면 약 1,900만이지만 재방문 금지로 빈 4×4 모서리 출발 전체 경로도 dfs 호출 약 2,100번
"""


def solution(grid, checkpoints, k):
    n = len(grid)
    m = len(grid[0])
    cps = [(r - 1, c - 1) for r, c in checkpoints]
    n_list = [(1,0), (-1,0), (0,1), (0,-1)]
    visit = [[False for _ in range(m)] for _ in range(n)]

    def dfs(x, y, idx, moves):
        if idx == len(cps):
            return 1
        if moves == k:
            return 0
        count = 0
        for a,b in n_list:
            nx = x+a
            ny = y+b
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if grid[nx][ny] == '#' or visit[nx][ny]:
                continue
            if (nx,ny) in cps and (nx,ny) != cps[idx]:
                continue
            if (nx, ny) == cps[idx]:
                nidx = idx + 1
            else:
                nidx = idx
            visit[nx][ny] = True
            count += dfs(nx, ny, nidx, moves + 1)
            visit[nx][ny] = False
        return count

    sx,sy = cps[0]
    visit[sx][sy] = True

    return dfs(sx,sy,1,0)


def all_paths(grid, checkpoints, k):
    """출발 칸에서 갈 수 있는 모든 단순 경로를 만든 뒤 조건을 사후 검사 (작은 입력 검증용)"""
    n, m = len(grid), len(grid[0])
    cps = [(r - 1, c - 1) for r, c in checkpoints]
    total = 0
    stack = [(cps[0],)]
    while stack:
        path = stack.pop()
        if path[-1] == cps[-1]:
            idx = [path.index(p) if p in path else -1 for p in cps]
            if len(path) - 1 <= k and min(idx) >= 0 and idx == sorted(idx):
                total += 1
            continue
        x, y = path[-1]
        for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + a, y + b
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "." and (nx, ny) not in path:
                stack.append(path + ((nx, ny),))
    return total
