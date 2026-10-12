"""프로그래머스 Lv.3 네트워크 (DFS)
https://school.programmers.co.kr/learn/courses/30/lessons/43162

접근: 아직 방문하지 않은 컴퓨터에서 DFS를 시작하면, 그 컴퓨터와 연결된 컴퓨터를 모두 방문 처리한다.
      DFS를 새로 시작한 횟수가 네트워크 개수다. dfs(com)은 들어오자마자 방문 표시를 하고,
      연결되어 있고(computers[com][i] == 1) 방문하지 않은 i로 넘어간다 (리턴하지 않고 호출만 해서 모든 이웃을 본다).
시간 복잡도: O(n²). 컴퓨터마다 dfs 1번, dfs 안에서 n번 확인 (n = 200이면 40,000)
"""
import random
import time


def solution(n, computers):
    answer = 0
    visit = [-1 for _ in range(n)]
    
    def dfs(com):
        visit[com] = 1
        for i in range(n):
            if visit[i] == -1 and computers[com][i] == 1:
                dfs(i)
    
    for i in range(n):
        if visit[i] == -1:
            visit[i] = 1
            dfs(i)
            answer += 1
    
    return answer


def union_find(n, computers):
    """같은 그룹끼리 대표를 합쳐 대표 수를 센다 (비교용)"""
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                parent[find(i)] = find(j)
    return len({find(i) for i in range(n)})


def make(n, edges):
    c = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for a, b in edges:
        c[a][b] = c[b][a] = 1
    return c


if __name__ == "__main__":
    assert solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1
    assert solution(1, [[1]]) == 1
    assert solution(4, make(4, [(0, 1), (2, 3)])) == 2
    assert solution(3, make(3, [(0, 1), (0, 2)])) == 1     # return dfs(i)로 쓰면 2를 따로 세서 2

    random.seed(0)
    for _ in range(3000):
        n = random.randint(1, 12)
        edges = [(a, b) for a in range(n) for b in range(a + 1, n) if random.random() < 0.2]
        c = make(n, edges)
        assert solution(n, c) == union_find(n, c), (n, edges)

    start = time.time()
    assert solution(200, make(200, [(i, i + 1) for i in range(199)])) == 1   # 재귀 깊이 200
    assert solution(200, [[1] * 200 for _ in range(200)]) == 1
    assert solution(200, make(200, [])) == 200
    print(f"n=200 x3: {time.time() - start:.3f}s")
    print("all tests passed")
